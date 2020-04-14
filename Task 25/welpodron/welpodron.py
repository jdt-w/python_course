class Animal_1:
    def __init__(self, name, type_of_animal = 'Кот'):
        print('Был вызван конструктор класса Animal_1')
        self.name = name
        self.type_of_animal = type_of_animal
        print(
            'Посмотрим на мои атрибуты:',
            '\nself.name: ', self.name,
            '\nself.type_of_animal: ', self.type_of_animal 
            )

cat_1 = Animal_1('Барсик')
dog_1 = Animal_1('Боня', 'Собака')

print(cat_1.type_of_animal, dog_1.type_of_animal)

string_1 = cat_1.name

if string_1 == 'Барсик':
    print('Строки совпадают!')

class Animal_2:
    static_class_attribute_1 = 'Кот'
    static_class_attribute_2 = 'Собака'
    
print(Animal_2.static_class_attribute_1)
print(Animal_2.static_class_attribute_2)

cat_3 = Animal_2()

class Animal_4:
    def __init__(self, color, type_of_animal):
        print('Был вызван конструктор класса Animal_4')
        self.__dynamic_private_class_attribute_1 = color
        print('Теперь атрибут __private_class_attribute_1 "приватен"')
        self.dynamic_not_private_class_attribute_1 = type_of_animal

cat_2 = Animal_4(color = 'Серый', type_of_animal = 'Кот')

print(cat_2.dynamic_not_private_class_attribute_1)

#следующие строки кода вызовут ошибку
'''
print(cat_2.__dynamic_private_class_attribute_1)
print(cat_2.dynamic_private_class_attribute_1)
'''
