FIB_1 = FIB_2 = 1

n = int(input('Введите число для преобразования - '))



for i in range(2, n):
    FIB_1, FIB_2 = FIB_2, FIB_1 + FIB_2
    print(f'след. число фибониччи - {FIB_2}')
