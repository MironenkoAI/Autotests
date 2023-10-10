from checkout import checkout
import yaml
import pytest

with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)


class TestWorkPositive:
    def test_step1(self):
        assert checkout("cat /etc/os-release", "jammy"), "test1 FAIL"

    def test_step2(self):
        assert checkout("cat /etc/os-release", "22.04.1"), "test2 FAIL"

    def test_step3(self):
        assert checkout("cat /etc/os-release", "NAME"), "test3 FAIL"

    # заархивировать папку
    def test_7z_a(self, make_folder, make_file):
        assert checkout(f'cd {data.get("folder_in")}; 7z a {data.get("folder_out")}archiv',
                        "Everything is Ok"), "test_a FAIL"

    # удалить папку/файл
    def test_7z_d(self, make_folder, make_file):
        assert checkout(f'cd {data.get("folder_out")}; 7z d ./archiv.7z file1.txt', "Everything is Ok"), "test_d FAIL"

    # показать файлы в папке не запуская

    # def test_7z_l(self, make_folder, make_file):
    #     assert checkout(f'cd {data.get("folder_out")}; 7z l ./archiv.7z', "Listing archive: ./archiv.7z"), "test_l FAIL"

    # разархивировать файлы из папки
    # def test_7z_x(self):
    #     assert checkout(f'cd {data.get("folder_ext")}; 7z x {data.get("folder_out")}archiv.7z', "Everything is Ok"), "test_x FAIL"


# запуск из терминала: pytest test_work.py
# или с ключом -v для более информативного вывода: pytest test_work.py -v
# если не работает: python3 -m pytest test_work.py -v

if __name__ == '__main__':
    pytest.main(["-vv"])
