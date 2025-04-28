# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 01:34:14 2025

@author: Msi
"""

from pylab import *
from time import perf_counter

def f(t, y):
    """Funcion que define la ecuacion diferencial"""
    return 0.5*(t**2 - y)

def exacta(t):
    """Solucion exacta del problema de valor inicial"""
    return t**2 - 4*t + 8 - 7.*exp(-0.5*t)

def euler(a, b, fun, N, y0):
    """Implementacion del metodo de Euler en el intervalo [a, b]
    usando N particiones y condicion inicial y0"""
    
    h = (b-a)/N # paso de malla
    t = zeros(N+1) # inicializacion del vector de nodos
    y = zeros(N+1) # inicializacion del vector de resultados
    t[0] = a # nodo inicial
    y[0] = y0 # valor inicial

    # Metodo de Euler
    for k in range(N):
        y[k+1] = y[k]+h*fun(t[k], y[k])
        t[k+1] = t[k]+h
    
    return (t, y)

figure("EULER 1A")


# Datos del problema
a = 0.  # extremo inferior del intervalo
b = 20. # extremo superior del intervalo
y0 = 0. # condicion inicial
malla=[10,20,40,80,160]


for N in malla:
    tini = perf_counter()

    (t, y) = euler(a, b, f, N, y0)
    
    ye = exacta(t)
    
    tfin = perf_counter()
    
    plot(t, y, "-*")
    
    # Calculo del error cometido
    error = max(abs(y-ye))
    
    # Resultados
    print('-----')
    print('Tiempo CPU: ' + str(tfin-tini))
    print('Error: ' + str(error))
    
    if N != malla[0]:
        print("Cociente de errores: " + str(error/error_old))
    
    print('Paso de malla: ' + str((b-a)/N))
    print('-----')
    
    error_old = error

plot(t, ye, 'k') # dibuja la solucion exacta
xlabel('t')
ylabel('y')
leyenda = ['N=' + str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)
grid(True)



#ejercicio 1b
figure("EULER 1B")
def f(t, y):
    return 6-y/10

def exacta(t):
    return 60*(1-exp(-t/10))
# Datos del problema
a = 0.  # extremo inferior del intervalo
b = 20. # extremo superior del intervalo
y0 = 0. # condicion inicial
malla=[10,20,40,80,160]


for N in malla:
    tini = perf_counter()

    (t, y) = euler(a, b, f, N, y0)
    
    ye = exacta(t)
    
    tfin = perf_counter()
    
    plot(t, y, "-*")
    
    # Calculo del error cometido
    error = max(abs(y-ye))
    
    # Resultados
    print('-----')
    print('Tiempo CPU: ' + str(tfin-tini))
    print('Error: ' + str(error))
    
    if N != malla[0]:
        print("Cociente de errores: " + str(error/error_old))
    
    print('Paso de malla: ' + str((b-a)/N))
    print('-----')
    
    error_old = error

plot(t, ye, 'k') # dibuja la solucion exacta
xlabel('t')
ylabel('y')
leyenda = ['N=' + str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)
grid(True)
    
#EJERCICIO 2

def taylor2(a, b, f1, f2, N, y0):
    h = (b - a)/N
    t = zeros(N+1)
    y = zeros(N+1)
    t[0] = a
    y[0] = y0
    for k in range(N):
        y[k+1] = y[k] + h*f1(t[k], y[k]) + h**2*f2(t[k], y[k])/2
        t[k+1] = t[k] + h
    return (t, y)

def taylor3(a, b, f1, f2, f3, N, y0):
    h = (b - a)/N
    t = zeros(N+1)
    y = zeros(N+1)
    t[0] = a
    y[0] = y0
    for k in range(N):
        y[k+1] = y[k] + h*f1(t[k], y[k]) + h**2*(f2(t[k], y[k]))/2 + h**3*f3(t[k], y[k])/6
        t[k+1] = t[k] + h
    return (t, y)
def df(t, y):
    return t - 0.25*(t**2 - y)

def dfdf(t,y):
    return 1 - 1/2*t + 1/8*t**2 - 1/8*y


def f(t, y):
    """Funcion que define la ecuacion diferencial"""
    return 0.5*(t**2 - y)

def exacta(t):
    """Solucion exacta del problema de valor inicial"""
    return t**2 - 4*t + 8 - 7.*exp(-0.5*t)

figure("TAYLOR2")
# Datos del problema
a = 0.  # extremo inferior del intervalo
b = 20. # extremo superior del intervalo
y0 = 0. # condicion inicial
malla=[10,20,40,80,160]


for N in malla:
    tini = perf_counter()

    (t, y) = taylor2(a, b, f,df, N, y0)
    
    ye = exacta(t)
    
    tfin = perf_counter()
    
    plot(t, y, "-*")
    
    # Calculo del error cometido
    error = max(abs(y-ye))
    
    # Resultados
    print('-----')
    print('Tiempo CPU: ' + str(tfin-tini))
    print('Error: ' + str(error))
    
    if N != malla[0]:
        print("Cociente de errores: " + str(error/error_old))
    
    print('Paso de malla: ' + str((b-a)/N))
    print('-----')
    
    error_old = error
#TAYLOR 2:los errores tienen q tender a 1/4 si haces error2n/errorn y 4 si hago errorn/error2n, pq el metodo es de orden 2
plot(t, ye, 'k') # dibuja la solucion exacta
xlabel('t')
ylabel('y')
leyenda = ['N=' + str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)
grid(True)


#ahora con taylor3

def f(t, y):
    """Funcion que define la ecuacion diferencial"""
    return 0.5*(t**2 - y)

def exacta(t):
    """Solucion exacta del problema de valor inicial"""
    return t**2 - 4*t + 8 - 7.*exp(-0.5*t)

figure("TAYLOR3")
# Datos del problema
a = 0.  # extremo inferior del intervalo
b = 20. # extremo superior del intervalo
y0 = 0. # condicion inicial
malla=[10,20,40,80,160]


for N in malla:
    tini = perf_counter()

    (t, y) = taylor3(a, b, f,df,dfdf, N, y0)
    
    ye = exacta(t)
    
    tfin = perf_counter()
    
    plot(t, y, "-*")
    
    # Calculo del error cometido
    error = max(abs(y-ye))
    
    # Resultados
    print('-----')
    print('Tiempo CPU: ' + str(tfin-tini))
    print('Error: ' + str(error))
    
    if N != malla[0]:
        print("Cociente de errores: " + str(error/error_old))
    
    print('Paso de malla: ' + str((b-a)/N))
    print('-----')
    
    error_old = error
#TAYLOR3:los errores tienen q tender a 1/8 si haces error2n/errorn y 8 si hago errorn/error2n, pq el metodo es de orden 3
plot(t, ye, 'k') # dibuja la solucion exacta
xlabel('t')
ylabel('y')
leyenda = ['N=' + str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)
grid(True)

# EJERCICIO 3

####################################################################################################################################

def heun(a, b, fun, N, y0):
    h = (b - a)/N
    t = zeros(N+1)
    y = zeros(N+1)
    t[0] = a
    y[0] = y0
    for k in range(N):
        t[k+1] = t[k] + h
        ff = fun(t[k], y[k]) # para evaluar fun menos veces
        yy = y[k] + h*ff
        y[k+1] = y[k] + 0.5 * h * (ff + fun(t[k+1], yy))
    return (t, y)

def RK4(a, b, fun, N, y0):
    h = (b - a)/N
    t = zeros(N+1)
    y = zeros(N+1)
    t[0] = a
    y[0] = y0
    for k in range(N):
        t[k+1] = t[k] + h
        k1 = fun(t[k], y[k])
        k2 = fun(t[k] + h/2, y[k] + h/2 * k1)
        k3 = fun(t[k] + h/2, y[k] + h/2 * k2)
        k4 = fun(t[k+1], y[k] + h * k3)
        y[k+1] = y[k] + h/6 * (k1 + 2*k2 + 2*k3 + k4)
    return (t, y)

def puntomedio(a, b, fun, N, y0):
    h = (b - a)/N
    t = zeros(N+1)
    y = zeros(N+1)
    t[0] = a
    y[0] = y0
    for k in range(N):
        t[k+1] = t[k] + h
        auxY = y[k] + h/2*fun(t[k], y[k])
        y[k+1] = y[k] + h*fun(t[k] + h/2, auxY)
    return (t, y)

def f(t, y):
    """Funcion que define la ecuacion diferencial"""
    return 0.5*(t**2 - y)

def exacta(t):
    """Solucion exacta del problema de valor inicial"""
    return t**2 - 4*t + 8 - 7.*exp(-0.5*t)

figure("HEUN")
# Datos del problema
a = 0.  # extremo inferior del intervalo
b = 20. # extremo superior del intervalo
y0 = 0. # condicion inicial
malla=[10,20,40,80,160]


for N in malla:
    tini = perf_counter()

    (t, y) = RK4(a, b, f, N, y0)
    
    ye = exacta(t)
    
    tfin = perf_counter()
    
    plot(t, y, "-*")
    
    # Calculo del error cometido
    error = max(abs(y-ye))
    
    # Resultados
    print('-----')
    print('Tiempo CPU: ' + str(tfin-tini))
    print('Error: ' + str(error))
    
    if N != malla[0]:
        print("Cociente de errores: " + str(error/error_old))
    
    print('Paso de malla: ' + str((b-a)/N))
    print('-----')
    
    error_old = error
plot(t, ye, 'k') # dibuja la solucion exacta
xlabel('t')
ylabel('y')
leyenda = ['N=' + str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)
grid(True)


def f(t, y):
    """Funcion que define la ecuacion diferencial"""
    return 0.5*(t**2 - y)

def exacta(t):
    """Solucion exacta del problema de valor inicial"""
    return t**2 - 4*t + 8 - 7.*exp(-0.5*t)

figure("RK4")
# Datos del problema
a = 0.  # extremo inferior del intervalo
b = 20. # extremo superior del intervalo
y0 = 0. # condicion inicial
malla=[10,20,40,80,160]


for N in malla:
    tini = perf_counter()

    (t, y) = heun(a, b, f, N, y0)
    
    ye = exacta(t)
    
    tfin = perf_counter()
    
    plot(t, y, "-*")
    
    # Calculo del error cometido
    error = max(abs(y-ye))
    
    # Resultados
    print('-----')
    print('Tiempo CPU: ' + str(tfin-tini))
    print('Error: ' + str(error))
    
    if N != malla[0]:
        print("Cociente de errores: " + str(error/error_old))
    
    print('Paso de malla: ' + str((b-a)/N))
    print('-----')
    
    error_old = error
    
plot(t, ye, 'k') # dibuja la solucion exacta
xlabel('t')
ylabel('y')
leyenda = ['N=' + str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)
grid(True)  

def f(t, y):
    """Funcion que define la ecuacion diferencial"""
    return 0.5*(t**2 - y)

def exacta(t):
    """Solucion exacta del problema de valor inicial"""
    return t**2 - 4*t + 8 - 7.*exp(-0.5*t)

figure("PUNTOMEDIO")
# Datos del problema
a = 0.  # extremo inferior del intervalo
b = 20. # extremo superior del intervalo
y0 = 0. # condicion inicial
malla=[10,20,40,80,160]


for N in malla:
    tini = perf_counter()

    (t, y) = puntomedio(a, b, f, N, y0)
    
    ye = exacta(t)
    
    tfin = perf_counter()
    
    plot(t, y, "-*")
    
    # Calculo del error cometido
    error = max(abs(y-ye))
    
    # Resultados
    print('-----')
    print('Tiempo CPU: ' + str(tfin-tini))
    print('Error: ' + str(error))
    
    if N != malla[0]:
        print("Cociente de errores: " + str(error/error_old))
    
    print('Paso de malla: ' + str((b-a)/N))
    print('-----')
    
    error_old = error

plot(t, ye, 'k') # dibuja la solucion exacta
xlabel('t')
ylabel('y')
leyenda = ['N=' + str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)
grid(True)

#EJERCICIO 4
# Datos del problema
a = 0. # extremo inferior del intervalo
b = 20. # extremo superior del intervalo
y0 = array([80,30]) # condicion inicial
malla = [20, 40, 80, 160, 320, 640]
figure("EULERSIS")

def eulersis(a, b, fun, N, y0):
    """Implementacion del metodo de Euler en el intervalo [a, b]
    usando N particiones y condicion inicial y0"""
    
    h = (b-a)/N # paso de malla
    t = zeros(N+1) # inicializacion del vector de nodos
    y = zeros([len(y0),N+1]) # inicializacion del vector de resultados, con y0 saco mas facil num de filas q es el num de incognitas q tengo,
    t[0] = a # nodo inicial
    y[:,0] = y0 # valor inicial

    # Metodo de Euler
    for k in range(N):
        y[:,k+1] = y[:,k]+h*fun(t[k], y[:,k])
        t[k+1] = t[k]+h
    
    return (t, y)

def f4(t,y):
    """funcion q define el sistema diferencial"""
    f1=0.25*y[0]-0.01*y[0]*y[1]
    f2=-y[1]+0.01*y[0]*y[1]
    return array([f1,f2])

for N in malla:
    
    (t, y) = eulersis(a, b, f4, N, y0) # llamada al metodo de Euler para sistemas
    
    # Dibujamos las soluciones
    subplot (121)
    plot(t,y[0,:],t,y[1,:])
    
    subplot (122)
    plot(y[0,:],y[1,:])
    
subplot (121)
plot(t,y[0,:],t,y[1,:])
xlabel('t')
ylabel('x,y')
legend(['Presa','Depredador'])

subplot (122)
plot(y[0,:],y[1,:])
xlabel('x')
ylabel('y')
leyenda = ['N=' + str(N) for N in malla]
legend(leyenda)
grid(False)


#Para metodo PM
figure("puntomediosis")

def puntomediosis(a, b, fun, N, y0): #a y b extremos izq der del intervalo, es decir, to y tN, fun define la ecuacion diferencial que queremos resolver, la llamamos fun e vez de f para que sea programa general, yo le doy el nombre de la funcion que define la ecuacion diferencial, para aplicar a mi funcion cambio el tercer elemento que define Euler, N numero subintervalos de la particion, y0 condicion inicial
    """Implementacion del metodo de Euler en el intervalo [a, b]
    usando N particiones y condicion inicial y0"""
    
    h = (b-a)/N # paso de malla
    t = zeros(N+1) # inicializacion del vector de nodos #arrary de tiempos
    y = zeros([len(y0),N+1]) # inicializacion del vector de resultados #array de valores que voy obteniendo
    t[0] = a # nodo inicial #aqui ponemos condicion inicial, el tiempo inicial es a
    y[:,0] = y0 # valor inicial

    # Metodo de Euler #bucle del metodo, el k toma valores entre 0 y N-1
    for k in range(N):
        ykmedio= y[:,k] + h/2 *fun(t[k],y[:,k])
        y[:,k+1] = y[:,k]+h*fun(t[k]+h/2, ykmedio)
        t[k+1] = t[k]+h
    
    return (t, y) #el programa que recibe 5 datos devuelve dos arrays de tamaño N-1


for N in malla:
    
    (t, y) = puntomediosis(a, b, f4, N, y0) # llamada al metodo de Euler para sistemas
    
    # Dibujamos las soluciones
    subplot (121)
    plot(t,y[0,:],t,y[1,:])
    
    subplot (122)
    plot(y[0,:],y[1,:])
    
subplot (121)
plot(t,y[0,:],t,y[1,:])
xlabel('t')
ylabel('x,y')
legend(['Presa','Depredador'])

subplot (122)
plot(y[0,:],y[1,:])
xlabel('x')
ylabel('y')
leyenda = ['N=' + str(N) for N in malla]
legend(leyenda)
grid(False)


#Para el metodo de Heun
figure("heunsis")

def heunsis(a,b,fun,N,y0):
    h = (b-a)/N
    t = zeros(N+1)
    y = zeros([len(y0),N+1])
    t[0] = a
    y[:,0] = y0 


    for k in range(N): 
        t[k+1] = t[k]+h
        y[:,k+1] = y[:,k]+(h/2)*(fun(t[k], y[:,k])+fun(t[k+1], y[:,k]+h*fun(t[k],y[:,k])))
    return (t, y)    
    



for N in malla:
    
    (t, y) = heunsis(a, b, f4, N, y0) # llamada al metodo de Euler para sistemas
    
    # Dibujamos las soluciones
    subplot (121)
    plot(t,y[0,:],t,y[1,:])
    
    subplot (122)
    plot(y[0,:],y[1,:])
    
subplot (121)
plot(t,y[0,:],t,y[1,:])
xlabel('t')
ylabel('x,y')
legend(['Presa','Depredador'])

subplot (122)
plot(y[0,:],y[1,:])
xlabel('x')
ylabel('y')
leyenda = ['N=' + str(N) for N in malla]
legend(leyenda)
grid(False)


#Para el metodo RK4
figure("rk4sis")
def rk4sis(a,b,fun,N,y0):
    h = (b-a)/N
    t = zeros(N+1)
    y = zeros([len(y0),N+1])
    t[0] = a
    y[:,0] = y0 

    for k in range(N):
        t[k+1] = t[k]+h
        k1=fun(t[k],y[:,k])
        k2=fun(t[k]+h/2,y[:,k]+k1*h/2)
        k3=fun(t[k]+h/2,y[:,k]+k2*h/2)
        k4=fun(t[k+1],y[:,k]+h*k3)
        y[:,k+1] = y[:,k]+(h/6)*(k1+2*k2+2*k3+k4)
    return (t, y) 



for N in malla:
    
    (t, y) = rk4sis(a, b, f4, N, y0) # llamada al metodo de Euler para sistemas
    
    # Dibujamos las soluciones
    subplot (121)
    plot(t,y[0,:],t,y[1,:])
    
    subplot (122)
    plot(y[0,:],y[1,:])
    

subplot (121)
plot(t,y[0,:],t,y[1,:])
xlabel('t')
ylabel('x,y')
legend(['Presa','Depredador'])

subplot (122)
plot(y[0,:],y[1,:])
xlabel('x')
ylabel('y')
leyenda = ['N=' + str(N) for N in malla]
legend(leyenda)
grid(False)

print('\n Ejercicio 5 \n')
#Hago asi el 5 pq me piden graficar las y y la ye(exacta)(asi q cambia un poco pq tengo q hallar ye y tal
#En el 4 mwe pedia grafica otra cosa

def f(t, y):
    """Funcion que define el sistema diferencial"""
    f1 = y[1]
    f2 = -20*y[1]-101*y[0]
    return array([f1, f2])

def exacta(t):
    """Solucion exacta del problema de valor inicial"""
    return exp(-10*t)*cos(t)

# Datos del problema
a = 0. # extremo inferior del intervalo
b = 7. # extremo superior del intervalo
y0 = array([1,-10]) # condicion inicial

malla = [20, 40, 80, 160, 320, 640]

figure('Figura 5 (Euler)')

for N in malla:
    
    tini = perf_counter()
    
    (t, y) = eulersis(a, b, f, N, y0) # llamada al metodo de Euler para sistemas
    
    tfin = perf_counter()

    ye = exacta(t) # calculo de la solucion exacta
    
    # Dibujamos las soluciones
    plot(t, y[0,:], '-*') # dibuja la solucion aproximada
    
    # Calculo del error cometido
    error = max(abs(y[0,:]-ye))

    # Resultados
    print('-----')
    print('Tiempo CPU: ', tfin-tini)
    print('Error: ', error)
    if N != malla[0]:
        print('Cociente de errores: ', error/errorold) #hacemos e2N/eN en vez de eN/e2N
    print('Paso de malla: ', (b-a)/N)
    print('-----')
    
    errorold = error
    
plot(t, ye, 'k') # dibuja la solucion exacta
xlabel('t')
ylabel('y')
leyenda = ['N=' + str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)
grid(True)



figure('Figura 5 (Heun)')

for N in malla:
    
    tini = perf_counter()
    
    (t, y) = heunsis(a, b, f, N, y0) # llamada al metodo de Heun para sistemas
    
    tfin = perf_counter()

    ye = exacta(t) # calculo de la solucion exacta
    
    # Dibujamos las soluciones
    plot(t, y[0,:], '-*') # dibuja la solucion aproximada
    
    # Calculo del error cometido
    error = max(abs(y[0,:]-ye))

    # Resultados
    print('-----')
    print('Tiempo CPU: ', tfin-tini)
    print('Error: ', error)
    if N != malla[0]:
        print('Cociente de errores: ', error/errorold) #hacemos e2N/eN en vez de eN/e2N
    print('Paso de malla: ', (b-a)/N)
    print('-----')
    
    errorold = error
    
plot(t, ye, 'k') # dibuja la solucion exacta
xlabel('t')
ylabel('y')
leyenda = ['N=' + str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)
grid(True)



figure('Figura 5 (RK4)')

for N in malla:
    
    tini = perf_counter()
    
    (t, y) = rk4sis(a, b, f, N, y0) # llamada al metodo de RK4 para sistemas
    
    tfin = perf_counter()

    ye = exacta(t) # calculo de la solucion exacta
    
    # Dibujamos las soluciones
    plot(t, y[0,:], '-*') # dibuja la solucion aproximada
    
    # Calculo del error cometido
    error = max(abs(y[0,:]-ye))

    # Resultados
    print('-----')
    print('Tiempo CPU: ', tfin-tini)
    print('Error: ', error)
    if N != malla[0]:
        print('Cociente de errores: ', error/errorold) #hacemos e2N/eN en vez de eN/e2N
    print('Paso de malla: ', (b-a)/N)
    print('-----')
    
    errorold = error
    
plot(t, ye, 'k') # dibuja la solucion exacta
xlabel('t')
ylabel('y')
leyenda = ['N=' + str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)
grid(True)
####################################################################################################################################

# EJERCICIO 5

####################################################################################################################################

def f(t, Y):
    F1 = Y[1]
    F2 = -20*Y[1] - 101*Y[0]
    return array([F1, F2])

def exacta(t):
    return exp(-10*t)*cos(t)

a = 0.
b = 7.
malla = [20, 40, 80, 160, 320, 640]
y0 = array([1, -10])
k = len(malla)
errores = zeros(k)


for N in malla:
    
    tini = perf_counter()
    
    (t, y) = rk4sis(a, b, f, N, y0) # llamada al metodo de RK4 para sistemas
    
    tfin = perf_counter()

    ye = exacta(t) # calculo de la solucion exacta
    
    # Dibujamos las soluciones
    plot(t, y[0,:], '-*') # dibuja la solucion aproximada
    
    # Calculo del error cometido
    error = max(abs(y[0,:]-ye))

    # Resultados
    print('-----')
    print('Tiempo CPU: ', tfin-tini)
    print('Error: ', error)
    if N != malla[0]:
        print('Cociente de errores: ', error/errorold) #hacemos e2N/eN en vez de eN/e2N
    print('Paso de malla: ', (b-a)/N)
    print('-----')
    
    errorold = error
    
plot(t, ye, 'k') # dibuja la solucion exacta
xlabel('t')
ylabel('y')
leyenda = ['N=' + str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)
grid(True)

print('\n\n\n5. MÉTODO RK4')

for i in range(k):
    N = malla[i]
    tini = perf_counter()
    (t, Y) = rk4sis(a, b, F, N, Y0)
    tfin = perf_counter()
    ye = exacta(t)
    error = max(abs(Y[0,:] - ye))
    
    print('\nN = ' + str(N))
    print('Paso de malla: ' + str((b-a)/N))
    print('Tiempo CPU: ' + str(tfin-tini))
    print('Error: ' + str(error))
    
    plot(t, Y[0,:])  # Ahora solo se necesita pintar la primera componente de Y
   
plot(t, ye, 'k')
xlabel('t')
ylabel('x')
leyenda = ['N = ' + str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)
title('5. MÉTODO RK4')
show() # Hay anomalías para N = 20 (hay problemas de estabilidad; ya se verá en clase)

###############################################################################
#cd le meto cosas nuevas a rk4 hay ponerle normalmente numamxiter pq sino puede entrar en bucle inf, pero de todas formas en este caso no va a entrar en bucle inf y no hay q poner num max iter
#rk4 va a seguir para abajo
#whilez>0 y hago Y=columnstack y añado cada it de rk4 pq no me ehe creado una y de long +1 pq nose cuantas iteracioens voy a dar pq seguramente acabe antes pq quiero z>0
#hago esto pq a priori nose cuantas iteracioens voy a dar
print('Ejercicio 7-0')
figure('EJERCICIO 7-0')
print('este apartaado es para darnos cuenta q hay q hacer while z>=0 pq sino el rk4 sigue haciendo ite y me da alturas negativas(mira la graf de este apartado que sigue iterando traz pasar z>=0 y etso no tiene ningun sentido')
print('VEMOS PQ HAY QUE HACER ESTO DEL Z>=0 Y POR ELLO RK4 SIN B NI N PQ NO LO SE A PRIORI CD OCURRE Z>=0 Y COMO NO PUEDO HACER Y=leng(N+1) PQ NO CONOZCO N PUES TENGO QUE HACER COLUMN_STACK TRAS CADA ITE E IR CREANDO LA MAT SOLUCION DINAMICAMENTE , CD OBTENGO UNA SOL LE HAGO APPEND Y ANTES PUES COMO LA TENIA INCIALIZAD APUES LA IBA METIENDO PERO AHORA HAY Q HACER APPEND PARA MATRICES')
g = 9.81
alpha = 0.02
M = 7.5
a = 0.
h = 0.05
Y0 = array([0, 50, 7.5])
T0=0
C=0
def F(t, Y): # Y[0] = z, Y[1] = v, Y[2] = m_f
    m = M + Y[2]
    T = T0*(Y[2] > 0) # Y[2] > 0 devuelve un 1 y, en caso contrario, devuelve un 0
    F1 = Y[1]
    F2 = -g + T/m - C*Y[1]*abs(Y[1])/m + alpha*T*Y[1]/m
    F3 = -alpha*T
    return array([F1, F2, F3])

def rk4sisMod70(a,b,fun,N,y0):
    h = (b-a)/N
    t = zeros(N+1)
    y = zeros([len(y0),N+1])
    t[0] = a
    y[:,0] = y0 

    for k in range(N):
        t[k+1] = t[k]+h
        k1=fun(t[k],y[:,k])
        k2=fun(t[k]+h/2,y[:,k]+k1*h/2)
        k3=fun(t[k]+h/2,y[:,k]+k2*h/2)
        k4=fun(t[k+1],y[:,k]+h*k3)
        y[:,k+1] = y[:,k]+(h/6)*(k1+2*k2+2*k3+k4)
    return (t, y) 



    
(t, y) = rk4sisMod70(0,20, F, 200, Y0) # llamada al metodo de RK4 para sistemas

# Dibujamos las soluciones
plot(t, y[0,:], '-*') # dibuja la solucion aproximada


print('Ejercicio 7-a')

print('hacemos ahora el apartado a)')
print('necesito hacerle append pq no puedo meterle en la pos 2 de un array si el array es de tam 1, eso me va a dar indexoutofbounds...')

g = 9.81
alpha = 0.02
M = 7.5



def rk4sisMod7a(a,fun,h,y0):
    t = zeros(1)
    y = zeros([len(y0),1])
    t[0] = a
    y[:,0] = y0 
    k=0
    while y[0,k]>=0:
        t = append(t,t[k]+h)
        k1=fun(t[k],y[:,k])
        k2=fun(t[k]+h/2,y[:,k]+k1*h/2)
        k3=fun(t[k]+h/2,y[:,k]+k2*h/2)
        k4=fun(t[k+1],y[:,k]+h*k3)
        yprov = y[:,k]+(h/6)*(k1+2*k2+2*k3+k4)
        y=column_stack((y,yprov))
        k=k+1
    return (t, y) 

print('EJERCICIO 7-b')
figure('EJERCICIO 7-b-1')
a = 0.#es 0 siempre pq parate de v=0 y t=0 siempre, es decir q siempre en tiempo=0 la velo es 0 (todo el sentido)
h = 0.05
Y0 = array([0, 50, 7.5])
T0=0
C=0
def F(t, Y): # Y[0] = z, Y[1] = v, Y[2] = m_f
    m = M + Y[2]
    T = T0*(Y[2] > 0) # Y[2] > 0 devuelve un 1 y, en caso contrario, devuelve un 0
    F1 = Y[1]
    F2 = -g + T/m - C*Y[1]*abs(Y[1])/m + alpha*T*Y[1]/m
    F3 = -alpha*T
    return array([F1, F2, F3])
(t1, y1) = rk4sisMod7a(0, F, h, Y0) # llamada al metodo de RK4 para sistemas

# Dibujamos las soluciones
plot(t1, y1[0,:], '-*') # dibuja la solucion aproximada


print('\nC='+str(C)+', '+'T='+str(T0))
print('Paso de malla: ' + str(h))
print('Tiempo de vuelo: ' + str(t1[-1])) # La entrada -1 del vector es la última componente
print('Altura máxima: ' + str(max(y1[0,:])))

figure('EJERCICIO 7-b-2')
a = 0.#es 0 siempre pq parate de v=0 y t=0 siempre, es decir q siempre en tiempo=0 la velo es 0 (todo el sentido)
h = 0.05
Y0 = array([0, 50, 7.5])
T0=0
C=0.02
def F(t, Y): # Y[0] = z, Y[1] = v, Y[2] = m_f
    m = M + Y[2]
    T = T0*(Y[2] > 0) # Y[2] > 0 devuelve un 1 y, en caso contrario, devuelve un 0
    F1 = Y[1]
    F2 = -g + T/m - C*Y[1]*abs(Y[1])/m + alpha*T*Y[1]/m
    F3 = -alpha*T
    return array([F1, F2, F3])
(t2, y2) = rk4sisMod7a(0, F, h, Y0) # llamada al metodo de RK4 para sistemas

# Dibujamos las soluciones
plot(t2, y2[0,:], '-*') # dibuja la solucion aproximada

print('\nC='+str(C)+', '+'T='+str(T0))
print('Paso de malla: ' + str(h))
print('Tiempo de vuelo: ' + str(t2[-1])) # La entrada -1 del vector es la última componente
print('Altura máxima: ' + str(max(y2[0,:])))

figure('EJERCICIO 7-b-3')
a = 0.#es 0 siempre pq parate de v=0 y t=0 siempre, es decir q siempre en tiempo=0 la velo es 0 (todo el sentido)
h = 0.05
Y0 = array([0, 50, 7.5])
T0=50
C=0.02
def F(t, Y): # Y[0] = z, Y[1] = v, Y[2] = m_f
    m = M + Y[2]
    T = T0*(Y[2] > 0) # Y[2] > 0 devuelve un 1 y, en caso contrario, devuelve un 0
    F1 = Y[1]
    F2 = -g + T/m - C*Y[1]*abs(Y[1])/m + alpha*T*Y[1]/m
    F3 = -alpha*T
    return array([F1, F2, F3])
(t3, y3) = rk4sisMod7a(0, F, h, Y0) # llamada al metodo de RK4 para sistemas

# Dibujamos las soluciones
plot(t3, y3[0,:], '-*') # dibuja la solucion aproximada

print('\nC='+str(C)+', '+'T='+str(T0))
print('Paso de malla: ' + str(h))
print('Tiempo de vuelo: ' + str(t3[-1])) # La entrada -1 del vector es la última componente
print('Altura máxima: ' + str(max(y3[0,:])))

print('Ejercicio 7-c')
figure('Ejercicio 7-c comparacion de las tres graficas')
title('7(c). MÉTODO RK4')
plot(t1, y1[0,:], t2, y2[0,:], t3, y3[0,:])
xlabel('t')
ylabel('z')
legend(['T0 = 0, C = 0', 'T0 = 0, C = 0.02', 'T0 = 50, C = 0.02'])
show()

figure('masa combustible')

title('7(c). MÉTODO RK4')
plot(t3, y3[2])
xlabel('t')
ylabel('mf')
legend(['T0 = 50, C = 0.02'])
show()

k=0
while y3[2,k] > 0:
    k = k+1
print('Momento en que se acaba el combustible: t = '+ str(t3[k-1]))
