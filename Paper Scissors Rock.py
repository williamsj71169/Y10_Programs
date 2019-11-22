
import random


# functions go here
def rps_checker():
    error = "Please choose rock, paper or scissor (r / p / s) "

    valid = False
    while not valid:

        # asks question and puts answer in lowercase
        response = input("Rock / Paper / Scissors: ").lower()
        print()

        if response == "rock" or response == "r":
            return "Rock"
        elif response == "paper" or response == "p":
            return "Paper"
        elif response == "scissors" or response == "s":
            return "Scissors"

        else:
            print(error)
            print()


def num_check(question, low, high):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if response < low or response > high:
                print("\nYour response is not valid, please try again")
                print()

            else:
                valid = True
                return response
        except ValueError:
            print()
            print("You did not enter an Integer. Please try again")
            print()


# Main routine goes here

play_again = ""
while play_again == "":

    computer_score = 0
    score = 0

    num_rounds = num_check("How many rounds would you like? (MAX 5)", 1, 5,)
    print()

    for item in range(1, num_rounds + 1):
        print()
        print("Round {}".format(item))
        print()

        WORDS = ("Paper", "Scissors", "Rock")
        word = random.choice(WORDS)
        correct = word
        print(word)

        chosen_item = rps_checker()
        print(chosen_item)

    #  checking chosen_item against word

        if chosen_item == word:
            print("Computer chose {}. TIE!". format(word))
            num_rounds -= 1

        elif word == "Rock" and chosen_item == "Paper":
            print("Computer chose Rock. Paper covers Rock. You win!")
            score += 1
            num_rounds -= 1

        elif word == "Paper" and chosen_item == "Scissors":
            print("Computer chose Paper. Scissors cuts Paper. You win!")
            score += 1
            num_rounds -= 1

        elif word == "Scissors" and chosen_item == "Rock":
            print("Computer chose Scissors. Rock breaks Scissors. You win!")
            score += 1
            num_rounds -= 1

        elif word == "Paper" and chosen_item == "Rock":
            print("Computer chose Paper. Paper covers Rock. You lose!")
            computer_score += 1
            num_rounds -= 1

        elif word == "Scissors" and chosen_item == "Paper":
            print("Computer chose Scissors. Scissors cuts Paper. You lose!")
            computer_score = 1
            num_rounds -= 1

        elif word == "Rock" and chosen_item == "Scissors":
            print("Computer chose Rock. Rock breaks Scissors. You lose!")
            computer_score += 1
            num_rounds -= 1

        else:
            print("lol, you did something wrong ")

    print(score)
    print(computer_score)

    print()

    play_again = (input("Push <enter> to play again or any other key to quit"))

    print()
