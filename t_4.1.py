#Задача 1
squares = [x ** 2 for x in range(1, 11)]
print(f"Квадраты первых 10 натуральных чисел: {squares}")

#Задача 2
names = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
week = {names[i]: i + 1 for i in range(len(names))}
print(f"Дни недели: {week}")

#Задача 3
tags = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
lower_tags = set([tags[i].lower() for i in range(len(tags))])
print(f"Теги библиотек в нижнем регистре: {lower_tags}")

#Задача 4
nums = [1, 3, 4, 87, 98, 15, 7, 4]
evens = [nums[i] for i in range(len(nums)) if nums[i] % 2 == 0]
print(f"Чётные числа: {evens}")

#Задача 5
def factorial(num: int) -> int:
    if isinstance(num, int) and num >= 0:
        res = 1
        for m in range(2, num + 1):
            res *= m
        return res
    else:
        raise ValueError("Недопустимое значение для возведения в факториал!")
facts = {i: factorial(i) for i in range(1, 6)}
print(f"Факториалы чисел: {facts}")
