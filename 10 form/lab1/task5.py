while True:
    try:
        a = float(input("Введіть значення a: "))
    except Exception:
        print("Значення може бути тільки числом")
        continue
    try:
        b = float(input("Введіть значення b: "))
    except Exception:
        print("Значення може бути тільки числом")
        continue
    avg = (a + b) / 2
    print(f"Середнє арефметичне двох чисел дорівнює {avg}")
    break
