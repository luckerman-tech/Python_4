def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@decorator
def calculate_area(length, width) -> str:
    return f"Площадь прямоугольника: {length * width}"

while True:
    try:
        userlength = float(input("Введите длину прямоугольника: "))
        userwidth = float(input("Введите ширину прямоугольника: "))
    except:
        print("Недопустимое значение длины или ширины!")
    else:
        if userlength <= 0 or userwidth <= 0:
            print("Недопустимое значение длины или ширины!")
        else:
            if userlength == round(userlength):
                userlength = int(userlength)
            if userwidth == round(userwidth):
                userwidth = int(userwidth)
            print(calculate_area(userlength, userwidth))
            break