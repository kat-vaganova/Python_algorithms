# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.


from random import randint

levels = 10
random_number = randint(1, 100)
print(random_number)

number_user = None
while number_user != random_number:
    print(f'You have left {levels} attempts')
    number_user = int(input('Guess the number: '))
    if number_user < random_number:
        print("The entered number more thought")
    elif number_user > random_number:
        print("The entered number less thought")
    else:
        print("Congratulation on your victory!")

    levels -= 1
    if levels == 0:
        print('Number of attempts ended!')
        break
