while True:
    try:
        a = float(input("Введіть довжину прямокутника: "))
    except Exception:
        print("Значення може бути тільки додатнім числом")
        continue
    try:
        b = float(input("Введіть ширину прямокутника: "))
    except Exception:
        print("Значення може бути тільки додатнім числом")
        continue
    if a <= 0:
        print("Значення має бути більше нуля")
        continue
    if b <= 0:
        print("Значення має бути більше нуля")
        continue
    p = (a + b) * 2
    s = a * b
    print(f"Периметр прямокутника дорівнює {p}")
    print(f"Площа прямокутника дорівнює {s}")
    break
