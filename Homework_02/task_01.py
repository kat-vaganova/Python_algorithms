# 1. Написать программу, которая будет
# складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.


def calculate(a, b):
    if sing == '+':
        answer = a + b
    elif sing == '-':
        answer = a - b
    elif sing == '*':
        answer = a * b
    elif sing == '/':
        # if b != 0:
        answer = a / b
    return answer


while True:
    a = int(input('Enter 1 number '))
    b = int(input('Enter 2 number '))
    sing = input('Enter sing or 0 for break: ')
    if sing == '0':
        break
    if b == 0 and sing == '/':
        print("Mistake, Нou can't divide by zero.")

    else:

        while True:
            if sing == '+' or sing == '-' or sing == '*' or sing == '/':
                print(calculate(a, b))
                break
            else:
                print('Mistake, try again!')
                sing = input('Enter sing or 0 for break: ')
            if sing == '0':
                break

