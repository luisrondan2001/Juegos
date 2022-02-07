import turtle
import time
import random

posponer = 0.1
puntos = 0
puntuacion_mas_alta = 0
#config de la centana
wn = turtle.Screen()
wn.title("Juego del gusanito")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"
cabeza.color("green")
#comida de la serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.goto(0,100)
comida.direction = "stop"
comida.color("red")


#cuerpo serpiente
segmentos = []

#Marcador en pantalla. 
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Puntos: 0   Puntuacion mas alta: 0", align="center", font = ("courier", 24, "normal"))


#funciones
def arriba():
    cabeza.direction = 'up'
def abajo():
    cabeza.direction = 'down'
def izquierda():
    cabeza.direction = 'left'
def derecha():
    cabeza.direction = 'right'

#funciones 
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
        
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
#teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

        
#bucle principal
while True:
    wn.update()
    #colisiones con los bordes. 
    if cabeza.xcor() > 280 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        #esconder los segmentos 
        for segmento in segmentos:
            segmento.goto(10000, 10000)
        #limpiar lista de segmentos
        segmentos.clear()
        #resetear Marcador
        puntos = 0
        texto.clear()
        texto.write("Puntos: {}   Puntuación más alta: {} ".format(puntos, puntuacion_mas_alta), align="center", font = ("courier", 24, "normal"))

    #colisiones de la comida 
    if cabeza.distance(comida) < 20:
        y = random.randint(-280, 280)
        x = random.randint(-280, 280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.penup()
        nuevo_segmento.goto(0,0)
        nuevo_segmento.direction = "stop"
        nuevo_segmento.color("grey")
        segmentos.append(nuevo_segmento)
        #aumentar marcador. 
        puntos += 1
        if puntos > puntuacion_mas_alta:
            puntuacion_mas_alta = puntos
        texto.clear()
        texto.write("Puntos: {}   Puntuación más alta: {} ".format(puntos, puntuacion_mas_alta), align="center", font = ("courier", 24, "normal"))

    # el cuerpo de la serpiente
    totalSeq = len(segmentos)
    for index in range(totalSeq -1, 0, -1):
        x = segmentos[index -1].xcor()
        y = segmentos[index -1].ycor()
        segmentos[index].goto(x,y)
    if totalSeq > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
    
    mov()
    #colisiones con el cuerpo. 
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20: 
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            #Esconder los segmemtos. 
            for segmento in segmentos:
                segmento.goto(1000,10000)
            
            segmentos.clear()
            puntos = 0
            texto.clear()
            texto.write("Puntos: {}   Puntuación más alta: {} ".format(puntos, puntuacion_mas_alta), align="center", font = ("courier", 24, "normal"))

        
    time.sleep(posponer)

#bucle para que no se cierre la ventana siempre va al final.
wn.mainloop()