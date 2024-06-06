# n1 - число номер 1
# n2 - число номер 2
# op - операция между числами


def calculate(n1, n2, op):
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        result = n1 / n2
    elif op == '^':
        result = n1 ** n2
    else:
        result = None
    return result


num1 = float(input('Введите первое число: '))
op = input('Введите знак (+,-,*,/,^): ')
num2 = float(input('Введите второе число: '))
result = calculate(num1, num2, op)
print(num1, op, num2, '=', result)
