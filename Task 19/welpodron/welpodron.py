spisok_1 = [[28, 70, 36], ['Строка 1', "Строка 2"]]
number_1 = 13
number_2 = number_1 + 5
stroka_1 = 'Строчка'

slovarb_1 = {
    number_1: [
        spisok_1,
        30
    ],
    stroka_1: {
        number_2: [
            90,
            40,
            'Строка в списке'
        ],
        stroka_1: 'Строчка-строчечка'
    }
}

for klu4 in slovarb_1:
    if klu4 == number_1: 
        for element in slovarb_1[klu4]:
            if element == spisok_1:
                for element_v_spiske in element:
                    print(element_v_spiske)
            else:
                print(element)
    if klu4 == stroka_1:
        for element in slovarb_1[klu4]:
            if element == number_2:
                for element_v_spiske in slovarb_1[klu4][element]:
                    print(element_v_spiske)   
            else:
                print(slovarb_1[klu4][element])