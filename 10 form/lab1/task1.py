while True:
    try:
        a = float(input("Введіть сторону квадрата: "))
    except Exception:
        print("Значення може бути тільки додатнім числом")
        continue
    if a <= 0:
        print("Довжина сторони квадрата має бути більше нуля")
        continue
    p = a * 4
    print(f"Периметр квадрата дорівнює {p}")
    break
