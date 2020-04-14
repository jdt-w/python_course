string_1 = 'Эта строка будет передана в функцию print() как аргумент'

print(string_1)

string_2 = 'Передадим функции print() ещё один аргумент'

print(string_1, string_2)

list_1 = [30, 40]
dict_1 = {
    10: list_1,
    '10': list_1,
    "20": list_1
}

def function_1(func_argument_1):
    print(func_argument_1)

function_1(dict_1)

def function_2(func_argument_1, func_argument_2):
    func_argument_1 = 90
    func_argument_2 = '800'
    print(func_argument_1, func_argument_2)
    return func_argument_1

print(list_1, dict_1)

function_2(list_1, dict_1)

print(list_1, dict_1)

list_1 = function_2(list_1, dict_1)

print(list_1)