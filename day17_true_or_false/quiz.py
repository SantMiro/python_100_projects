import random

class Quiz():

    '''Quiz class to play true or false.'''
    
    def __init__(self,question_data,game_over):

        '''Set game over boolean, questions and counters for round and score.'''

        self.game_over = game_over
        self.question_data = question_data
        self.round = 1
        self.score = 0

    def shuffle_questions(self):

        '''Shuffle the questions to get different orders.'''

        questions = self.question_data.copy()
        random.shuffle(questions)
        return questions
    
    def pick_question(self,questions):

        '''Picks a question from list and asks user for answer.'''

        question = questions[self.round-1]
        answer = input(f'Q. {self.round}: {question['text']} True or False? ')
        return question, answer
    
    def check_answer(self,questions):

        '''Checks if answer is correct or incorret. Updates counters of round and score.'''

        question, answer = self.pick_question(questions)
        if answer == question['answer'].lower():
            print('You got it right!')
            print(f'The correct answer was {question["answer"]}.')
            self.score += 1
            print(f'Your current score is: {self.score}/{self.round}')
            self.round += 1
        else:
            print('You got it wrong.')
            print(f'The correct answer was {question['answer']}.')
            print(f'Your current score is: {self.score}/{self.round}')
            self.round += 1

    def end_game(self,questions):

        '''End the game when there are no more questions.'''

        if self.round == len(questions) + 1:
            print('\nThat is the end of the game.')
            print(f'Your final score is: {self.score}/{self.round-1}.\n')
            self.game_over = True
        else:
            self.game_over = False
        return self.game_over