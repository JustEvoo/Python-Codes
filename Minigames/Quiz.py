
questions = ("What is the capital of France? ",
             "Which planet is known as the Red Planet? ",
             "What is the largest ocean on Earth? ",
             "Who wrote 'Romeo and Juliet'? ",
             "What is the chemical symbol for gold? ")

options = (("A. Paris", "B. London", "C. Berlin", "D. Madrid"),
           ("A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"),
           ("A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"),
           ("A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"),
           ("A. Ag", "B. Au", "C. Fe", "D. Pb"))
answers = ("A", "B", "D", "B", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("="*50)
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Please enter your guess: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
    question_num += 1

print("="*50)
print("RESULT")
print("="*50)

print("Guesses: ", end = "")
for guess in guesses:
    print(guess, end=" ")
print()
print("Answers: ", end = "")
for answer in answers:
    print(answer, end=" ")
print()
result = int(score / len(questions) *100)
print(f"score : {result}%")