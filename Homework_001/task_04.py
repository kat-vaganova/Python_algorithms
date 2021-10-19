# 4. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

letter_1 = input(f'введите букву: ')
letter_2 = input(f'введите еще одну букву: ')
pl_letter_1 = ord(letter_1) - 96
pl_letter_2 = ord(letter_2) - 96
distance = abs((ord(letter_2) - 96) - (ord(letter_1) - 96))

print(f'Буква {letter_1} в алфавите стоит на месте {pl_letter_1}')
print(f'Буква {letter_2} в алфавите стоит на месте {pl_letter_2}')
print(f'Между ними находится {distance} букв(а/ы)')


# решение со списком
# letters = input(f'введите через пробел две буквы : ')
# letters = letters.lower()
# letters = list(letters)
#
# print(f'Буква {letters[0]} в алфавите стоит на месте {ord(letters[0]) - 96}')
# print(f'Буква {letters[2]} в алфавите стоит на месте {ord(letters[2]) - 96}')
# print(f'Между ними находится {abs((ord(letters[2]) - 96) - (ord(letters[0]) - 96))} букв(а/ы)')




