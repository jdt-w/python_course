class Animal_1:
    def __init__(self, func_argument_1, func_argument_2):
        print('Был вызван конструктор класса Animal_1')
        self.class_attribute_1 = func_argument_1
        self.class_attribute_2 = func_argument_2

name_1 = 'Барсик'
name_2 = 'Игорь'
color_1 = 'Рыжий'
color_2 = 'Белый'

cat_1 = Animal_1(func_argument_1 = name_1, func_argument_2 = color_1)
cat_2 = Animal_1(func_argument_1 = name_2, func_argument_2 = color_2)

class Animal_2:
    def __init__(self, name, color, type_of_animal = 'Кот'):
        print('Был вызван конструктор класса Animal_2')
        print(
            'Конструктору класса Animal_2 были переданы следующие аргументы:',
            '\nname: ', name,
            '\ncolor:', color,
            '\ntype_of_animal:', type_of_animal
        )
        self.name = name 
        self.color = color
        self.type_of_animal = type_of_animal

cat_3 = Animal_2('Боря', 'Чёрный')
dog_1 = Animal_2(name = 'Боня', color= 'Коричневый', type_of_animal = 'Собака')
dog_2 = Animal_2('Хома', 'Чёрный', 'Собака')
