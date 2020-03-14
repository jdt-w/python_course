spisok_1 = [[28, 70, 36], ['Строка 1', "Строка 2"]]

print(spisok_1[0], spisok_1[1])

number_1 = 8
spisok_2 = spisok_1[0]
spisok_3 = spisok_1[number_1 - 7]
 
print(spisok_2, spisok_3)

number_2 = spisok_1[0][2] # 36
number_3 = spisok_2[2] # 36
number_4 = spisok_1[0][0] + spisok_1[0][1] # 98

stroka_1 = spisok_1[1][0] # Строка 1

print(number_2, number_3, number_4, stroka_1)