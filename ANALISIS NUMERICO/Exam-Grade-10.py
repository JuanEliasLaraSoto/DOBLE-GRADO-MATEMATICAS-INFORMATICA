# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 12:33:34 2025

@author: Usuario_UMA
"""

from pylab import *

####################################################################################################################################

# EJERCICIO 1

####################################################################################################################################

print('EXÁMEN DE JUAN ELIAS LARA SOTO - ANALISIS NUMERICO - DOBLE GRADO MATEMÁTICAS-INFORMÁTICA\n')

print('EJERCICIO 1')

def butcher(a, b, f, N, y0):
    h = (b - a)/N
    t = zeros(N+1)
    y = zeros(N+1)
    t[0] = a 
    y[0] = y0
    for k in range(N):
       tk1=t[k]
       yk1=y[k]
       tk2=t[k]+0.5*h
       yk2=y[k]+h*0.5*f(tk1,yk1)
       tk3=t[k]+h 
       yk3=y[k]-h*f(tk1,yk1)+2*h*f(tk2,yk2)
       y[k+1]=y[k]+h*((1/6)*f(tk1,yk1)+(2/3)*f(tk2,yk2)+(1/6)*f(tk3,yk3))
       t[k+1] = t[k] + h
    return (t, y)


def f(t, y):
    return y+abs(t)

def exacta(t):
    return (1+t+exp(t+1))*(t<=0)+(-(1+t)+2*exp(t)+exp(t+1))*(t>0)

figure("EJERCICIO 1")


# Datos del problema
a = -1.  # extremo inferior del intervalo
b = 1. # extremo superior del intervalo
y0 = 1. # condicion inicial
malla=[20,40,80,160]


for N in malla:

    (t, y) = butcher(a, b, f, N, y0)
    
    ye = exacta(t)
    
    
    if(N==160):
        plot(t, y, "-*y")
    
    # Calculo del error cometido
    error = max(abs(y-ye))
    
    # Resultados
    print('-----')
    print('Error: ' + str(error))
    
    if N != malla[0]:
        print("Cociente de errores: " + str(error_old/error))
    
    print('Paso de malla: ' + str((b-a)/N)+' (N= '+str(N)+')')
    print('-----')
    
    error_old = error

plot(t, ye, 'k') # dibuja la solucion exacta
xlabel('t')
ylabel('y')
leyenda = ['N=' + str(160)]
leyenda.append('exacta')
legend(leyenda)
grid(True)

print('Respondemos a la pregunta: ¿cuál parece ser el orden del método?\n')
print('El orden del método se ha estimado observando cómo decrece el error al aplicar el mismo método con distintos tamaños de paso.Para ello se ha utilizado el cociente de errores, que permite comparar directamente el error entre simulaciones con pasos sucesivos.En este caso, los cocientes obtenidos se aproximan a 8, lo cual indica que al reducir el paso a la mitad, el error se reduce aproximadamente a una octava parte. Esta disminución es propia de un método de tercer orden. Por tanto, los resultados numéricos, junto con el análisis del cociente de errores, permiten concluir que el método es de orden tres.')

####################################################################################################################################

# EJERCICIO 2

####################################################################################################################################

print('\nEJERCICIO 2')



def butcher_sis(a, b, f, N, y0):
    h = (b - a)/N
    t = zeros(N+1)
    y = zeros([len(y0),N+1])
    t[0] = a 
    y[:,0] = y0
    for k in range(N):
       tk1=t[k]
       yk1=y[:,k]
       tk2=t[k]+0.5*h
       yk2=y[:,k]+h*0.5*f(tk1,yk1)
       tk3=t[k]+h 
       yk3=y[:,k]-h*f(tk1,yk1)+2*h*f(tk2,yk2)
       y[:,k+1]=y[:,k]+h*((1/6)*f(tk1,yk1)+(2/3)*f(tk2,yk2)+(1/6)*f(tk3,yk3))
       t[k+1] = t[k] + h
    return (t, y)




#Empezamos dando los datos del problema de Cauchy
a=0
b=10
y0= array([1,0,0])
N=500

def f(t,y):
    return array([y[1],y[2],-t*y[1]+cos(y[0])])


figure('EJERCICIO 2')
(t,y)= butcher_sis(a,b,f,N,y0)
plot(t, y[0], '-r')
xlabel('t')
ylabel('y')
leyenda= ['N='+str(N)]
legend(leyenda)
grid(True)