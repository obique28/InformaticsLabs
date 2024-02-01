import math

while True:
    try:
        a = float(input("Введіть довжину першого катета: "))
    except Exception:
        print("Значення може бути тільки додатнім числом")
        continue
    try:
        b = float(input("Введіть довжину другого катета: "))
    except Exception:
        print("Значення може бути тільки додатнім числом")
        continue
    if a <= 0:
        print("Значення має бути більше нуля")
        continue
    if b <= 0:
        print("Значення має бути більше нуля")
        continue
    c = math.sqrt(a ** 2 + b ** 2)
    p = a + b + c
    print(f"Довжина гіпотенузи дорівнює {c}")
    print(f"Периметр трикутника дорівнює {p}")
    break
