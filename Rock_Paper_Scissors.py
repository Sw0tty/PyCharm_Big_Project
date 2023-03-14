import random
import time
computer_wins = 0
player_wins = 0
tools = ("r", "s", "p")
while computer_wins < 3 and player_wins < 3:
    player_choice = None
    while player_choice not in tools:
        player_choice = input("Чем сходите? (r-камень, s-ножницы, p-бумага)")
    computer_choice = random.choice(("r", "s", "p"))
    if computer_choice == "s":
        print("Компьютер выбрал ножницы")
    elif computer_choice == "r":
        print("Компьютер выбрал камень")
    else:
        print("Компьютер выбрал бумагу")
    if computer_choice == "r" and player_choice == "s"\
            or computer_choice == "s" and player_choice == "p"\
            or computer_choice == "p" and player_choice == "r":
        computer_wins += 1
        print("Очко компьютеру")
    elif computer_choice == "s" and player_choice == "r"\
            or computer_choice == "p" and player_choice == "s"\
            or computer_choice == "r" and player_choice == "p":
        player_wins += 1
        print("Эта партия за вами")
    else:
        print("Ничья")
    print()
print("---Игра окончена---")
if computer_wins > player_wins:
    print("На этот раз победил компьютер")
else:
    print("Поздравляем, вы выиграли")
time.sleep(3)
