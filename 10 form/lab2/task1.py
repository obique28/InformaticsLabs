number=int(input("Введіть тризначне число: "))
number_str=str(number)
a1= number // 100
a2= (number % 100) // 10
a3= number % 10
result1= a2 * 100 + a1 * 10 + a3
result2= a3 * 100 + a2 * 10 + a1
result3= a1 * 100 + a3 * 10 + a2
print(f"Результат 1: {result1}")
print(f"Результат 2: {result2}")
print(f"Результат 3: {result3}")