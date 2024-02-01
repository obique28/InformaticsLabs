while True:
    try:
        a = float(input("Введіть довжину ребра куба: "))
    except Exception:
        print("Значення може бути тільки додатнім числом")
        continue
    if a <= 0:
        print("Значення має бути більше нуля")
        continue
    v = a ** 3
    s = (a ** 2) * 6
    print(f"Об'єм куба дорівнює: {v}")
    print(f"Площа поверхні куба дорівнює: {s}")
    break
