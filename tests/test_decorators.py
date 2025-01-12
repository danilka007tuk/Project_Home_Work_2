from src.decorators import error_function, my_function


def test_my_function(capsys):
    my_function(1, 3)
    captured = capsys.readouterr()
    assert captured.out == (
        "Запуск функции my_function, Inputs: (1, 3), kwargs: {}\n"
        "Результат: 4\n"
        "Функция my_function успешно выполнена.\n"
    )


def test_error_function(capsys):
    try:
        error_function(1, 3)
    except ValueError:
        pass
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Запуск функции error_function, Inputs: (1, 3), kwargs: {}\nОшибка в функции error_function: error\n"
    )
