# ------------------------------------------------------------------------------------------------
# Overview of Quiz Week 2
# --------------------------------------------------------------
# We are going to recode the quiz program from last week to achieve the following
# goals:
#
# Challenge 1:  Put some of the question and answer strings from last week
#               into a newly defined QuizQuestion class, and then put those into
#               a python list.
# Challenge 2:  Use a single for loop over our new list to run the
#               quiz logic (if...else) test, wait for input and keep score as
#               to recreate the results of what we made last week.
# Challenge 3:  Instead of writing the questions and answer strings in code,
#               load them from a (provided) csv text file and store them in
#               your list.
#
# ------------------------------------------------------------------
# But.. I wasn't here last week!/Didn't complete the code last week!
# ------------------------------------------------------------------
# In the 'quiz_last_week' file is some code that completes the challenges from last week.
# You can use that to start from, or cut and paste your own code from last week here
# if you have some.
#
# There are more comments below with extended hints for each of the three
# challenges.
# ------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------
# Challenge 1 - part 1
# ------------------------------------------------------------------------------------------------
#
#  Define a QuizQuestion class and create a few QuizQuestions.
#
#  In case you have forgotten how to create a class, here are a few tips:
#
# - We start defining a class with the 'class' keyword, a name, some brackets and a colon.
#   After that you are ready to start defining class functions.
# - Use the special '__init__' class function to pass in data and setup a class' data variables
#   In our case it will be strings for the questions and the answers plus an extra variable
#   for the correct answer's letter (A, B or C)
# - When using class variables, and when calling class functions from within a class definition
#   we have to use the self. keyword - see below for an example.
# - We need to make a class that can accept five strings on creation,
#   one for the question, three for the possible answers and
#   one for the correct answer letter (A,B or C)
# - I've created an example class below you can adapt into your QuizQuestion class, or just delete.
#
# --------------------------------------------------------------------------------------------------


class ExampleClass:
    def __init__(self, input_1, input_2, input_3, input_4, input_5):
        self.class_variable_1 = input_1
        self.class_variable_2 = input_2
        self.class_variable_3 = input_3
        self.class_variable_4 = input_4
        self.class_variable_5 = input_5


# creating a class instance
my_example_class = ExampleClass("What is the best school?", "Rutlish", "Hogwarts", "School of Rock", "A")

# accessing member data of a class and printing it
print("a my_example_class variable:" + str(my_example_class.class_variable_1))


# ------------------------------------------------------------------------------------------------
# Challenge 1 - part 2
# -----------------------
#
# Store a couple of QuizQuestions in a python list.
#
# TIPS
#
# - Create an empty python list variable using a pair of square brackets
#   Like so: my_empty_list = []
# - Add new items to the list using the append function.
#   Like so: my_list.append(my_quiz_question_1)
# ------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------
# Challenge 2
# ---------------
#
# Use a for loop to run through the QuizQuestions in our new list, print their questions
# and answers, wait for user input and then check if the input letter was correct.
#
#  TIPS
#
# - This is basically recreating the logic of the program we created last week but
#   using a loop to fill in the data rather than doing it all by hand question by question.
# - Start by using the 'in' keyword to quickly run through all items in a list.
#   Like so: for question in my_questions_list:
# - Use the 'print' and 'input' function to put the data on the screen and wit for input.
# - Compare the input with the correct answer variable of your quiz question class.
# - track the score as before and output it when you finish the quiz
# ------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------
# Challenge 3
# --------------
#
# Load QuizQuestions from a csv file and then store them in our list.
#
# - You will want to add this file loading code above the other bits of code you have written.
# - There is a .csv file included in this weeks code folder
#   folder. It contains a few questions.
# - A csv file is just a text file with bits of data
#   separated by new lines and commas. Thus the full name of the file
#   format 'Comma Separated Values' - or the acronym 'csv' for short.
# - The quiz questions in our CSV file are separated into rows that
#   look like this:
#       "Who designed the first computer?","Bill Gates","Steve Jobs","Charles Babbage",C
#
# - Python has support for loading csv files using the 'csv' library.
#   you will need to use'import csv' to complete this challenge.
# - To load data from a file you can use something like the following code -
#
#   with open('name_of_file.csv') as csv_file: # opens the file
#       read_csv = csv.reader(csv_file, delimiter=',') # loads it as a CSV file
#       for row in read_csv: # loops through each row in the file
#           loaded_data_value_1 = row[0] # row indexes correspond to values in the file separated by commas
#           loaded_data_value_2 = row[1]
#
# ------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------
# Bonus Challenges
# -------------------
#
# 1. See how far you can get recreating this quiz program in pygame
#   - I have included a 'pygame_draw_text' file that shows how to
#     create a pygame window, draw text and mess about with keyboard
#     input.
#
# 2. Consider how to add:
#    - a count down time in which a player must answer or fail the question.
#    - multiple themed rounds of questions (e.g. music, film, sport)
#    - Two (or more) players taking turns to answer questions and keeping scores
#      for each of them
#
# ------------------------------------------------------------------------------------------------
