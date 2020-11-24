import turtle
poli = turtle.Turtle()
nLati = (int)(input("numero di lati: "))
poli.color('red','yellow')
poli.begin_fill()
ang = 360 / nLati
for _ in range (nLati):
    poli.forward(50)
    poli.left(ang)
poli.end_fill()


#import turtle importa il modulo turtle
#from turtle impoert * importa tutte le classi nel modulo turtle