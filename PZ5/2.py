"""
Описать функцию AddLeftDigit(D, K), добавляющую к целому положительному
числу K слева цифру D (D — входной параметр целого типа, лежащий в диапазоне
1-9, K — параметр целого типа, являющийся одновременно входным и выходным).
С помощью этой функции последовательно добавить к данному числу K слева
данные цифры D1 и D2, выводя результат каждого добавления.
"""
def AddLeftDigit(D, K):
    return int(str(D) + str(K))

try:
    D = int(input("Введите цифру: "))
    if (D <= 0) or (D >= 10):
        print("Ошибка ввода")
        exit()
    else:
        K = int(input("Введите число: "))
        print(AddLeftDigit(D, K))

except ValueError:
    print("Ошибка ввода")

    