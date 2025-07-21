# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from numpy import *
from matplotlib.pyplot import *#el * es q importa todo de esa libreria
a=2+2
#comentar
print(a)
b=3-4
print (b)
c=3*4
print(c)
d=1/3
print(d)
#concatenar
print(a,b)

print ('El valor de un tercio es',d)
#saber de q tipo es una variable
print(type(a))
#potencia
f=2**3
print(f)

print(pi)

print(sqrt(33))


#numero e
print  (exp(1))

a=a+2
print(a)
a+=2
a=a*(-1)
print(a)
a*=-1
print(a)

b=a
print(a,b)

print(sin(0),cos(0),sin(pi),cos(pi))
#1.2246467991473532e-16 es el 0 maquina
#definir funcion, entre parentesis pongo las variables de las q depende la funcion
def f (x):
    return x**2+4

print(f(0),f(1))
y0=f(0)

#definimos otra funcion:
def sumaproducto (x,y):
    return x+y,x*y 
print(sumaproducto(2,3))

z=sumaproducto(4,5)
#se empieza a contar por un 0
print(z[0])
sumaz=z[0]
prodz=z[1]
(s,p)=sumaproducto(4,5)
print(s)
print(sumaproducto(4,5)[0])

for i in range (11):
    print(i)
    #que no empiece en 1
for i in range (1,11):
    print (i)
    #de dos en dos
for i in range (1,11,2):
    print(i)
for i in range (10,0,-1):
    print (i)
#definimos una funcion sumaveces

def sumasveces(a,n):
    suma=0 
    for i in range (n):
         suma=suma+a
         
    return suma
print(sumasveces(1,4))
#definimos otra funcion

def ecuacion2grado(a,b,c):
    r1=(-b+sqrt(b**2-4*a*c))/(2*a)
    r2=(-b-sqrt(b**2-4*a*c))/(2*a)
    print ('raices=',r1, 'y',r2)
    return (r1,r2)

print (ecuacion2grado(1,-1,-1))

def ecuacion2grado_bis(a,b,c):
    if a==0:
        r=-c/b 
        print('raiz=',r)
        return r
    else:
        r1=(-b+sqrt(b**2-4*a*c))/(2*a)
        r2=(-b-sqrt(b**2-4*a*c))/(2*a)
        print ('raices=',r1, 'y',r2)
        return (r1,r2)

print (ecuacion2grado_bis(1,-1,-1))

#dibujamos graficas
#importamos libreria
x=linspace(0,10,11)#para un eje de coord, va de 0 a 10 y dibuja 11 puntos, le puedo poner mas para q salga mejor pq los 11 puntos se uniran con rectas
print(x)
y=x
figure()#para inicializar el dibujador
plot(x,y)#para dibujar le paso el eje x y el y

figure()
x=linspace (0,pi)#si no pongo cts puntos pone 100puntos
y=sin(x)
plot(x,y)

x1=linspace(0,pi,10)
y1=sin(x1)
figure()#cada vez q pongo figure hace una nueva, si no lo pone pues dibuja todas las q le ponga en el mismo
plot(x1,y1,'o') 
figure()
plot(x1,y1,'o-')
plot(x1,y1,'*-')
plot(x1,y1,'b-')#lo pone rojo
plot(x1,y1,'k-')#lo pone negro, buscalo en google las demas
xlabel('Eje x')
ylabel('Eje y')
title ('holamundo')

figure()
x=linspace(0,pi,200)
y=exp(x)*sin(10*x)
plot(x,y,'ro-',x,x,'o')#podria hacer debajo plot(x,x,'o') es lo mismo pero es es mas rapido
plot(x,0*x,'k')#y no plot(x,0)pq x tiene esun array de dimension 200, y  0 es un array de dim 1
plot(x,y,'ro-',x,x,'o',x,0*x,'k')#lo va detectando por pares
















