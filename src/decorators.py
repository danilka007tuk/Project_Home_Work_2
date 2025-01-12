from functools import wraps


def log(filename=None):
    def my_decorators_error(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{function.__name__}: inputs: {args}, kwargs: {kwargs}\n")
                else:
                    print(f"Запуск функции {function.__name__}, Inputs: {args}, kwargs: {kwargs}")

                result = function(*args, **kwargs)

                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{function.__name__} ok: {result}\n")
                else:
                    print(f"Результат: {result}")
                    print(f"Функция {function.__name__} успешно выполнена.")

                return result

            except Exception as e:
                error_message = f"Ошибка в функции {function.__name__}: {e}"
                if filename:
                    with open(filename, "a") as file:
                        file.write(error_message + "\n")
                else:
                    print(error_message)
                raise
            return result

        return wrapper

    return my_decorators_error


@log()
def my_function(x, y):
    return x + y


@log()
def error_function(x, y):
    raise ValueError("error")


my_function(1, 3)
