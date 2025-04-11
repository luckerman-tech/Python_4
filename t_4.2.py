def prime_nums(limit: int):
    for num in range(2, limit + 1):
        is_prime = True
        for divider in range(2, int(num ** 0.5) + 1):
            if num % divider == 0:
                is_prime = False
        if is_prime:
            yield num

try:
    end_num = int(input("Введите число, до которого включительно будут выведены простые числа: "))
except:
    raise ValueError("Должно быть введено целое число больше 1!")
else:
    if end_num < 2:
        raise ValueError("Должно быть введено целое число больше 1!")

print(f"Список простых чисел до {end_num} включительно:")
for number in prime_nums(end_num):
    print(number)