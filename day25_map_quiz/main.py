import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('Mexico Map Game')
image = 'mexico-greyedout.gif'
screen.addshape(image)

turtle.shape(image)

def write_on_map(x,y,state):
    pen = turtle.Turtle(visible=False)
    pen.penup()
    pen.goto(x,y)
    pen.write(state, align = 'center', font = ('Arial',6,'normal'))

coordinates = pd.read_csv('coordinates.csv')


game_on = True
found = 0
guessed_states = []

while game_on:
    answer_state = screen.textinput(title=f'{found}/32 states found.', prompt="Write a state's name: ")
    if not answer_state:
        game_on = False
    else:
        answer_state.capitalize()
        if answer_state in coordinates.States.values and answer_state not in guessed_states:
            row = coordinates[answer_state == coordinates.States]
            x = int(row.X.iloc[0])
            y = int(row.Y.iloc[0])
            state = row.States.iloc[0]
            write_on_map(x,y,state)
            found += 1
            guessed_states.append(answer_state)
    if found == 32:
        game_on = False

# with open('states.txt') as states:
#     states_list = states.readlines()

# states_list = [i.strip() for i in states_list]

# data = pd.read_csv('coordinates.csv')

# data['States'] = states_list

# data.to_csv('coordinates.csv',index=False)
# x_coordinates = []
# y_coordinates = []
# click_count = 0

# def get_mouseclick_coor(x, y):
#     global x_coordinates, click_count, y_coordinates
#     x_coordinates.append(x)
#     y_coordinates.append(y)
#     click_count += 1
#     if click_count >= 32:
#          # Save coordinates to a CSV file using pandas
#         df = pd.DataFrame({'X':x_coordinates,'Y':y_coordinates})
#         df.to_csv('coordinates.csv', index=False)
#         # Optionally, stop listening for clicks after 32 clicks
#         screen.onscreenclick(None)



# turtle.onscreenclick(get_mouseclick_coor)
#print(coordinates)
turtle.mainloop()
#screen.exitonclick()