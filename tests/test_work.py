import pytest
from checkout import checkout

folder_in = "/home/user/folder_in/"
folder_out = "/home/user/folder_out/"
folder_ext = "/home/user/folder_ext/"


def test_step1():
    assert checkout("cat /etc/os-release", "jammy"), "test1 FAIL"


@pytest.mark.run_this
def test_step2():
    assert checkout("cat /etc/os-release", "22.04.1"), "test2 FAIL"

def test_step3():
    assert checkout("cat /etc/os-release", "NAME"), "test3 FAIL"


# заархивировать папку
def test_7z_a():
    assert checkout(f'cd {folder_in}; 7z a {folder_out}archiv', "Everything is Ok"), "test_a FAIL"


# удалить папку/файл
def test_7z_d():
    assert checkout(f'cd {folder_out}; 7z d ./archiv.7z fail1.txt', "Everything is Ok"), "test_d FAIL"


# показать файлы в папке не запуская
def test_7z_l():
    assert checkout(f'cd {folder_out}; 7z l ./archiv.7z', "Listing archive: ./archiv.7z"), "test_l FAIL"


# разархивировать файлы из папки
def test_7z_x():
    assert checkout(f'cd {folder_ext}; 7z x {folder_out}archiv.7z', "Everything is Ok"), "test_x FAIL"

# запуск из терминала: pytest test_work.py
# или с ключом -v для более информативного вывода: pytest test_work.py -v
# если не работает: python3 -m pytest test_work.py -v
