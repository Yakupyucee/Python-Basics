class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self,answer):
        return self.answer == answer
    
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionIndex + 1} of {len(self.questions)}". center(80,"*"))
        print(f"{self.questionIndex + 1}. Soru : {question.text}") 

        for q in question.choices:
            print(f"-{q}")    
        
        answer = input("Answer : ")
        self.guess(answer)

    def guess(self,answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            print("Your answer is correct.")
            self.score += 1
        else:
            print(f"Your answer is wrong. Correct answer is {question.answer.upper()}.")
        self.questionIndex += 1
        self.loadQuestion()
    
    def loadQuestion(self):
        if(len(self.questions) == self.questionIndex):
            print(f"The quiz is over. \nScore: {self.score}")
        else:
            self.displayQuestion()


q1 = Question("What is the most popular programming language?",["python","java","C++","C"],"python")
q2 = Question("What is the most used programming language?",["python","java","C++","C"],"python")
q3 = Question("What is the easiest programming language to learn?",["python","java","C++","C"],"python")
questions = [q1,q2,q3]

quiz = Quiz(questions)

quiz.loadQuestion()
