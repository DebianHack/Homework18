import random


def game():
    choices = ['Камень', 'Ножницы', 'Бумага']
    player_choice = input("Выберите Камень, Ножницы или Бумага: ").capitalize()
    computer_choice = random.choice(choices)

    print(f"Игрок выбрал: {player_choice}")
    print(f"Компьютер выбрал: {computer_choice}")

    if player_choice == computer_choice:
        print("Ничья!")
    elif (player_choice == 'Камень' and computer_choice == 'Ножницы') or \
            (player_choice == 'Ножницы' and computer_choice == 'Бумага') or \
            (player_choice == 'Бумага' and computer_choice == 'Камень'):
        print("Игрок победил!")
    else:
        print("Компьютер победил!")


while True:
    game()
    play_again = input("Хотите сыграть еще раз? (Да/Нет): ").capitalize()
    if play_again != 'Да':
        break




