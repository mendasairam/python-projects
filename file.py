def ask_question(question, options, correct_answer):
    print(question)
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    
    try:
        answer = int(input("Enter the number of your answer: "))
        if 1 <= answer <= len(options):
            if options[answer - 1] == correct_answer:
                print("Correct!")
                return True
            else:
                print("Wrong!")
                return False
        else:
            print("Invalid choice. Please select a number from the options.")
            return False
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False

def run_quiz(questions):
    score = 0
    total_questions = len(questions)
    
    for question, options, correct_answer in questions:
        if ask_question(question, options, correct_answer):
            score += 1
    
    print(f"\nQuiz complete! Your final score is {score}/{total_questions}.")

questions = [
             
    ("Which country won world cup in cricket in 2011 ?", ["Bangaladesh", "Australia", "Sri Lanka", "India"], "India"),
    ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], "Mars"),
    ("Who wrote 'To Kill a Mockingbird'?1", ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"], "Harper Lee"),
    ("What is the chemical symbol for gold?", ["Au", "Ag", "Pb", "Fe"], "Au")
]
run_quiz(questions)
