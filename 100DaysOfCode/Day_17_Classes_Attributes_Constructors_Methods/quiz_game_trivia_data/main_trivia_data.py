from question_model_trivia_data import Question
from data_trivia_data import question_data
from quiz_brain_trivia_data import QuizBrain

question_bank = []
for qa in question_data:
    question_bank.append(Question(qa['question'], qa['correct_answer']))  # simply change dictionary key names

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print('Quiz completed.')
print(f'Final Score: [Correct/Total]: {quiz.score}/{quiz.question_number}')
