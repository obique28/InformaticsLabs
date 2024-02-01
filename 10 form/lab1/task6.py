import math

while True:
    try:
        a = float(input("Введіть перше число: "))
    except Exception:
        print("Значення може бути тільки додатнім числом")
        continue
    try:
        b = float(input("Введіть друге число: "))
    except Exception:
        print("Значення може бути тільки додатнім числом")
        continue
    if a <= 0:
        print("Значення має бути більше нуля")
        continue
    if b <= 0:
        print("Значення має бути більше нуля")
        continue
    sum = a + b
    diff = math.fabs(a - b)
    mult = a * b
    div_fraction = (max(a, b) ** 2) % (min(a, b) ** 2)
    print(f"Сума {sum}")
    print(f"Різниця {diff}")
    print(f"Добуток {mult}")
    print(f"Частка ділення квадратів {div_fraction}")
    break
