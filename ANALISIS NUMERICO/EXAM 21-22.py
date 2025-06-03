# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 18:57:34 2025

@author: Msi
"""


from pylab import *
from time import perf_counter
print('EXAM JUNE 21-22- ej1')

def fun(t,y):
    return array ([y[1],-15*y[0]+3*y[1]])



def AB4_sistema(a, b, fun, N, y0):
    y = zeros((len(y0), N+1))
    t = zeros(N+1)
    f = zeros((len(y0), N+1))
    t[0] = a
    h = (b - a) / float(N)
    y[:,0] = y0
    f[:,0] = fun(a, y[:,0])

    for k in range(4):##cambia segun el orden, tiene q ser de al menos 1 menos
        t[k+1] = t[k] + h
        k1 = fun(t[k],y[:,k])
        k2 = fun(t[k] + h/2, y[:,k] + h/2*k1)
        k3 = fun(t[k] + h/2, y[:,k] + h/2*k2)
        k4 = fun(t[k+1], y[:,k] + h*k3)
        y[:,k+1] = y[:,k] + h/6*(k1 + 2*k2 + 2*k3 + k4)
        f[:,k+1] = fun(t[k+1], y[:,k+1])

    for k in range(4, N):##cambia el 3
        y[:,k+1] = y[:,k] + h/24.0 * (55.0 * f[:,k] - 59.0 * f[:,k-1] + 37.0 * f[:, k-2] - 9*f[:,k-3])
        t[k+1] = t[k] + h
        f[:,k+1] = fun(t[k+1], y[:,k+1])

    return (t, y)



y0 = array([1.0, 0])
a = 0.0
b = 20.0
malla = [200]


figure('EJERCICIO 1')

for i in range(1):
    N = malla[i]
    tini = perf_counter()
    (t, Y) = AB4_sistema(a, b, fun, N, y0)
    tfin = perf_counter()
    
    subplot(121)
    plot(t,Y[0],t,Y[1])
    xlabel('t')
    ylabel('x,y')
    legend(['Presas','Depredadores'])
    
    subplot(122)
    plot(Y[0],Y[1])
    xlabel('presas')
    ylabel('depredadores')
    legend(['trayectoria'])
    
    print('\nN = ' + str(N))
    print('Paso de malla: ' + str((b-a)/N))
    print('Tiempo CPU: ' + str(tfin-tini))
   

leyenda=(['N = ' + str(N) for N in malla])
subplot(121)
legend(leyenda)
subplot(122)
legend(leyenda)