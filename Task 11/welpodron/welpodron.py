istina = True 
ne_pravda = False 

print(istina, type(istina), ne_pravda, type(ne_pravda))

if istina == True:
    print('Это истина!')

if True:
    print('Это тоже истина!')

if istina:
    print('Это ещё одна истина!')

number_1 = 54 

if number_1 == number_1:
    print('Значение переменной number_1 действительно равняется самому себе')

if number_1 > 0:
    print('Значение переменной number_1 больше нуля')

if number_1 < 90:
    print('Значение переменной number_1 меньше 90')

if number_1 + 1 != 0:
    print('Число (number_1 + 1) не равно нулю')

if number_1 >= number_1:
    print('Значение переменной number_1 не больше себя самого, но равно себе')

if number_1 <= number_1:
    print('Значение переменной number_1 не меньше себя самого, но равно себе')

if number_1 * 0 == 54:
    print('Будет забавно, если это будет выведено в консоль')
else:
    print('Сработал данный вывод, так как предыдущий оказался НЕ ИСТИННЫМ')