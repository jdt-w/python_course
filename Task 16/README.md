# Задание 16: Знакомство с циклами (for, while) Часть 3

#### Содержание:

+ [Теоретические материалы](#THEORETICAL_MATERIALS)
+ [Задание](#TASK)
+ [Дополнительные материалы](#ADDITIONAL_MATERIALS)
+ [При возникновении проблем](#ISSUES)

#### <a name="THEORETICAL_MATERIALS"></a> 1. Теоретические материалы



#### <a name="TASK"></a> 2. Задание

Создайте переменную `number_1`, присвойте ей значение равное `10`

Создайте переменную `number_2`, присвойте ей значение равное `0`

Создайте цикл `while`: 

```
while условие(я):
    блок инструкций
```

* в качестве *условия(ий)* цикла используйте следующие утверждения:
    * значение переменной `number_2` должно быть **не равно** числу `10` **ИЛИ** результат сложения значения переменной `number_2` и числа `1` должен быть **равен** числу `10`  
* в качестве *блока инструкций* цикла используйте *условные инструкции if ...* и операцию увеличения значения переменной `number_2` на `1`:
    * в качестве *условия(ий) первой условной инструкции* используйте следующие утверждения:
        * значение переменной `number_2` должно быть **больше** числа `4`  
    * в качестве *блока инструкций первой условной инструкции, если условие(я) было(и) соблюдено(ы)*, используйте следующий код:
        ```python
            print('Цикл прошёл число 4, текущее число: ', number_2)  
        ```
    * в качестве *условия(ий) второй условной инструкции* используйте следующие утверждения:
        * значение переменной `number_2` должно быть **равно** числу `8`
    * в качестве *блока инструкций второй условной инструкции, если условие(я) было(и) соблюдено(ы)*, используйте следующий код:
        ```python
            print('Цикл дошёл до 8, закончим цикл раньше чем предполагалось')
            break  
        ```
    * последней командой в *блоке инструкций* цикла используйте следующий код: `number_2+=1`

Например:

```python
# Образец кода: 
while number_2 != 10 or number_2 + 1 == 10:
    if number_2 > 4:
        print('Цикл прошёл число 4, текущее число: ', number_2)
    if number_2 == 8:
        print('Цикл дошёл до 8, закончим цикл раньше чем предполагалось')
        break
    number_2+=1  
```

Создайте цикл `while ... else`: 

```
while условие(я):
    блок инструкций
else:
    блок инструкций, который будет вызван один раз после исполнения цикла, НО ТОЛЬКО В СЛУЧАЕ, ЕСЛИ ЦИКЛ НЕ БЫЛ ПРЕРВАН ИНСТРУКЦИЕЙ break  
```

* в качестве *условия(ий)* цикла используйте следующие утверждения:
    * значение переменной `number_1` должно быть **больше** числа `0`
* в качестве *блока инструкций* цикла используйте следующий код:
    ```python
        print(number_1)
        number_1-=1
    ```
* в качестве *блока инструкций else* цикла используйте следующий код: `print('Цикл while был закончен')`

Например:

```python
# Образец кода: 
while number_1 > 0:
    print(number_1)
    number_1-=1
else:
    print('Цикл while был закончен')  
```

* Образец решённого задания находится в папке <a href="./welpodron">`welpodron`</a> - файл <a href="./welpodron/welpodron.py">`welpodron.py`</a>

#### <a name="ADDITIONAL_MATERIALS"></a> 3. Дополнительные материалы



#### <a name="ISSUES"></a> Есть вопрос?

Свяжитесь с автором проекта: [welpodron](https://vk.com/welpodron)

> @welpodron 2020