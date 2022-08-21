#9 Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти
while True:
    num = int(input("Введите номер четверти прямоугольной системы координат: "))
    if num == 1:
        print("x > 0, y > 0")
        break
    elif num == 2:
        print("x < 0, y > 0")
        break
    elif num == 3:
        print("x < 0, y < 0")
        break
    elif num == 4:
        print("x > 0, y > 0")
        break
    else:
        print("Введите число от 1 до 4")