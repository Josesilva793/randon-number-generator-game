import os
import random

# FUNCTION TO CLEAR THE TERMINAL
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

# BASICS INPUNTS TO START PLAYING THE GAME
lives = int(input("Number of lives: "))
max_score = int(input("Max score to win: "))
score = 0

# FUNCTION PLAY GAME TO START PLAYING THE GAME AND KEEP PLAYING UNTIL YOU WIN OR LOSE THE GAME
def play_game():
    while True:
        ran = random.randint(0, 9)
        player = int(input("Enter a number from 0 to 9: "))
        print("Your random number is:", ran)

        if ran == player:
            global score
            score += 1
            print("Your score is:", score)

            if score >= max_score:
                print("You won!")
                break
        else:
            global lives
            lives -= 1
            print("You have", lives, "lives left.")

            if lives < 0:
                print("Game over! You lost.")
                break

play_game()
