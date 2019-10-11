import pygame
from pygame.locals import *
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


def set_active_quiz_question(question_data: QuizQuestion, question_index: int):
    drawn_text_data = []

    y_pos = 100
    question_text_render = font.render(str(question_index + 1) + ". " + question_data.question,
                                       True, pygame.Color("#000000"))
    question_text_render_rect = question_text_render.get_rect(centerx=320, centery=y_pos)
    drawn_text_data.append([question_text_render, question_text_render_rect])
    y_pos += 30

    answer_a_text_render = font.render("A: " + question_data.answer_a, True, pygame.Color("#000000"))
    answer_a_text_render_rect = answer_a_text_render.get_rect(x=250, centery=y_pos)
    drawn_text_data.append([answer_a_text_render, answer_a_text_render_rect])
    y_pos += 20

    answer_b_text_render = font.render("B: " + question_data.answer_b, True, pygame.Color("#000000"))
    answer_b_text_render_rect = answer_b_text_render.get_rect(x=250, centery=y_pos)
    drawn_text_data.append([answer_b_text_render, answer_b_text_render_rect])
    y_pos += 20

    answer_c_text_render = font.render("C: " + question_data.answer_c, True, pygame.Color("#000000"))
    answer_c_text_render_rect = answer_c_text_render.get_rect(x=250, centery=y_pos)
    drawn_text_data.append([answer_c_text_render, answer_c_text_render_rect])

    return drawn_text_data


random.shuffle(quiz_questions_list)
total_score = 0

pygame.init()
screen = pygame.display.set_mode((640, 480))

background = pygame.Surface(screen.get_size())
background = background.convert(screen)
background.fill((220, 220, 220))

font = pygame.font.Font(None, 20)

correct_answers = 0
active_quiz_question = 0
rendered_text_data = set_active_quiz_question(quiz_questions_list[active_quiz_question], active_quiz_question)

correct_text = None
correct_text_rect = None

answer_key = ""
question_answered = False

end_of_game = False
end_text_1 = None
end_text_1_rect = None
end_text_2 = None
end_text_2_rect = None

clock = pygame.time.Clock()
is_running = True
while is_running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            is_running = False
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                if question_answered:
                    if active_quiz_question < len(quiz_questions_list) - 1:
                        active_quiz_question += 1
                        rendered_text_data = set_active_quiz_question(quiz_questions_list[active_quiz_question],
                                                                      active_quiz_question)
                        question_answered = False
                        correct_text = None
                    else:
                        rendered_text_data = []
                        correct_text = None
                        question_answered = False
                        end_of_game = True
            new_key_pressed = True
            if event.key == K_a:
                answer_key = "A"
                question_answered = True
            if event.key == K_b:
                answer_key = "B"
                question_answered = True
            if event.key == K_c:
                answer_key = "C"
                question_answered = True

    if question_answered and correct_text is None:
        if answer_key == quiz_questions_list[active_quiz_question].right_answer:
            correct_text = font.render("Correct! - Press enter for next question.", True, pygame.Color("#000000"))
            correct_text_rect = correct_text.get_rect(centerx=320, centery=300)
            correct_answers += 1
        else:
            correct_text = font.render("Wrong! - Press enter for next question.", True, pygame.Color("#000000"))
            correct_text_rect = correct_text.get_rect(centerx=320, centery=300)

    screen.blit(background, (0, 0))

    if end_of_game:
        if end_text_1 is None:
            end_text_1 = font.render("End of quiz", True, pygame.Color("#000000"))
            end_text_1_rect = end_text_1.get_rect(centerx=320, centery=200)

            end_text_2 = font.render("You answered " + str(correct_answers) + "/21 correctly",
                                     True, pygame.Color("#000000"))
            end_text_2_rect = end_text_2.get_rect(centerx=320, centery=230)
        screen.blit(end_text_1, end_text_1_rect)
        screen.blit(end_text_2, end_text_2_rect)
    else:
        for text in rendered_text_data:
            screen.blit(text[0], text[1])

        if question_answered:
            screen.blit(correct_text, correct_text_rect)

    pygame.display.flip()  # flip all our drawn stuff onto the screen

pygame.quit()  # exited game loop so quit pygame
