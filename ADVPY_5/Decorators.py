# Задание 1

import os, datetime


def logger_1(old_function):

    def new_function(*args, **kwargs):
        result_old = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='cp1251') as f:
            f.write(f'\nДата вызова функции: {datetime.datetime.now()}')
            f.write(f'\nИмя функции: {old_function.__name__}\n')
            f.write(f'\nАргументы: {args} / {kwargs}')
            f.write(f'\nВозвращаемое значение функции: {result_old}')

            return result_old

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger_1
    def hello_world():
        return 'Hello World'

    @logger_1
    def summator(a, b=0):
        return a + b

    @logger_1
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()



# Задание 2


def logger_2(path):
    def __logger2(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='cp1251') as f:
                f.write(f'\nДата вызова функции: {datetime.datetime.now()}')
                f.write(f'\nИмя функции: {old_function.__name__}\n')
                f.write(f'\nАргументы: {args} / {kwargs}')
                f.write(f'\nВозвращаемое значение функции: {result}')

            return result

        return new_function

    return __logger2


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger_2(path)
        def hello_world():
            return 'Hello World'

        @logger_2(path)
        def summator(a, b=0):
            return a + b

        @logger_2(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()

