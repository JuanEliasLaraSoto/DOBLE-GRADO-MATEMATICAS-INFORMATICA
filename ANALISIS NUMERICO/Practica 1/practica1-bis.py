# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 23:30:03 2025

@author: Msi
"""
import math
from pylab import *
from time import perf_counter
import algoritmos

def f(t,y):
    return -y+2*sin(t)

def f_exacta(t):
    return (pi+1)*exp(-t)+sin(t)-cos(t)

(t,y)=algoritmos.euler(0,10,f,50,pi)

ye = f_exacta(t)


plot(t, y, "-*")

# Calculo del error cometido
error = max(abs(y-ye))
print('Error: ' + str(error))





(t,y)=algoritmos.heun(0,10,f,50,pi)

ye = f_exacta(t)


plot(t, y, "-*")

# Calculo del error cometido
error = max(abs(y-ye))
print('Error: ' + str(error))



(t,y)=algoritmos.puntomedio(0,10,f,50,pi)

ye = f_exacta(t)


plot(t, y, "-*")

# Calculo del error cometido
error = max(abs(y-ye))
print('Error: ' + str(error))


(t,y)=algoritmos.RK4(0,10,f,50,pi)

ye = f_exacta(t)


plot(t, y, "-*")

# Calculo del error cometido
error = max(abs(y-ye))
print('Error: ' + str(error))



def f4(t,y):
    """funcion q define el sistema diferencial"""
    f1=3*y[0]-2*y[1]
    f2=-y[0]+3*y[1]-2*y[2]
    f3=-y[1]+3*y[2]
    return array([f1,f2,f3])



def solucion_analitica(t):
    f1=(-1/4) * exp(5*t) + (3/2) * exp(3*t) - (1/4) * exp(t)
    f2=(1/4) * exp(5*t) - (1/4) * exp(t)
    f3=(-1/8) * exp(5*t) - (3/4) * exp(3*t) - (1/8) * exp(t)
    return array([f1,f2,f3])



(t,y)=algoritmos.eulersis(0,1,f4,50,array([1,0,-1]))

ye = solucion_analitica(t)



# Calculo del error cometido
error = max(abs(y[0,:]-ye[0,:]))
print('Error: ' + str(error))

error = max(abs(y[1,:]-ye[1,:]))
print('Error: ' + str(error))
error = max(abs(y[2,:]-ye[2,:]))
print('Error: ' + str(error))


(t,y)=algoritmos.heunsis(0,1,f4,50,array([1,0,-1]))

ye = solucion_analitica(t)



# Calculo del error cometido
error = max(abs(y[0,:]-ye[0,:]))
print('Error: ' + str(error))

error = max(abs(y[1,:]-ye[1,:]))
print('Error: ' + str(error))
error = max(abs(y[2,:]-ye[2,:]))
print('Error: ' + str(error))

(t,y)=algoritmos.puntomediosis(0,1,f4,50,array([1,0,-1]))

ye = solucion_analitica(t)



# Calculo del error cometido
error = max(abs(y[0,:]-ye[0,:]))
print('Error: ' + str(error))

error = max(abs(y[1,:]-ye[1,:]))
print('Error: ' + str(error))
error = max(abs(y[2,:]-ye[2,:]))
print('Error: ' + str(error))





(t,y)=algoritmos.rk4sis(0,1,f4,50,array([1,0,-1]))

ye = solucion_analitica(t)



# Calculo del error cometido
error = max(abs(y[0,:]-ye[0,:]))
print('Error: ' + str(error))

error = max(abs(y[1,:]-ye[1,:]))
print('Error: ' + str(error))
error = max(abs(y[2,:]-ye[2,:]))
print('Error: ' + str(error))