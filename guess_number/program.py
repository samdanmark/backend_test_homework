from random import randint

number = randint(1, 100)
print('Угадайте число')

while True:
    guess = int(input('Введите число: '))
    if guess < number:
        print('Загаданное число больше')
    elif guess > number:
        print('Загаданное число меньше')
    else:
        print('Вы угадали число!')
        break