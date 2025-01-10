from functools import wraps


def log(predicate, error_message, filename: str = ""):
    """Декоратор log принимает функцию предикат, сообщение об ошибке и
    путь к файлу. Функция предикат может проверять выходные данные функции.
    В случае ошибки выводится сообщение error_message.
    Декоратор отмечает начало работы функции, выводит результат и
    сообщает об окончание работы"""
    def my_decorators_error(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if not predicate(*args, **kwargs):
                with open(filename, "a+") as file:
                    file.write(f"{function}\nError:{error_message}\nInputs: {args}, {str(kwargs)}\n")
                raise ValueError(error_message)
            elif filename != "":
                result = function(*args, **kwargs)
                with open(filename, "a+") as file:
                    file.write(f"{function} ok\n")
            else:
                print("Getting started with the " + f"{function}"[1:-23])
                result = function(*args, **kwargs)
                print("Shutting down the function")
            return result
        return wrapper
    return my_decorators_error


def predicate_is_filter(arg, arg2):
    return arg, arg2 == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def predicate_is_sort(arg, arg2: bool = True):
    return arg, arg2 == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
