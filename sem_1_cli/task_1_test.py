# Написать автотест на Python, который читает содержимое файла
# и выводит на экран SUCCESS, если в тексте содержатся заданные слова.
# В противном случает выводит FAIL.
import subprocess


def main():
    result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out = result.stdout
    if result.returncode == 0:
        # print(result)
        # print('*' * 50)
        # print(out)
        # print('*' * 50)
        # print(result.returncode)
        if "22.04.1" in out and "jammy" in out:
            print('SUCCESS')
        else:
            print('FAIL')


if __name__ == "__main__":
    main()