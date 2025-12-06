from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))


quiz_brain = QuizBrain(question_bank)

while quiz_brain.has_questions():
    quiz_brain.next_question()

print(f"You have completed the quiz !!! \n"
      f"your final score is: {quiz_brain.score}/{len(question_bank)}")