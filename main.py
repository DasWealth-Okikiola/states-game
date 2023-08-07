from Score_Turtle import Writer
import turtle
import pandas

screen = turtle.Screen()
screen.title("Das_Guess_The_States_GAME")
image = "blank_states_img.gif"
turtle.bgpic(image)

dataFrame = pandas.read_csv("50_states.csv")
all_states = dataFrame.state.to_list()
Guessed_state = []

while len(Guessed_state) < 50:
    answer = screen.textinput(title=f"{len(Guessed_state)}/50 correct!",
                              prompt="Write a USA state name").title()
    if answer == "Exit":
        left_states = []
        for state in all_states:
            if state not in Guessed_state:
                left_states.append(state)
        left_states_data = pandas.DataFrame(left_states)
        left_states_data.to_csv("Unlearnt_States.csv")

        break
    if answer in all_states:
        Guessed_state.append(answer)
        answer_row = dataFrame[dataFrame.state == answer]
        Writer(coordinate=(int(answer_row.x), int(answer_row.y)), state=answer)

# screen.exitonclick()
