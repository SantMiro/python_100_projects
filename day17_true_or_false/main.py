#################################
# Title: True or False Quiz     #
# Author: Santiago Miro         #
#        June 2024              #
#################################

'''This is a game of true or false. The user guesses is an statement is true or false and gets points if correct.'''

import data
from quiz import Quiz # Quiz class of the game

question_data = data.question_data # The original questions
game_over = False # Start a new game
quiz = Quiz(question_data,game_over) # quiz object
questions = quiz.shuffle_questions() # Shuffle questions to get a different game each time


def quiz_game(game_over,quiz,questions):
    start = input('\nDo you want to start a new game? Type "y" or "n". \n')
    if start == 'y':
        while not game_over:   
            quiz.check_answer(questions)
            game_over = quiz.end_game(questions)
        quiz_game(game_over,quiz,questions)

quiz_game(game_over,quiz,questions)



