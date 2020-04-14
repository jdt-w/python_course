# Задание 12: Знакомство с условиями (bool, if, elif, else) Часть 2

#### Содержание:

+ [Теоретические материалы](#)
+ [Задание](#)
+ [Дополнительные материалы](#)
+ [При возникновении проблем](#Issues)

#### <a name=""></a> 1. Теоретические материалы



#### <a name=""></a> 2. Задание

Создайте переменную `number_1`, присвойте ей значение равное `903`  

Создайте условную инструкцию: 

```
if условие(я):
    блок инструкций, если условие(я) было(и) соблюдено(ы)
```

* в качестве *условия(ий)* условной инструкции используйте следующий код: `number_1 > 0 and number_1 * 3 <= 1500 and number_1 - 3 != 800`
* в качестве *блока инструкций условной инструкции, если условие(я) было(и) соблюдено(ы)*, используйте следующий код: `print('''Будет выполнено только в случае, если (число number_1 больше нуля) И (число number_1 * 3 меньше ИЛИ равно 1500) И (число number_1 - 3 не равно 800)''')`

```python
# Образец кода: 
if number_1 > 0 and number_1 * 3 <= 1500 and number_1 - 3 != 800:
    print('''Будет выполнено только в случае,
     если (число number_1 больше нуля) И (число number_1 * 3 меньше ИЛИ равно 1500) И
     (число number_1 - 3 не равно 800)
    ''')
```

Создайте условную инструкцию: 

```
if условие(я):
    блок инструкций, если условие(я) было(и) соблюдено(ы)
else:
    блок инструкций, если условие(я) не было(и) соблюдено(ы)
```

* в качестве *условия(ий)* условной инструкции используйте следующие утверждения: 
    * значение переменной `number_1` должно быть **равно** числу `404` **И** значение переменной `number_1` должно быть **меньше** числа `500` **И** значение переменной `number_1` должно быть **не**(**больше или равно** числа `2900`) 
* в качестве *блока инструкций условной инструкции, если условие(я) было(и) соблюдено(ы)*, используйте следующий код: `print('''Будет выполнено только в случае, если (число number_1 равно 404) И (число number_1 меньше 500) И (НЕ(число number_1 больше ИЛИ равно 2900))''')`
* в качестве *блока инструкций условной инструкции, если условие(я) не было(и) соблюдено(ы)*, используйте следующий код: `print(':c')`

Например:

```python
# Образец кода: 
if number_1 == 404 and number_1 < 500 and not(number_1 >= 2900):
    print('''Будет выполнено только в случае,
     если (число number_1 равно 404) И (число number_1 меньше 500) И (НЕ
     (число number_1 больше ИЛИ равно 2900))
    ''')
else: 
    print(':c')
```

Создайте условную инструкцию: 

```
if условие(я):
    блок инструкций, если условие(я) было(и) соблюдено(ы)
```

* в качестве *условия(ий)* условной инструкции используйте следующий код: `number_1 > -1 or number_1 + 40 > 30`
* в качестве *блока инструкций условной инструкции, если условие(я) было(и) соблюдено(ы)*, используйте следующий код: `print('Будет выполнено если (number_1 больше -1) ИЛИ (number_1 + 40 больше 30)')`

```python
# Образец кода: 
if number_1 > -1 or number_1 + 40 > 30:
    print('Будет выполнено если (number_1 больше -1) ИЛИ (number_1 + 40 больше 30)')
```

Создайте условную инструкцию: 

```
if условие(я):
    блок инструкций, если условие(я) было(и) соблюдено(ы)
else:
    блок инструкций, если условие(я) не было(и) соблюдено(ы)
```

* в качестве *условия(ий)* условной инструкции используйте следующие утверждения: 
    * значение переменной `number_1` должно быть **больше** числа `0` **ИЛИ** значение переменной `number_1` должно быть **не равно** числу `300` **ИЛИ** значение переменной `number_1` должно быть **не**(**равно** числу `400`) 
* в качестве *блока инструкций условной инструкции, если условие(я) было(и) соблюдено(ы)*, используйте следующий код: `print('Будет выполнено если (number_1 больше 0) ИЛИ (number_1 не равно 300) ИЛИ (НЕ(number_1 равно 400))')`
* в качестве *блока инструкций условной инструкции, если условие(я) не было(и) соблюдено(ы)*, используйте следующий код: `print(':c')`

Например:

```python
# Образец кода: 
if number_1 > 0 or number_1 != 300 or not(number_1 == 400):
    print('Будет выполнено если (number_1 больше 0) ИЛИ (number_1 не равно 300) ИЛИ (НЕ(number_1 равно 400))')
else:
    print(':c')
```

Создайте переменную `number_2`, присвойте ей значение равное `60`

Создайте многоуровневую условную инструкцию: 

```
if условие(я):
    блок инструкций (в том числе и вложенные if ... else), если условие(я) было(и) соблюдено(ы)
else:
    блок инструкций (в том числе и вложенные if ... else), если условие(я) не было(и) соблюдено(ы)
```

* в качестве *условия(ий)* условной инструкции используйте следующий код: `number_2 > 0`
* в качестве *блока инструкций (в том числе и вложенные if ... else) условной инструкции, если условие(я) было(и) соблюдено(ы)*, используйте *вложенную условную конструкцию if ... else*:
    * в качестве *условия(ий)* условной инструкции используйте следующий код: `number_2 * 3 <= 1500`
    * в качестве *блока инструкций (в том числе и вложенные if ... else) вложенной условной инструкции, если условие(я) было(и) соблюдено(ы)*, используйте следующий код: `print('Число number_2 больше 0 И number_2 * 3 меньше ИЛИ равно 1500')`
    * в качестве *блока инструкций (в том числе и вложенные if ... else) вложенной условной инструкции, если условие(я) не было(и) соблюдено(ы)*, используйте следующий код: `print('Число number_2 больше 0, НО number_2 * 3 НЕ МЕНЬШЕ 1500 ИЛИ НЕ РАВЕН 1500')`  
* в качестве *блока инструкций (в том числе и вложенные if ... else) условной инструкции, если условие(я) не было(и) соблюдено(ы)*, используйте следующий код: `print('Число number_2 не больше 0')`

```python
# Образец кода: 
if number_2 > 0:
    if number_2 * 3 <= 1500:
        print('Число number_2 больше 0 И number_2 * 3 меньше ИЛИ равно 1500')
    else:
        print('Число number_2 больше 0, НО number_2 * 3 НЕ МЕНЬШЕ 1500 ИЛИ НЕ РАВЕН 1500')
else:
    print('Число number_2 не больше 0')
```

Создайте многоуровневую условную инструкцию: 

```
if условие(я):
    блок инструкций (в том числе и вложенные if ... else), если условие(я) было(и) соблюдено(ы)
else:
    блок инструкций (в том числе и вложенные if ... else), если условие(я) не было(и) соблюдено(ы)
```

* в качестве *условия(ий)* условной инструкции используйте следующие утверждения: 
    * значение переменной `number_2` должно быть **не равно** числу `30` **И** значение переменной `number_2` должно быть **больше** числу `1` **ИЛИ** значение переменной `number_2` должно быть **равно** значению переменной `number_2` 
* в качестве *блока инструкций (в том числе и вложенные if ... else) условной инструкции, если условие(я) было(и) соблюдено(ы)*, используйте следующий код: `print('(number_2 не равно 30) И (number_2 больше 1) ИЛИ (number_2 равно number_2')`
* в качестве *блока инструкций (в том числе и вложенные if ... else) условной инструкции, если условие(я) не было(и) соблюдено(ы)*, используйте *вложенную условную конструкцию if ... else*:
    * в качестве *условия(ий)* условной инструкции используйте следующие утверждения:
        * значение переменной `number_2` должно быть **равно** значению переменной `number_1` **ИЛИ** значение переменной `number_1` умноженной на `5` должно быть **меньше** числа `-30` 
    * в качестве *блока инструкций (в том числе и вложенные if ... else) вложенной условной инструкции, если условие(я) было(и) соблюдено(ы)*, используйте следующий код: `print('В случае если перечисленные выше условия не были соблюдены, НО (number_2 равно number_1) ИЛИ (number_1 * 5 меньше -30)')`
    * в качестве *блока инструкций (в том числе и вложенные if ... else) вложенной условной инструкции, если условие(я) не было(и) соблюдено(ы)*, используйте следующий код: `print('В случае если НИ ОДНО из перечисленных выше условий не было соблюдено')`  

Например:

```python
# Образец кода: 
if number_2 != 30 and number_2 > 1 or number_2 == number_2:
    print('(number_2 не равно 30) И (number_2 больше 1) ИЛИ (number_2 равно number_2')
else:
    if number_2 == number_1 or number_1 * 5 < -30:
        print('В случае если перечисленные выше условия не были соблюдены, НО (number_2 равно number_1) ИЛИ (number_1 * 5 меньше -30)')
    else:
        print('В случае если НИ ОДНО из перечисленных выше условий не было соблюдено')
```

* Образец решённого задания находится в папке `welpodron` - файл `welpodron.py`

#### <a name=""></a> 3. Дополнительные материалы



#### <a name="Issues"></a> Есть вопрос?

Свяжитесь с автором проекта: [welpodron](https://vk.com/welpodron)

> @welpodron 2020