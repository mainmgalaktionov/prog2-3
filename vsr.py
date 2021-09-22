
values = ((0, 0), (0, 1), (1, 0), (1, 1))


def head():

    head = '| A | B | F |'
    under_head = '+ ' + '-' * (len(head) - 4) + ' +'
    print(under_head)
    print(head)
    print(under_head)


def logical_operation_four(val):
    """Строит строки для таблицы истинности четвертого выражения"""
    result = (val[0] or val[1]) and (not val[0] or not val[1])
    result = int(result)
    line = '| ' + str(val[0]) + ' | ' + str(val[1]) + ' | ' + str(result) + ' |'
    print(line)
    print('+', '-' * (len(line)-4), '+')


def logical_operation_one(val):
    """Строит строки для таблицы истинности 'штриха Шеффера'"""
    result = not(val[0] and val[1])
    result = int(result)
    line = '| ' + str(val[0]) + ' | ' + str(val[1]) + ' | ' + str(result) + ' |'
    print(line)
    print('+', '-' * (len(line)-4), '+')


def logical_operation_twenty_two(val):
    """Строит строки для таблицы истинности двадцать второго выражения"""
    result = not(not(val[0] and val[1]) or (val[0] == val[1])) or not(val[0])
    result = int(result)
    line = '| ' + str(val[0]) + ' | ' + str(val[1]) + ' | ' + str(result) + ' |'
    print(line)
    print('+', '-' * (len(line)-4), '+')


"""Вывод первой таблицы"""
print('\n4) F = (A∨B)∧(¬A∨¬B)\n')
head()
for i in range(len(values)):
    logical_operation_four(values[i])
"""Вывод второй таблицы"""
print('\n1) F = ¬(A∧B)\n')
head()
for i in range(len(values)):
    logical_operation_one(values[i])
"""Вывод третьей таблицы"""
print('\n22) F = ¬(¬(A∧B)∨A↔B)∨¬A\n')
head()
for i in range(len(values)):
    logical_operation_twenty_two(values[i])