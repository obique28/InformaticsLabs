from math import pi

while True:
    try:
        r = float(input("Введіть радіус кола: "))
    except Exception:
        print("Значення може бути тільки додатнім числом")
        continue
    if r <= 0:
        print("Значення має бути більше нуля")
        continue
    l = 2 * r * pi
    s = (r ** 2) * pi
    print(f"Довжина кола дорівнює: {l}")
    print(f"Площа круга дорівнює: {s}")
    break
