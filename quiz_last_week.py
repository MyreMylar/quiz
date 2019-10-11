import csv
import random


# Define class
class QuizQuestion:
    def __init__(self, question, answer_a, answer_b, answer_c, right_answer):
        self.question = question
        self.answer_a = answer_a
        self.answer_b = answer_b
        self.answer_c = answer_c
        self.right_answer = right_answer
        

# load quiz questions from file to list
quiz_questions_list = []
with open("questions.csv") as questions_file:
    read_csv = csv.reader(questions_file, delimiter=',')
    for row in read_csv:
        if len(row) == 5:
            quiz_questions_list.append(QuizQuestion(row[0], row[1], row[2], row[3], row[4]))


# run quiz with a for loop
random.shuffle(quiz_questions_list)
total_score = 0
for quiz_question in quiz_questions_list:
    print(quiz_question.question)
    print("A: " + quiz_question.answer_a)
    print("B: " + quiz_question.answer_b)
    print("C: " + quiz_question.answer_c + "\n")

    playerInput = input("Type answer letter and then press enter: ")

    if playerInput.upper() == quiz_question.right_answer:
        print("\nCorrect!\n\n")
        total_score += 1
    else:
        print("\nWrong.\n\n")

# print final results
print("End of Quiz")
print("Total score = " + str(total_score) + "/" + str(len(quiz_questions_list)))
