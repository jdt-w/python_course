number_1 = 10
number_2 = 0

while number_1 > 0:
    print(number_1)
    number_1-=1
else:
    print('Цикл while был закончен')

while number_2 != 10 or number_2 + 1 == 10:
    if number_2 > 4:
        print('Цикл прошёл число 4, текущее число: ', number_2)
    if number_2 == 8:
        print('Цикл дошёл до 8, закончим цикл раньше чем предполагалось')
        break
    number_2+=1

