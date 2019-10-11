# ---------------------------------------------------------------------------------------------------------------
# Challenge 1
# -------------
#
# Using some code from last week's quiz solution and some from
# the pygame text example code file, open a pygame window and draw the
# first question (with answers) in the loaded questions list
# to the window.
#
# HINTS
# - Start by opening up the pygame_draw_text file in the code editor, and
#   see if you can change the text
# - You can reference the first item in a list using an index of 0
#   like so: quiz_questions_list[0]
# - You can treat an indexed list member like a variable of that type
#   so you can access it's data members and functions,
#   like so: quiz_questions_list[0].answer_a
# ---------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------
# Challenge 2
# ---------------------
#
# Use pygame's keyboard input event system to change
# the displayed question when the K_RETURN key is pressed.
#
# HINTS
#
# - You may find it useful to have an integer variable representing
#   the current index position in the list.
# - You can index into a list using an integer variable just as with a
#   a number, like so: quiz_questions_list[current_question_index]
# ---------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------
# Challenge 3
# ----------------------
# We are going to recreate the control flow of our text quiz program in pygame.
#
# First - Add a True or False bool variable to check whether the current question has been answered or not.
# You will need to reset this variable to False each time we change to a new question.

# Second - Use pygame's keyboard events to check when the letters a, b or c are pressed and set
# your current_question_answered variable to True.
#
# Third - Use an if statement to only allow the Return key to change to a new question if the
# current_question_answered variable is True.
#
# Fourth - While current_question_answered is True display pygame text saying 'Correct' or 'False' depending on
# if the correct answer was pressed in step 2.
#
# If you've done all that you should have the basics of a functioning pygame quiz.
# ---------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------
# Bonus Challenges
# -----------------------------
# Put some final polish on your quiz.
#
# - Add back final score tracking and display and generally stop the quiz from crashing at the end.
#   Perhaps add a 'retry quiz Y/N' prompt that starts the program over from the beginning.
# - Use random.shuffle() to ask the questions in a random order.
# - Add a 20 second time limit to answer each question and display the remaining time.
#
# HINT
# - You can track time with a clock = pygame.time.Clock().
# - You can call clock.tick(60) to get the number of milliseconds since tick() was last called.
# - By adding the value of tick to a variable each loop we can keep track of how many milliseconds have passed
#   since we last set the variable to zero. You could also start a timer at 20,000 milliseconds (20 seconds)
#   and subtract ticks from it.
# - Don't forget to divide your counter by 1,000 before displaying it.
# - You will also want to round and convert your number of seconds to remove all the decimal places.
#   Try something like - str(int(round(question_timer/1000)))
# ---------------------------------------------------------------------------------------------------------------
