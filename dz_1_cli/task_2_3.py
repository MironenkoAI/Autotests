import subprocess
import string


def find_text_in_command_output(command, text):
    output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8").stdout
    output = output.translate(str.maketrans("", "", string.punctuation))
    words = output.split()
    if text in words:
        print("Команда выполнена успешно и слово найдено.")
        return True
    else:
        print("Команда не выполнена или слово не найдено.")
        return False


# Пример использования функции
if __name__ == "__main__":
    cmd = "cat /etc/os-release"
    txt = "Jammy"
    find_text_in_command_output(cmd, txt)
