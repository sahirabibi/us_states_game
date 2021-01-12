import pandas as pd 
import turtle 
from turtle import Turtle 

# create window 
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# -------------------------------- State Coordinates ----------------------------------------- #
# get coordinates of states 

def get_mouse_click_cor(x, y):
    print(x, y)
# click on different areas on turtle window in order to recieve x, y coordinates.     
# turtle.onscreenclick(get_mouse_click_cor) <<<---- uncomment if starting blank  


# ------------------------Generate state labels and coordinates list ------------------------- # 

# generate text on window based on user input 
class State(Turtle):
    def __init__(self, answer,coordinates):
        """create a turtle text object with the answer if correct using name of state and tuple of coordinates"""
        super().__init__()
        self.hideturtle()
        self.penup()  
        self.goto(coordinates)      
        self.write(arg=answer.title(), align='center', font=('Courier', 11, 'normal'))
        

# create a dataframe for states
data = pd.read_csv('./50_states.csv')
# isolate column of states as a list to check answer against 
states_list = data.state.to_list()
# get a tuple of x, y value from dataframe
data['coordinates'] = list(zip(data.x, data.y))
# list of all coordinates 
coordinates_list = data.coordinates.to_list()


# ------------------------------- Game Play -------------------------------------------------- #

# store guessed states 
guessed_states = []
game_on = True
# count correct guessed states
correct = 0  
# prompt user to guess state
answer = screen.textinput(title=f"Guess a state {correct}/50", prompt = "Type a name of state.")

while game_on: 
    if answer.title() in states_list:
        # get the index of the state in order to match with correct coordinates tuple 
        match_index = states_list.index(answer.title())
        # pass values to State class to generate turtle object
        State(answer, coordinates_list[match_index])
        # increase number of correct answers out of 50 by one
        correct += 1
        guessed_states.append(answer)
        # print prompt screen again and ask for guess 
        answer = screen.textinput(title=f"Guess a state{correct}/50", prompt = "Type a name of state.")    
    elif answer.lower() == 'exit' or correct == 50:
        turtle.write(f"Thanks for playing.\nTotal: {correct}/50", align='center',font=('Courier', 18, 'normal'))
        unguessed_states = [state for state in states_list if state not in guessed_states]
        game_on = False
    else:
        # incorrect, reprint prompt screen
        answer = screen.textinput(title=f"Guess a state{correct}/50", prompt = "Type a name of state.")


print(len(unguessed_states))
screen.mainloop()


