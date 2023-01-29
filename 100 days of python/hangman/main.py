import random
import pyfiglet

print(pyfiglet.figlet_format(" _ _ a _ _ w"))

word_list = ["Hans", "wurst", "Kuh"]
chosen_word=random.choice(word_list)
lifes = 6

lineword=["_" for x in chosen_word]

while lifes>0:
    print(lineword)
    guess = input("What's your guess?\n").lower()
    right= guess in chosen_word
    if right:
        print("nice!")

        index = 0       
        while index>0:
            index = chosen_word.index(guess)
            lineword[index] = guess

    else:
        lifes-=1
        print(f"Nope! Lifes left: {lifes}")