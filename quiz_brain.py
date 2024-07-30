'''TODO: 
asking the questions
checking if the answer was correct
checking if we're the end of the quiz
'''
class QuizBrain:
    def __init__(self, question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0

    def next_quesiton(self):
        #retrieve the item at the currect question_number from the question_list
        #use the imput() function to show the user the Question text and ask for the user's answer
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer= input(f"Q. {self.question_number}: {current_question.text} (True/False): ") 
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return (self.question_number <len(self.question_list))
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower()== correct_answer.lower():
            self.score+=1
            print("you got it right")
        else:
            print("that's wrong.")

        print(f"the correct answer is {correct_answer}")
        print(f"your current score is {self.score}/{self.question_number}")
        print("\n")

