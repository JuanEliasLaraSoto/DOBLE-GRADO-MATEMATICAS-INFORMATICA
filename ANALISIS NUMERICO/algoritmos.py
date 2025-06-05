# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 22:30:18 2025

@author: Msi
"""
from pylab import *
from time import perf_counter


def BDF3_sis(a, b, fun, N, y0):
    Y = zeros((len(Y0), N+1))
    t = zeros(N+1)
    F = zeros((len(Y0), N+1))
    h = (b - a)/float(N) 
    t[0] = a
    Y[:,0] = y0
    F[:,0] = fun(a, Y[:,0])
    maxiter = 0
    for k in range(2): # dos primeras iteraciones con el método RK4
        t[k+1] = t[k] + h
        k1 = fun(t[k], Y[:,k])
        k2 = fun(t[k] + h/2, Y[:,k] + h/2*k1)
        k3 = fun(t[k] + h/2, Y[:,k] + h/2*k2)
        k4 = fun(t[k+1], Y[:,k] + h*k3)
        Y[:,k+1] = Y[:,k] + h/6*(k1 + 2*k2 + 2*k3 + k4)
        F[:,k+1] = fun(t[k+1], Y[:,k+1])
    for k in range(2, N):
        t[k+1] = t[k] + h
        Ck = 18/11*Y[:,k] - 9/11*Y[:,k-1] + 2/11*Y[:,k-2]
        eps = 1.e-12
        error = eps + 1
        iter = 0
        z = Y[:,k]
        while(error >= eps and iter < 200):
            znew = h*6/11*fun(t[k+1], z) + Ck
            error = max(abs(z - znew)) # OJO: LA NORMA EN \R^2 ES DISTINTA (tomamos la norma infinito)
            z = znew
            iter += 1
        if iter == 200:
            print('El método de punto fijo no ha convergido')
        maxiter = max(maxiter, iter)
        Y[:,k+1] = z
        F[:,k+1] = fun(t[k+1], Y[:,k+1])
    return (t, Y, maxiter)


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


def AM3_sis(a, b, fun, N, y0):
    Y = zeros((len(y0), N+1))
    t = zeros(N+1)
    F = zeros((len(y0), N+1))
    h = (b - a)/float(N) 
    t[0] = a
    Y[:,0] = y0
    F[:,0] = fun(a, Y[:,0])
    maxiter = 0
    for k in range(2):
        t[k+1] = t[k] + h
        k1 = fun(t[k], Y[:,k])
        k2 = fun(t[k] + h/2, Y[:,k] + h/2*k1)
        k3 = fun(t[k] + h/2, Y[:,k] + h/2*k2)
        k4 = fun(t[k+1], Y[:,k] + h*k3)
        Y[:,k+1] = Y[:,k] + h/6*(k1 + 2*k2 + 2*k3 + k4)
        F[:,k+1] = fun(t[k+1], Y[:,k+1])
    for k in range(2, N):
        t[k+1] = t[k] + h
        Ck = Y[:,k] + h/24*(19*F[:,k] - 5*F[:,k-1] + F[:,k-2])
        eps = 1.e-12
        error = eps + 1
        iter = 0
        z = Y[:,k]
        while(error >= eps and iter < 200):
            znew = 9/24*h*fun(t[k+1], z) + Ck
            error = max(abs(z - znew)) # OJO: LA NORMA EN \R^2 ES DISTINTA (tomamos la norma infinito)
            z = znew
            iter += 1
        if iter == 200:
            print('El método de punto fijo no ha convergido')
        maxiter = max(maxiter, iter)
        Y[:,k+1] = z
        F[:,k+1] = fun(t[k+1], Y[:,k+1])
    return (t, Y, maxiter)












#####EJERCICIO 3###################################
def ABM3(a, b, fun, N, y0):
    y = zeros(N+1)
    t = zeros(N+1)
    f = zeros(N+1)
    h = (b - a)/float(N) 
    t[0] = a
    y[0] = y0
    f[0] = fun(a, y[0])
    for k in range(2): # como el método AM3 es de orden 4, hay que hallar y_1 e y_2 con un método unipaso de orden >= 3
        t[k+1] = t[k] + h
        k1 = fun(t[k], y[k])
        k2 = fun(t[k] + h/2, y[k] + h/2*k1)
        k3 = fun(t[k] + h/2, y[k] + h/2*k2)
        k4 = fun(t[k+1], y[k] + h*k3)
        y[k+1] = y[k] + h/6*(k1 + 2*k2 + 2*k3 + k4)
        f[k+1] = fun(t[k+1], y[k+1]) # MUY IMPORTANTE: siempre se me olvida esta línea
    for k in range(2, N):
        Ck = y[k] + h/24*(19*f[k] - 5*f[k-1] + f[k-2])
        t[k+1] = t[k] + h
        pred = y[k] + h/12*(23*f[k] - 16*f[k-1] + 5*f[k-2]) # predicción (método AB3)
        y[k+1] = h*(9/24)*fun(t[k+1], pred) + Ck # correción (método AM3)
        f[k+1] = fun(t[k+1], y[k+1])
    return (t, y)



def AM3_Newton(a, b, fun, N, y0):
    tol=1.e-12
    nmax=200
    y = zeros(N+1)
    t = zeros(N+1)
    f = zeros(N+1)
    h = (b - a)/float(N) 
    t[0] = a
    y[0] = y0
    f[0] = fun(a, y[0])
    maxiter = 0
    for k in range(2):#usamos rk4 pq el orden de am3 es 4
        t[k+1] = t[k] + h
        k1 = fun(t[k], y[k])
        k2 = fun(t[k] + h/2, y[k] + h/2*k1)
        k3 = fun(t[k] + h/2, y[k] + h/2*k2)
        k4 = fun(t[k+1], y[k] + h*k3)
        y[k+1] = y[k] + h/6*(k1 + 2*k2 + 2*k3 + k4)
        f[k+1] = fun(t[k+1], y[k+1])
    for k in range(2, N):
        t[k+1] = t[k] + h
        Ck = y[k] + h/24*(19*f[k] - 5*f[k-1] + f[k-2])#ojo con tk, siempre ponerlo primero mejor
        dist = tol + 1
        count = 0
        z = y[k] + h/12*(23*f[k] - 16*f[k-1] + 5*f[k-2])
        while(dist >tol and count < nmax):
            F = z - 9*h/24*fun(t[k+1], z) - Ck # al escribir 9*24/h y 9*h/24 pueden obtenerse resultados ligeramente distintos
            dF = 1 - 9*h/24*dyfun(t[k+1], z)
            znew = z - F/dF
            dist = abs(z - znew)
            count += 1
            z = znew

        if count == nmax:
            print('El método de punto fijo no ha convergido')
        maxiter = max(maxiter, count)
        y[k+1] = z
        f[k+1] = fun(t[k+1], y[k+1])
    return (t, y, maxiter)



def AM3_generico(a, b, fun, N, y0):
    tol=1.e-12
    nmax=200
    y = zeros(N+1)
    t = zeros(N+1)
    f = zeros(N+1)
    h = (b - a)/float(N) 
    t[0] = a
    y[0] = y0
    f[0] = fun(a, y[0])
    maxiter = 0
    for k in range(2):#usamos rk4 pq el orden de am3 es 4
        t[k+1] = t[k] + h
        k1 = fun(t[k], y[k])
        k2 = fun(t[k] + h/2, y[k] + h/2*k1)
        k3 = fun(t[k] + h/2, y[k] + h/2*k2)
        k4 = fun(t[k+1], y[k] + h*k3)
        y[k+1] = y[k] + h/6*(k1 + 2*k2 + 2*k3 + k4)
        f[k+1] = fun(t[k+1], y[k+1])
    for k in range(2, N):
        Ck = y[k] + h/24*(19*f[k] - 5*f[k-1] + f[k-2])#ojo con tk, el p fijo se aplica a lo ostro q tiene el yk+1
        t[k+1] = t[k] + h
        dist = tol + 1#para q entre
        count = 0
        z = y[k] + h/12*(23*f[k] - 16*f[k-1] + 5*f[k-2])
        while(dist >tol and count < nmax):
            znew = 9/24*h*fun(t[k+1], z) + Ck 
            dist = abs(z - znew)
            count += 1
            z = znew

        if count == nmax:
            print('El método de punto fijo no ha convergido')
        maxiter = max(maxiter, count)
        y[k+1] = z
        f[k+1] = fun(t[k+1], y[k+1])
    return (t, y, maxiter)



def AM3_generico(a, b, fun, N, y0):
    tol=1.e-12
    nmax=200
    y = zeros(N+1)
    t = zeros(N+1)
    f = zeros(N+1)
    h = (b - a)/float(N) 
    t[0] = a
    y[0] = y0
    f[0] = fun(a, y[0])
    maxiter = 0
    for k in range(2):#usamos rk4 pq el orden de am3 es 4
        t[k+1] = t[k] + h
        k1 = fun(t[k], y[k])
        k2 = fun(t[k] + h/2, y[k] + h/2*k1)
        k3 = fun(t[k] + h/2, y[k] + h/2*k2)
        k4 = fun(t[k+1], y[k] + h*k3)
        y[k+1] = y[k] + h/6*(k1 + 2*k2 + 2*k3 + k4)
        f[k+1] = fun(t[k+1], y[k+1])
    for k in range(2, N):
        Ck = y[k] + h/24*(19*f[k] - 5*f[k-1] + f[k-2])#ojo con tk, el p fijo se aplica a lo ostro q tiene el yk+1
        t[k+1] = t[k] + h
        dist = tol + 1#para q entre
        count = 0
        z = y[k]
        while(dist >tol and count < nmax):
            znew = 9/24*h*fun(t[k+1], z) + Ck 
            dist = abs(z - znew)
            count += 1
            z = znew

        if count == nmax:
            print('El método de punto fijo no ha convergido')
        maxiter = max(maxiter, count)
        y[k+1] = z
        f[k+1] = fun(t[k+1], y[k+1])
    return (t, y, maxiter)


def RK2(a, b, fun, N, y0):
    y = zeros(N+1)
    t = zeros(N+1)
    h = (b - a)/float(N)
    t[0] = a
    y[0] = y0
    for k in range(N):
        z = y[k] + 0.5 * h * fun(t[k], y[k])
        t[k+1] = t[k] + h
        y[k+1] = y[k] + h * fun(t[k] + 0.5 * h, z)
    return t, y

def AB3(a, b, fun, N, y0):
    y = zeros(N+1)
    t = zeros(N+1)
    f = zeros(N+1)
    t[0] = a
    h = (b - a) / float(N)
    y[0] = y0
    f[0] = fun(a, y[0])

    for k in range(2):#Usamos un método unipaso (como Runge-Kutta 2) para "arrancar" el método multipaso AB3, porque este último necesita al menos 3 puntos iniciales para funcionar.
        z = y[k] + 0.5 * h * f[k]
        y[k+1] = y[k] + h * fun(t[k] + 0.5 * h, z)
        t[k+1] = t[k] + h
        f[k+1] = fun(t[k+1], y[k+1])

    for k in range(2, N):
        y[k+1] = y[k] + h/12.0 * (23.0 * f[k] - 16.0 * f[k-1] + 5.0 * f[k-2])
        t[k+1] = t[k] + h
        f[k+1] = fun(t[k+1], y[k+1])

    return (t, y)


def AB2(a,b,fun, N,y0):
    
    y = zeros(N+1)
    t = zeros(N+1)
    f = zeros(N+1)#novedad
    t[0] = a
    h = (b-a)/float(N) 
    y[0] = y0
    f[0] = fun(a,y[0])    
    y[1] = y[0] + h*f[0]#uso euler para arrancar(para hallar el y1 ya que es bipaso),paso de euler para calcular el y1 pq esto es metodo bipaso asi que necesito conocer el y0,y1 
    t[1] = a+h
    f[1] = fun(t[1], y[1])
    for k in range(1,N):#bucle en tiempo, va desde el  1 pq y ahe caluclado el y1 y va hasta N ojo con el detalle, pq llego hasta el k+1
        y[k+1] = y[k]+0.5*h*(3.0*f[k] - f[k-1])
        t[k+1] = t[k] + h
        f[k+1] = fun(t[k+1], y[k+1])#guardo la f para q el programa sea muy eficaz, pq sino hay q evaluarla muchas veces y gasta mucho
        
    return (t,y)








# Datos del problema
y0 = 0.0
a = 0.0
b = 5.0
malla=[10,20,40,80,160]


for N in malla:
    tini = perf_counter()

    (t, y) = AB2(a, b, fun, N, y0)
    
    
    tfin = perf_counter()
    
    plot(t, y, "-*")
    
    h=(b-a)/float(N)
    
    ye = exacta(t)

    
    # Calculo del error cometido
    error = max(abs(y-ye))
    tcpu=tfin-tini 
    
    print('N = '+str(N))
    print('Error='+str(error))
    print('Tiempo CPU='+str(tcpu))
    
    
    
    if N > malla[0]:
        order=(log(errorold)-log(error))/log(2)
        print('orden aprox ' +str(order))
        
    print('---------------------')
    errorold=error
    

plot(t,ye)
leyenda=['N = '+str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)