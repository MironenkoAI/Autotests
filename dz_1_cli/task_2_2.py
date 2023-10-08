import subprocess
import re


def main(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    my_out = result.stdout
    print(my_out)
    print('*' * 50)
    my_out = my_out.replace('_', ' ')
    clean_out = re.sub(r'[^\w\s]', ' ', my_out)
    print(clean_out)
    print('*' * 50)
    if result.returncode == 0:
        if text in clean_out:
            print('True')
        else:
            print('False')


if __name__ == "__main__":
    main("cat /etc/os-release", "CODENAME")
