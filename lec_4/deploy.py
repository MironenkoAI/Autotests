from sshcheckers import ssh_checkout, upload_files
import yaml

with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)


def deploy():
    res = []
    upload_files(data.get("host"), data.get("user"), data.get("passwd"), data.get("local_path"),
                 data.get("remote_path"))
    res.append(ssh_checkout(data.get("host"), data.get("user"), data.get("passwd"),
                            f'echo {data.get("passwd")} | sudo -S dpkg -i {data.get("remote_path")}',
                            "Настраивается пакет"))
    res.append(ssh_checkout(data.get("host"), data.get("user"), data.get("passwd"),
                            f'echo {data.get("passwd")} | sudo -S dpkg -s {data.get("filename")}',
                            "Status: install ok installed"))
    return all(res)


if deploy():
    print("Деплой успешен")
else:
    print("Ошибка деплоя")
