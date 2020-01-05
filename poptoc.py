# This file contains code that runs the game "PopToc"

# First we need to get a users to select a number
# Then we need to define a function that houses the game code

def poptoc_func():
    user_input_play = input("Welcome! Would you like to play a game of POPTOC ? ")

    # By adding a total score initial value of 0, outside of the while loop, we can keep count of the total score
    total_score = 0
    while user_input_play != "no":
        score = 0
        user_input = int(input("What number would you like to play with? "))

        if user_input % 5 == 0 and user_input % 3 == 0:
            score += user_input
            print("POPTOC!?!")
            print(f"Congratulations! Your score is now {score}!")

        elif user_input % 5 == 0:
            score += user_input
            print("POP!?!")
            print(f"Congratulations! Your score is now {score}!")

        elif user_input % 3 == 0:
            score += user_input
            print("TOC!?!")
            print(f"Congratulations! Your score is now {score}!")

        else:
            score -= user_input
            print("Sorry, you lose!")
            print(f"Your new score is {score} :(")

        total_score += score
        print(f"Your total score is {total_score}")



poptoc_func()
