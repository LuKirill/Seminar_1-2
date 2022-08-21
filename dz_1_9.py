#7 Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

x = 1
y = 0
z = 1
if -(x or y or z) == -x and -y and -z:
    print(True)
else:
    print(False)