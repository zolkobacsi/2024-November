import random
import os


def question(questions):
    if len(questions) == 0:
        print("You have run out of questions. Thank you for playing.")
        exit()
    select = random.randint(0, len(questions) - 1)
    return_question = questions[select]
    questions.pop(select)
    return return_question


def answer_check(answer, right_answer):
    if answer.capitalize() == right_answer.capitalize():
        return True
    else:
        return False
    

def player_score(score):
    score += 1
    return score
    

def new_game():
    continue_playing =input("\nWould you like to continue the game? Yes/No\n")
    if continue_playing.lower() != "yes":
        print("Thank you for playing my game.")
        exit()


questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Madrid", "B) Paris", "C) Berlin", "D) Rome"],
            "answer": "B"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
            "answer": "B"
        },
        {
            "question": "What is the square root of 64?",
            "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
            "answer": "C"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["A) Gold", "B) Oxygen", "C) Silver", "D) Osmium"],
            "answer": "B"
        },
        {
            "question": "In which year did World War II end?",
            "options": ["A) 1945", "B) 1946", "C) 1944", "D) 1943"],
            "answer": "A"
        }
    ]

decision = True
score = 0
number_of_games = 0


os.system("cls")
print("""
WElcome to my quizz show! Today you are our chosen to answer the questions, and hopefully you'll do great!
(Press ENTER to continue)""")
input()

while decision:
    number_of_games += 1
    selected_question = question(questions)
    right_answer = selected_question["answer"]

    os.system("cls")
    print(selected_question["question"])
    formatted_options = "\n".join(selected_question["options"])
    print(formatted_options)

    answer = input("Please andswer with a letter of your choice from the option list.")

    if answer_check(answer, right_answer):
        score = player_score(score)
        success_percentage = (score / number_of_games) * 100
        print(f"You answered correctly. You have {score}/{number_of_games} points. Success rate:{success_percentage:.2f}")
    else:
        success_percentage = (score / number_of_games) * 100
        print(f"That wasn't the correct answer. It was {right_answer}. You current score is {score}/{number_of_games}. Success rate:{success_percentage:.2f}")
    
    new_game()
    