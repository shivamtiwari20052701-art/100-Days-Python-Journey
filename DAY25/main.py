import turtle 
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "DAY25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

States_data = pandas.read_csv("DAY25/50_states.csv")
all_states = States_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
  answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="whats the another states name?").title()

  if answer_state == "Exit":
     missing_states = [state for state in all_states if state not in guessed_states]#using list comprehnsion
    #  for state in all_states:
    #     if state not in guessed_states:
    #        missing_states.append(state)
     new_data = pandas.DataFrame(missing_states)
     new_data.to_csv("DAY25/states_to_learn.csv")
     break
  #if answer of the state is one of the states of 50_states.csv
  if answer_state in all_states:
      guessed_states.append(answer_state)
      #if they got it right
        #create a turtle to write the name of the state using its x and y point 
      t = turtle.Turtle()
      t.penup()
      t.hideturtle()
      state_data = States_data[States_data.state == answer_state]
      t.goto(state_data.x.item(),state_data.y.item())#item only takes first element from that particular row
      t.write(answer_state)