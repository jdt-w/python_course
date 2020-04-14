string_1 = 'Я хочу быть второй строкой'
string_2 = 'Я хочу быть первой строкой'

print('Обязательные аргументы требуют определённого порядка: ',string_1, string_2)

print('Для нашей цели мы изменили порядок передаваемых аргументов, но это не всегда эффективно ',string_2, string_1)

string_3 = 'Я хочу быть третьей строкой'

def function_1(func_argument_1, func_argument_2, func_argument_3):
    print(func_argument_1, func_argument_2, func_argument_3)

function_1(func_argument_1 = string_2, func_argument_2 = string_1, func_argument_3 = string_3)

def function_2(func_argument_1, func_argument_2 = 'Я значение аргумента по-умолчанию'):
    print(func_argument_1, func_argument_2)

function_2(func_argument_1=string_2)
function_2(string_2, func_argument_2=string_1)
function_2(string_3, string_2)