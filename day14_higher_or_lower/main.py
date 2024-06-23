import game_data
import random

def pick_user(data):
    user = random.choice(data)
    user_name  = user['name']
    user_count = user['follower_count']
    return user_name, user_count

def correct(score, new_user_name, new_user_count):
    score +=1
    user_name, user_count = new_user_name, new_user_count
    print(f'\n                  Correct! Your score is {score} points.\n')
    print(user_name)
    return score, user_name, user_count

def incorrect(score,end_turn):
    print(f'\n                  Incorrect! Your final score is {score}.\n')
    end_turn = True
    return end_turn

data = game_data.data


def higher_or_lower():
    start = input('\nDo you want to start a new game of higher or lower? Type "y" to start or "n" to exit. ')
    if start == 'y':
        print('\nSelect if the profile at the bottom has a higher or lower number of followers on Instagram than the one at the top.')
        print('Type "h" if it has more followers and "l" is it has fewer.\n') 
        end_turn = False
        user_name, user_count = pick_user(data)
        print(user_name)
        score = 0

        while not end_turn:
            
            print(game_data.vs)
            new_user_name, new_user_count = pick_user(data)
            print(new_user_name,'\n')
            choice = input('Type "h" if it has more followers and "l" is it has fewer.') 
            if choice == 'h' and user_count <= new_user_count:
                score, user_name, user_count = correct(score, new_user_name, new_user_count)
            elif choice == 'h' and user_count >= new_user_count:
                end_turn = incorrect(score,end_turn)
            elif choice == 'l' and user_count >= new_user_count:
                score, user_name, user_count = correct(score, new_user_name, new_user_count)
            elif choice == 'l' and user_count <= new_user_count:
                end_turn = incorrect(score,end_turn)
        higher_or_lower()

higher_or_lower()
