while True:
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: нужно вводить только числа!")
        continue

    print("\nВыберите операцию:")
    print("1. + (сложение)")
    print("2. - (вычитание)")
    print("3. * (умножение)")
    print("4. / (деление)")
    print("0. Выход")

    c = input("Введите номер операции: ")

    if c == "1":
        print("Результат:", a + b)
    elif c == "2":
        print("Результат:", a - b)
    elif c == "3":
        print("Результат:", a * b)
    elif c == "4":
        if b == 0:
            print("Ошибка: делить на ноль нельзя!")
        else:
            print("Результат:", a / b)
    elif c == "0":
        print("Выход из программы. До свидания!")
        break
    else:
        print("Такой операции нет.")

    print("\n---\n")