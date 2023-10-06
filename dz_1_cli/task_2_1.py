# Задание 2: (повышенной сложности)
# Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный
# режим работы, в котором вывод разбивается на слова с удалением всех знаков пунктуации (их
# можно взять из списка string.punctuation модуля string). В этом режиме должно проверяться
# наличие слова в выводе.
import subprocess
import string


def clean_text(out):
    clean_out = str.maketrans('', '', string.punctuation)
    return out.translate(clean_out)


def main(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    print(result.stdout)
    print('*' * 50)
    my_out = clean_text(result.stdout)
    print(my_out)
    print('*' * 50)
    if result.returncode == 0:
        if text in my_out:
            print('True')
        else:
            print('False')


if __name__ == "__main__":
    main("cat /etc/os-release", "ID")
