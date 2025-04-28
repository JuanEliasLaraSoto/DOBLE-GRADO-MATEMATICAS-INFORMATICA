# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 12:21:43 2025

@author: Msi
"""
import math
from pylab import *
from time import perf_counter
import algoritmos

#para los de la velocidad

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

M=72 
H=2000
abre=1000
g=9.81


def F(t, Y): # Y[0] = z, Y[1] = v, Y[2] = m_f
    C = 0.3*(Y[0] > 0)+40*(Y[0]<1000) # Y[2] > 0 devuelve un 1 y, en caso contrario, devuelve un 0
    F1 = Y[1]
    F2 = -g -(C/M)*Y[1]*abs(Y[1])
    return array([F1, F2])


a = 0.#es 0 siempre pq parate de v=0 y t=0 siempre, es decir q siempre en tiempo=0 la velo es 0 (todo el sentido)
h = 0.05
Y0 = array([H,-25])



start = perf_counter()
# llamada al método RK4:
(t1, y1) = rk4sisMod7a(0, F, h, Y0)
end = perf_counter()
tiempo_cpu = end - start
print("Tiempo de CPU: {:.6f} segundos".format(tiempo_cpu))

# Gráficas
figure(figsize=(10, 5))
subplot(1,2, 1)#subplot(filas, columnas, índice)
plot(t1, y1[0,:])
xlabel("t (s)")
ylabel("Altura z(t) (m)")
title("Altura vs Tiempo")
grid(True, which='both', linestyle='--', linewidth=0.5)


subplot(1, 2, 2)
plot(t1, y1[1,:])
xlabel("t (s)")
ylabel("Velocidad v(t) (m/s)")
title("Velocidad vs Tiempo")
grid(True, which='both', linestyle='--', linewidth=0.5)

tight_layout()
show()

print('Paso de malla: ' + str(h))
print('Tiempo de vuelo: ' + str(t1[-1])) # La entrada -1 del vector es la última componente
print('Altura máxima: ' + str(max(y1[0,:])))
print('velocidad al aterrizar: ' + str(y1[1,-1]))

k=0
while y1[0,k]>1000:
    k=k+1
print("velocidad al abrir paracaida"+str(y1[1,k]))















#para una dimension
def f(t,y):
    return cos(8*pi*t)*(1-5*y)
def exacta(t):
    return (1/5)+(4/5)*exp(-(5/(8*pi))*sin(8*pi*t))
def trap(a, b, fun, N, y0):
   
    
    h = (b-a)/N # paso de malla
    t = zeros(N+1) # inicializacion del vector de nodos
    y = zeros(N+1) # inicializacion del vector de resultados
    t[0] = a # nodo inicial
    y[0] = y0 # valor inicial

    # Metodo de Euler
    for k in range(N):
        t[k+1] = t[k]+h
        y[k+1]=(y[k]+0.5*h*f(t[k],y[k])+0.5*h*cos(8*pi*t[k+1]))/(1+5*0.5*h*cos(8*pi*t[k+1]))
        
    
    return (t, y)


figure("EULER 1A")


# Datos del problema
a = 0.  # extremo inferior del intervalo
b = 1. # extremo superior del intervalo
y0 = 0. # condicion inicial
malla=[40,80,160,320]


for N in malla:
    tini = perf_counter()

    (t, y) = trap(a, b, f, N, y0)
    
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









#para tablero de butcher
from pylab import zeros, array, exp, legend, title, show, plot, xlabel, ylabel

####################################################################################################################################

# EJERCICIO 1(a)

####################################################################################################################################

def butcher(a, b, f, N, y0):
    h = (b - a)/N
    t = zeros(N+1)
    y = zeros(N+1)
    t[0] = a 
    y[0] = y0
    for k in range(N):
       tk1=t[k]+0.33*h 
       yk1=(y[k]+h*0.33)/(1+0.33*h )
       y[k+1 ]=y[k]+h*(1-yk1)
       t[k+1] = t[k] + h

    return (t, y)

####################################################################################################################################

# EJERCICIO 1(b)

####################################################################################################################################

def f(t, y):
    return 1-10*y

def exacta(t):
    return (1/10)+(9/10)*exp(-10*t)

figure("EULER 1A")


# Datos del problema
a = 0.  # extremo inferior del intervalo
b = 2. # extremo superior del intervalo
y0 = 1. # condicion inicial
malla=[20,40,80,160,320]


for N in malla:
    tini = perf_counter()

    (t, y) = butcher(a, b, f, N, y0)
    
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
# Parece que el método es de orden uno, pues al dividir por dos el paso de malla, el error se divide también por dos










##para dimensiones superiores, REVISAR


#Empezamos definiendo el sistema de ecuaciones con el que vamos a trabajar
def f(t,z):
    f1 = 1/z[0] -(exp(t**2)/t**2)*z[1] -t
    f2= 1/z[1] -exp(t**2) -2*t*exp(-t**2)
    return array([f1,f2])

#Definimos la solucion exacta, que en este caso si conocemos
def exacta(t):
    f1 = 1/t
    f2 = exp(-t**2)
    return array([f1,f2])

print("EJERCICIO 1")
#para un solo N

#Empezamos dando los datos del problema de Cauchy
a=1
b=2
y0= array([1,exp(-1)])
N=1000

#Implementamos el metodo RK4 para sistemas


(t,y) = rk4sis(a,b,f,N,y0)
ye = exacta(t)

#Calculo del error cometido
errorX = max(abs(y[0]-ye[0]))
errorY = max(abs(y[1]-ye[1]))
print('El error cometido que nos piden es ',max([errorX,errorY]))

figure('Ejercicio 1')
subplot(211)
plot(t,y[0],'r')
plot(t,ye[0],'b')
xlabel('t')
ylabel('x')
legend(['Aproximacion de x','Solucion exacta de x'])

subplot(212)
plot(t,y[1],'k')
plot(t,ye[1],'b')
xlabel('t')
ylabel('y')
legend(['Aproximacion de y','Solucion exacta de y'])






def f(t,z):
    f1 = 1/z[0] -(exp(t**2)/t**2)*z[1] -t
    f2= 1/z[1] -exp(t**2) -2*t*exp(-t**2)
    return array([f1,f2])

#Definimos la solucion exacta, que en este caso si conocemos
def exacta(t):
    f1 = 1/t
    f2 = exp(-t**2)
    return array([f1,f2])


print("EJERCICIO 2")
#para muchos N
a=1
b=2
y0= array([1,exp(-1)])
mesh= [20,40,80,160,320,640]
figure('Ejercicio 2')
subplot(211)
for N  in mesh:
    
    tini = perf_counter()
    
    (t,y)= rk4sis(a,b,f,N,y0)
    tfin= perf_counter()
    ye= exacta(t)
    error = max(abs(y[0]-ye[0]))
    plot(t, y[0], '-*')
    print('----')
    print('Tiempo CPU: ' + str(tfin-tini))
    print('Error: ' + str(error))
    if N != mesh[0]: #no es igual
         cerror =errorold/error
         print('cociente de errores:'+str(cerror))
         
    #resultados
    print('Paso de malla:' +str((b-a)/N))    
    print('----')
    errorold = error
   #el dibujo de la exacta se puede dibujar fuera del bucle ya que siempre es la misma 


xlabel('t')
ylabel('x')
plot(t,ye[0],'k')
leyenda= ['RK4,N='+str(N) for N in mesh]
leyenda.append('Exacta') #a la lista que he creado antes le añado la exacta

legend(leyenda)
grid(True)


subplot(212)
for N  in mesh:
    
    tini = perf_counter()
    
    (t,y)= rk4sis(a,b,f,N,y0)
    tfin= perf_counter()
    ye= exacta(t)
    error = max(abs(y[1]-ye[1]))
    plot(t, y[1], '-*')
    print('----')
    print('Tiempo CPU: ' + str(tfin-tini))
    print('Error: ' + str(error))
    if N != mesh[0]: #no es igual
         cerror =errorold/error
         print('cociente de errores:'+str(cerror))
         
    #resultados
    print('Paso de malla:' +str((b-a)/N))    
    print('----')
    errorold = error
   #el dibujo de la exacta se puede dibujar fuera del bucle ya que siempre es la misma 


xlabel('t')
ylabel('y')
plot(t,ye[1],'k')
leyenda= ['RK4,N='+str(N) for N in mesh]
leyenda.append('Exacta') #a la lista que he creado antes le añado la exacta

legend(leyenda)
grid(True)












#para rehacer 
##para dimensiones superiores, REVISAR
print("EJERCICIO 1")
#para un solo N

#Empezamos dando los datos del problema de Cauchy
a=0
b=7
y0= array([1,-10])

def f(t,y):
    return array([y[1],-20*y[1]-101*y[0]])
def exacta(t):
    return exp(-10*t)*cos(t)
print("EJERCICIO 2")
#para muchos N
mesh= [20,40,80,160,320,640]
figure('Ejercicio 2')
for N  in mesh:
    
    tini = perf_counter()
    
    (t,y)= rk4sis(a,b,f,N,y0)
    tfin= perf_counter()
    ye= exacta(t)
    error = max(abs(y[0]-ye))
    plot(t, y[0], '-*')
    print('----')
    print('Tiempo CPU: ' + str(tfin-tini))
    print('Error: ' + str(error))
    if N != mesh[0]: #no es igual
         cerror =errorold/error
         print('cociente de errores:'+str(cerror))
         
    #resultados
    print('Paso de malla:' +str((b-a)/N))    
    print('----')
    errorold = error
   #el dibujo de la exacta se puede dibujar fuera del bucle ya que siempre es la misma 


xlabel('t')
ylabel('y')
plot(t,ye,'k')
leyenda= ['RK4,N='+str(N) for N in mesh]
leyenda.append('Exacta') #a la lista que he creado antes le añado la exacta

legend(leyenda)
grid(True)

'''
Como el cociente de errores es aproximadamente 1 en cada paso, y el error no disminuye al refinar la malla, se concluye que el método no mejora su precisión al reducir el paso. Por tanto, el orden efectivo del método es cero, lo que sugiere que la implementación actual no es consistente con el método de Runge-Kutta descrito por el tablero de Butcher.
'''

'''
Para estimar el orden del método utilizado, se ha comparado el error cometido al resolver el mismo problema con diferentes tamaños de paso.
 Al reducir el paso a la mitad, se ha observado que el error también se reduce aproximadamente a la mitad. 
 Este comportamiento se ha cuantificado mediante el cociente de errores, que es la razón entre el error con un paso y el error con la mitad de ese paso.

En este caso, los cocientes de errores obtenidos se aproximan a 2. Este valor indica que el error disminuye linealmente al reducir el paso, lo cual es característico de los métodos numéricos de primer orden.
 Por tanto, tanto por la teoría como por la observación experimental del cociente de errores, se concluye que el método es de orden uno.'''

'''
Para comprobar el orden del método, se ha analizado cómo varía el error al reducir progresivamente el tamaño del paso. Se ha utilizado el cociente de errores, que compara el error cometido con un paso determinado frente al error con la mitad de ese paso.

En este caso, los cocientes de errores obtenidos se aproximan a 4. Esto indica que al reducir el paso a la mitad, el error disminuye aproximadamente a una cuarta parte, lo cual es característico de los métodos de segundo orden. Por tanto, el cociente de errores confirma que el método implementado tiene orden dos.
'''
'''
El orden del método se ha estimado observando cómo decrece el error al aplicar el mismo método con distintos tamaños de paso. 
Para ello se ha utilizado el cociente de errores, que permite comparar directamente el error entre simulaciones con pasos sucesivos.

En este caso, los cocientes obtenidos se aproximan a 8, lo cual indica que al reducir el paso a la mitad, 
el error se reduce aproximadamente a una octava parte. Esta disminución es propia de un método de tercer orden. 
Por tanto, los resultados numéricos, junto con el análisis del cociente de errores, permiten concluir que el método es de orden tres.

'''

''' REPRESENTAR DOS GRÁFICAS EN UNA

subplot(121)
plot(t, Y[0,:], t, Y[1,:])
xlabel('t')
ylabel('x, y')
legend(['Presa', 'Depredador'])

subplot(122)
plot(Y[0,:], Y[1,:])
xlabel('x')
ylabel('y')
legend(['Trayectoria'])

show() '''


'''
plot(t,y[0],'r',linewidth=4)
plot(t,ye[0],'b',linewidth=1)

'''
# Hay anomalías para N = 20 (hay problemas de estabilidad; ya se verá en clase)

#para la trayectoria


#Empezamos definiendo el sistema de ecuaciones con el que vamos a trabajar
def f(t,z):
    f1 = 0.25*z[0]-0.01*z[0]*z[1]
    f2= -z[1] + 0.01*z[0]*z[1]
    return array([f1,f2])

#Definimos la solucion exacta, que en este caso si conocemos
def exacta(t):
    f1 = 1/t
    f2 = exp(-t**2)
    return array([f1,f2])
a=0
b=20
y0= array([80,30])

print("EJERCICIO 2")
#para muchos N
mesh= [20,40,80,160,320,640]
figure('Ejercicio 2')

for N  in mesh:
    
    tini = perf_counter()
    
    (t,y)= rk4sis(a,b,f,N,y0)
    tfin= perf_counter()
    ye= exacta(t)
    error = max(abs(y[1]-ye[1]))
    plot(y[0,:], y[1,:])
    print('----')
    print('Tiempo CPU: ' + str(tfin-tini))
    print('Error: ' + str(error))
    if N != mesh[0]: #no es igual
         cerror =errorold/error
         print('cociente de errores:'+str(cerror))
         
    #resultados
    print('Paso de malla:' +str((b-a)/N))    
    print('----')
    errorold = error
   #el dibujo de la exacta se puede dibujar fuera del bucle ya que siempre es la misma 


xlabel('x')
ylabel('y')

leyenda= ['RK4,N='+str(N) for N in mesh]

legend(leyenda)
grid(True)

show()
