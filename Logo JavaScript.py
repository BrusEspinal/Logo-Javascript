from turtle import *
lapiz = Turtle()

lapiz.pensize(1)
lapiz.speed(2)
bgcolor("#21252B") 
lapiz.shape("circle")
lapiz.turtlesize(.5)

figura1 = [(80, -90), (120, 150), (-120, 150), (-90, -80), (0, -120)]
figura2 = [(70, -80), (110, 140), (0, 140), (0, -100)]
texto1 = [(-15, 100), (-35, 101), (-35, -40), (-70, -30), (-69, -55), (-15, -70)]
texto2 = [(60, -60), (75, 30), (35, 25), (40, 70), (80, 70), (85, 100), (10, 100), (10, 0), (50, 5), (45, -35), (10, -40), (10, -70)]

def pintar(color, puntoInicial, coordenadas):
    lapiz.color(color)
    lapiz.penup()
    lapiz.goto(puntoInicial)
    lapiz.pendown()
    lapiz.begin_fill()
    for x in range(len(coordenadas)):
        lapiz.goto(coordenadas[x])
    lapiz.end_fill()
    
pintar("#DAB92D", (0, -120), figura1)
pintar("#F0DB4F", (0, -100), figura2)
pintar("#FFFFFF", (-15, -50), texto1)
pintar("#FFFFFF", (10, -70), texto2)

lapiz.hideturtle()
done()
