from turtle import *
def crearSistemaL(numIters,axioma):
 cadenaInicio = axioma
 cadenaFin = ""
 for i in range(numIters):
     cadenaFin = procesarCadena(cadenaInicio)
     cadenaInicio = cadenaFin
 return cadenaFin
def procesarCadena(cadenaVieja):
 nuevaCadena = ""
 for ch in cadenaVieja:
     nuevaCadena = nuevaCadena + aplicarReglas(ch)
 return nuevaCadena
def aplicarReglas(ch):
 nuevaCadena = ""
 if ch == 'X':
     nuevaCadena = 'F+[[X]-X]-F[-FX]+X' # Regla 1
 elif ch == 'F':
     nuevaCadena = 'FF' # Regla 2
 else:
     nuevaCadena = ch # No se aplica regla, mantenemos el caracter
 return nuevaCadena
def dibujarSistemaL(aTurtle, instrucciones, angulo, distancia):
     pila = []
     aTurtle.penup()
     aTurtle.setpos(-80, -150)
     aTurtle.pendown()
     aTurtle.setheading(70)
     for cmd in instrucciones:
         if cmd == 'F':
             aTurtle.forward(distancia)
         elif cmd == '-':
             aTurtle.right(angulo)
         elif cmd == '+':
             aTurtle.left(angulo)
         elif cmd == '[':
             aTurtle.color("black")
             pila.append((aTurtle.xcor(),aTurtle.ycor(),aTurtle.heading()))
             aTurtle.color("brown")
             #aTurtle.left(angulo)
         elif cmd == ']':
             aTurtle.color("black")
             xcor, ycor, heading = pila.pop()
             aTurtle.penup()
             aTurtle.setpos(xcor,ycor)
             aTurtle.pendown()
             aTurtle.setheading(heading)
             #aTurtle.right(angulo)
def main():
 tracer(0, 0)
 inst = crearSistemaL(6, "X") # crea la cadena
 print(inst)
 t = Turtle() # crea la tortuga
 wn = Screen()
 t.up()
 t.back(200)
 t.down()
 t.speed(2)
 dibujarSistemaL(t, inst, 25, 3)
 done()
main()
