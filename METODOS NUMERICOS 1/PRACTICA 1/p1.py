# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:08:48 2023

@author: Msi
"""

from numpy import *
from matplotlib.pyplot import *

print('EJERCICIO 1')
def sumaveces(a,n):
    suma=0
    for i in range (1,n+1) :
        suma=suma+a
    return suma
print (sumaveces(4,9))

def sumaveces2(a,n):
    suma=0
    i=1
    while(i<=n):
        suma=suma+a
        i+=1
    return suma
print (sumaveces2(1,3))

print('EJERCICIO 2')
def epsilon():
    x=1
    while(1<1+x):
        x=x/2 #lo q quiero es ir reduciendo el x para ver ese epsilon q es muy chico, para ello lo voy reduciendo diviendoilo por 2, pero podria ahberlo reducido diviendolo por 3 por ej, da igual, mientras q lo reduzca

    return 2*x#para q sea el anterior ya que necesito el minimo, por ello el anterior si verifica que pertenece al conj ya que 1+x>1 por tanto pertenece al conj y es el mas pequeño q perte al conj y empieza en 1 pq da veri 1+x>1 y al final quiero el minimo y el minimo es el menor pero q pertenece al conjunto, no resto pq me qdara negativo, asiq mejor lo voy reduciendo con divisiones 

eps=epsilon()
print(eps)
print (1+eps>1)
    
print('EJERCICIO 3')

figure()#1 inicio con figure
x=linspace(-2,2,100)#eje x con linspace
y=x-exp(-x)#eje y defiendolo con la f
plot(x,y)#plot
plot(x,0*x,'k') 
 
print('EJERCICIO 4')

def aproxe(n):
    aprox=(1+1/n)**n #potencia
    error=abs(aprox-exp(1))#error siempre en vabs,asi se calcu el error absoluto
    print ('n=',n,'aproxe=',aprox,'error=',error)
    return aprox,error
aproxe(10)
aproxe(100)
aproxe(1000)
   
    
print('EJERCICIO 5') 

def sumaparcial(n):
    suma=0
    for i in range (1,n+1):#el primer parametro siempre lo inluye y el segundo no lo incluye
        suma=suma+1/sqrt(i)
    print ('n=',n,'suma=',suma)
    return suma
sumaparcial(10)
sumaparcial(100)
sumaparcial(1000)    
#Observar que la serie es divergente: LA SERIE ES DIVERGENTE PQ CONFORME AUMENTO EL N
# MAS Y MAS GRANDE SE HACE, LO PODEMOS OBSERVAR CON LAS TRES LLAMADAS A SUMAPARCIAL REALIZADAS ENCIMA

n=0
while(sumaparcial(n)<50):
    n=n+1
print(' para n=' , n ,  'la suma parcial es mayor que 50')
    
#clase 
#n=500
#while(sumaparcial(n)<50):
#   n+=1
#print('La suma parcial es mayor que 50')
print('EJERCICIO 6') 

##no lo puedes hacer con x=linspace(1,100,100)
## y=sumaparcial(x) pq ese x esta en float pq el linspace lo divide en puntos q son float y cada x es un float y tu no le puedes meter un float por parametro a lalllamada de una func 
##guay lo de la relacion de x e y pq en y metes el eje x xon una f q tu defines donde tu es el eje x
figure()#para q no nos lo pinte sobre la grafica de antes

for n in range (1,101):
   # figure()
    plot (n,sumaparcial(n), 'bo') 
    #usa pUNTO GORDO 'bo' PARA Q SE VEA LA GRAFICA, pq no esta unida con lineas como estaba en las anteriores q hice, debido a q ahi usaba linsapce y tal
    #aqui estoy pintando un punto por cada ite, de hecho si tras la palabra for le pongo un figure, solo vemos un punto en cada iteracion ya q en cada iteracion el dibujdaor se esta poniendo en blanco y pinta el punto correspondiente,
    #aqui no estoy dibujando una grafica, sino q punto a punto estroy construyendola a pelo, en cada ite pongo un punto en la grafica y asi tras todas las ite obtengo la grafica
    #plot construye la grafica con el eje x y el eje y

print('EJERCICIO 7')  
def sumaparcial2(n):
    suma=0
    for i in range(1,n+1):
        suma=suma+(1/(i*(i+1)))
    error=abs(suma-1)
    print('n=',n,'Sn=',suma,'error=',error)
    return suma,error
print(sumaparcial2(10))
print(sumaparcial2(10**7))
print(sumaparcial2(10**8))


    
def sumaparcial3(n):
    
    suma=(1-(1/(n+1)))
    error=abs(suma-1)
    print('n=',n,'Sn=',suma,'error=',error)
    return suma,error
print(sumaparcial3(10))
print(sumaparcial3(10**7))
print(sumaparcial3(10**8))    
##10**7 pq no se puede meter float q eso seria con 10^7 asi q meto int con 10**7
## y print sal elos dos si no solo sale 1 yno la dupola del return

print('EJERCICIO 8')
def factorial(k):
    if k==0:
        return 1 
    else:
        fact=1
        for i in range(2,k+1):
            fact=fact*i
    return fact
def sumaparcial4(n):
    suma=0
    for i in range(0,n+1): #el primer parametro siempre lo inluye y el segundo no lo incluye
        suma=suma+(1/factorial(i))
    error=abs(suma-exp(1))
    print('n=',n,'Sn=',suma,'error=',error)
    return suma,error
print(sumaparcial4(100))



print('EJERCICIO 9')

def sumaparcial5(n,x):
    suma=0
    for i in range(0,n+1): #el primer parametro siempre lo inluye y el segundo no lo incluye
        suma=suma+(x**i/factorial(i))
    error=abs(suma-exp(x))
    print('n=',n,'Sn=',suma,'error=',error)
    return suma,error
print(sumaparcial5(10**2,0))
print(sumaparcial5(10**2,1))
print(sumaparcial5(10**2,5))
print(sumaparcial5(10**2,10))
print(sumaparcial5(10**2,-1))
print(sumaparcial5(10**2,-5))
print(sumaparcial5(10**2,-10))

print('EJERCICIO 10')

def sumamedia(x):#la primera pos de un array es 0
    suma=0
    n=len(x)
    for i in range(n):#va de 0 a n-1
        suma=suma+x[i]
    media=suma/n
    return suma,media
x=[1,2,3]
print(sumamedia(x))
print(sum(x), mean(x))