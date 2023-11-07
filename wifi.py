from turtle import*
bgcolor("black")
colors = ["red", "yellow", "blue", "green"]
speed (10*100000000)
for x in range(6000):
    pencolor(colors[x%4])
    forward(x)
    left(95)