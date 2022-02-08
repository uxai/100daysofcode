class QuizBrain:
    def __init__(self, question_list):
        self.questions_list = question_list
        self.question_number = 0
        self.score = 0

    def has_question(self):
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}: {current_question.text} True/False? ")
        self.check_answer(response, current_question.answer)
        
    def check_answer(self, response, answer):
        if response.lower() == answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print(f"You got it wrong, the correct answer is {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
