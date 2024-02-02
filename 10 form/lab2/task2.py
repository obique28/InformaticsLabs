number = int(input("Введіть шестизначне число: "))
a1 = (number // 100000) % 10
a2 = (number // 10000) % 10
a3 = (number // 1000) % 10
a4 = (number // 100) % 10
a5 = (number // 10) % 10
a6 = number % 10
result = a6 * 100000 + a5 * 10000 + a4 * 1000 + a3 * 100 + a2 * 10 + a1
print(f"Результат: {result}")
