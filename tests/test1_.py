import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    assert checkout("cat /etc/os-release", "jammy"), "test1 FAIL"


def test_step2():
    assert checkout("cat /etc/os-release", "22.04.1"), "test2 FAIL"


def test_step3():
    assert checkout("cat /etc/os-release", "NAME"), "test3 FAIL"

# запуск из терминала: pytest test1_.py
# или с ключом -v для более информативного вывода: pytest test1_.py -v
# если не работает: python3 -m pytest test1_.py -v
