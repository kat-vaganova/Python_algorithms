# 5. Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.

letter = int(input('Enter number of letter (from 1 to 26): '))
print(f'Your letter is: {chr(letter + 96)}')
