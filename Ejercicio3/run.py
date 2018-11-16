from mipaquete.modelo import *
#p=PersonaEquipo("hola")
f= Futbolista("jose")
#f.entrenar()

m=Medico("luis")
#m.entrenar()

p=Presidente("juan")
#p.entrenar()

e=Entrenador("Julio")
#e.entrenar()

lista=[f,m,p,e]
for l in lista:
	l.entrenar()


