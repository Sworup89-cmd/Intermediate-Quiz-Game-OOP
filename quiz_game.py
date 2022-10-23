class QuizGame:

    def __init__(self, q_list):
        self.question_no = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_no]
        self.question_no += 1
        print(question.q_text)
        user_answer = input("Enter your answer")
        self.check_answer(user_answer, question.q_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Right Answer")
        else:
            print("Wrong Answer")

