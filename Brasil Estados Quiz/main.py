import turtle
import pandas
import tkinter as tk

image_width = 500
image_height = 441

FONT = ("Arial", 10, "normal")
df = pandas.read_csv("estados.csv")
estados = df.state.to_list()

def create_screen(title, width, height, bg_color):
    screen = turtle.Screen()
    screen.title(title)
    screen.setup(width=width, height=height)
    screen.bgcolor(bg_color)
    return screen


screen = create_screen("Estados do Brasil", image_width, image_height, "white")
image = "mapa_brasil2.gif"
screen.addshape(image)
turtle.shape(image)

screen.tracer(0)
t = turtle.Turtle()
t.hideturtle()
t.penup()

correct_states = []
game_is_on = True

while game_is_on:
    screen.update()
    answer = screen.textinput(f"{len(correct_states)}/27 estados", "Digite um estado")
    if answer:
        answer_state = answer.title()
        if answer_state == "Desisto":
            missing_states = [state for state in estados if state not in correct_states]
            new_data = pandas.DataFrame(missing_states, columns=['state'])
            new_data.to_csv("states_to_learn.csv", index=False)
            for state in missing_states:
                state_data = df[df.state == state]
                if not state_data.empty:
                    try:
                        x, y = int(state_data.x.values[0]), int(state_data.y.values[0])
                        t.setpos(x, y)
                        t.color("dark red")
                        t.write(state, font=FONT)
                    except ValueError:
                        print(f"Invalid coordinates for {state}")
            break
        if answer_state in estados:
            state_data = df[df.state == answer_state]
            if not state_data.empty:
                try:
                    x, y = int(state_data.x.values[0]), int(state_data.y.values[0])
                    t.goto(x, y)
                    t.write(answer_state, font=FONT)
                    correct_states.append(answer_state)
                except ValueError:
                    print(f"Invalid coordinates for {answer_state}")
        if len(correct_states) == 27:
            screen.bye()
            window = tk.Tk()
            window.title("Parabéns!")
            label = tk.Label(window, text="Parabéns! Você acertou todos os estados do Brasil! 🇧🇷")
            label.pack(pady=20, padx=40)
            window.mainloop()

screen.exitonclick()
