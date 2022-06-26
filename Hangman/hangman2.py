import random
import time

list_words = ["quick", "brown", "fox", "great", "Mississippi"]
confirm = "y"
time_per_guess = 30
total_score = 0
scores = {0: 100, 1: 250, 2: 550, 3: 800, 4: 1200, 5: 1500}


def correct_answer():
    total_score += 1


def set_time():
    # set timer
    return time.time() + time_per_guess


def play_hangman():
    guessed_letters = []
    word = random.choice(list_words)

    word_blank = "_ "*len(word)
    print(word_blank)
    # create number of guess allowed

    print(f"You have {number_guess} guess")
    time_start = set_time()
    # while number_guess != 0 or end>time.time():
    limit_reached = False
    while time_start > time.time():
        if number_guess == 0:
            limit_reached = True
            break
        user_input = input().lower()

        # ALREADY GUESSED LETTER AND WORD
        if user_input in guessed_letters:
            print("Input already guessed.", end=" ")
        else:
            guessed_letters.append(user_input)

            # if guessing word
            if len(user_input) == len(word):
                if user_input == word:
                    print(f"You guessed it right! The word is '{word}'.")
                    number_guess = 0
                    total_score += 1
                    # end game na or try again
                else:
                    print("Incorrect guess")

            # GUESSING LETTER
            elif len(user_input) == 1:
                if user_input in word:
                    print(f"Letter {user_input} is correct.")

                    # position reveal guessed letter
                    position_lst = []
                    for pos, char in enumerate(word):
                        if(char == user_input):
                            position_lst.append(pos)

                    # loop for word_blank
                    for newpos in position_lst:
                        word_blank = word_blank[:2*newpos] + \
                            user_input + word_blank[2*newpos+1:]
                    print(word_blank)
                else:
                    print(f"Letter {user_input} is not in the word.")
                    number_guess -= 1
                    print("Guess left=", number_guess)
            elif len(user_input) < len(word):
                input("Insufficient letters.")
            else:
                input("TOO MUCH letters!!")
        if word_blank.replace(" ", "") == word:         # All letters are guessed
            print(f"The word is {word}")
            total_score += 1
            break
        if limit_reached == True:
            print("Guess limit reached")

    if time.time() > time_start:
        print("But 30 Seconds has passed.")
    confirm = input("Try again? Y/N").lower()


while confirm == "y":
    play_hangman()
print("Program Terminated")
number_guess = 10
