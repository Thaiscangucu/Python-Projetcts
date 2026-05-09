import turtle
import pandas

df = pandas.read_csv("estados.csv")
all_states = df.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "mapa_brasil2.gif"
turtle.addshape(image)
turtle.shape(image)

def get_mouse_click_cor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_cor)
turtle.mainloop()