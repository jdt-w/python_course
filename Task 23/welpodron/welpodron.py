number_1 = 0
string_1 = ''
list_1 = []
dict_1 = {}

print(type(number_1), type(string_1), type(list_1), type(dict_1))

class Animal:
    def __init__(self):
        print('Был вызван конструктор класса Animal')

cat_1 = Animal()

print(type(cat_1))
print(cat_1)