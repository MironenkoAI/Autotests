# Задание 1:
# Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).
import subprocess

folder_out = "/home/user/folder_out/"
folder_ext = "/home/user/folder_ext/"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


# показать файлы в папке не запуская
def test_7z_l():
    assert checkout(f'cd {folder_out}; 7z l ./archiv.7z', "Listing archive: ./archiv.7z"), "test_l FAIL"


# разархивировать файлы из папки
def test_7z_x():
    assert checkout(f'cd {folder_ext}; 7z x {folder_out}archiv.7z', "Everything is Ok"), "test_x FAIL"
