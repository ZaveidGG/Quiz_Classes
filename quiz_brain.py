class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def nextQuestion(self):
        while self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"\nQ.{self.question_number}:{current_question.text} (True/False):")
            correct_answer = current_question.answer
            self.check_answer(user_answer, correct_answer)
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            self.score += 1
            print("Your answer is correct!")
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print(f"Your answer is wrong. The correct answer is {c_answer}")
            print(f"Your current score is {self.score}/{self.question_number}")