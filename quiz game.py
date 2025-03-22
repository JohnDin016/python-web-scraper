# ----------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1


    for key in questions:
        print("# --------------------------- ")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# ----------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!!")
        return 0

# ----------------------------
def display_score(correct_guesses, guesses):
    print("# ----------------------------")
    print("RESULTS!")
    print("# ----------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


# ----------------------------
def play_again():

    response = input("Do you want to play again? (yes/no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# ----------------------------

questions = {"What is the biggest country in the world?: ": "A",
    "What planet is known as the Red Planet: ": "B",
    "Who painted the Mona Lisa?: ": "C",
    "How many continents are there?: ": "D"}

options = [["A. Algeria","B. Germany","C. Russia","D. Nigeria"],
          ["A. Mars","B. Sun","C. Moon","D. Earth"],
          ["A. Ronaldo","B. Brad Pitt","C. Leonardo da Vinci","D. Messi"],
          ["A. 8","B. 10", "C. 11", "D. 7"]]
new_game()


while play_again():
    new_game()

print("BYEEEEE")