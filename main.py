from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from art import logo

print(logo)

question_bank = []
for QA in question_data:
    newQuestion = Question(QA["text"], QA["answer"])
    question_bank.append(newQuestion)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.nextQuestion()

print("\n\nYou've completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")

