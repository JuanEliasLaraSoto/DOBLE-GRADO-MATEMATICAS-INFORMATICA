# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 22:36:11 2025

@author: Msi
"""

from pylab import *
from time import perf_counter


def fun(t,y):
    return -y+2*sin(t);


def exacta(t):
    return (pi+1)*exp(-t)+sin(t)-cos(t);


def AB3(a, b, fun, N, y0):
    y = zeros(N+1)
    t = zeros(N+1)
    f = zeros(N+1)
    t[0] = a
    h = (b - a) / float(N)
    y[0] = y0
    f[0] = fun(a, y[0])

    for k in range(2):
        t[k+1] = t[k] + h
        k1 = fun(t[k], y[k])
        k2 = fun(t[k] + h/2, y[k] + h/2 * k1)
        k3 = fun(t[k] + h/2, y[k] + h/2 * k2)
        k4 = fun(t[k+1], y[k] + h * k3)
        y[k+1] = y[k] + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        f[k+1] = fun(t[k+1], y[k+1])

    for k in range(2, N):
        y[k+1] = y[k] + h/12.0 * (23.0 * f[k] - 16.0 * f[k-1] + 5.0 * f[k-2])
        t[k+1] = t[k] + h
        f[k+1] = fun(t[k+1], y[k+1])

    return (t, y)


# Datos del problema
y0 = pi
a = 0.0
b = 10.0
malla=[50]


for N in malla:
    tini = perf_counter()

    (t, y) = AB3(a, b, fun, N, y0)
    
    
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

# Datos del problema
y0 = pi
a = 0.0
b = 10.0
malla=[50]

figure()

for N in malla:
    tini = perf_counter()

    (t, y, maxiter) = AM3_generico(a, b, fun, N, y0)
    
    
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
    print('Máximo número de iteraciones de punto fijo: ' + str(maxiter))

    
    
    if N > malla[0]:
        order=(log(errorold)-log(error))/log(2)
        print('orden aprox ' +str(order))
    print('---------------------')
    errorold=error
    

plot(t,ye)
leyenda=['N = '+str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)


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




# Datos del problema
y0 = pi
a = 0.0
b = 10.0
malla=[50]


for N in malla:
    tini = perf_counter()

    (t, y) = ABM3(a, b, fun, N, y0)
    
    
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






def fun(t, y):
    return array([3*y[0] - 2*y[1], -y[0] + 3*y[1] - 2*y[2], -y[1] + 3*y[2]])
def exacta(t):
    return array([-0.25*exp(5*t)+3/2*exp(3*t)-0.25*exp(t),0.25*exp(5*t)-0.25*exp(t),-1/8*exp(5*t)-3/4*exp(3*t)-1/8*exp(t)]);




######## EJERCICIO 4
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
        z = Y[:,k] + h/12*(23*F[:,k] - 16*F[:,k-1] + 5*F[:,k-2])
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








Y0 = array([1.0,0, -1.0])
a = 0.0
b = 1.0
malla = [100]

for N in malla:
    t0 = perf_counter()
    (t, y,MAXITER) = AM3_sis(a, b, fun, N, Y0)
    t1 = perf_counter()

    h = (b - a) / N
    (ye1,ye2,ye3) = exacta(t)

    error1 = max(abs(ye1 - y[0,:]))
    error2 = max(abs(ye2 - y[1,:]))
    error3 = max(abs(ye3 - y[2,:]))


    print(error1)
    print(error2)
    print(error3)
    print(MAXITER)


def AB3_sis(a, b, fun, N, y0):
    y = zeros((len(y0), N+1))
    t = zeros(N+1)
    f = zeros((len(y0), N+1))
    t[0] = a
    h = (b - a) / float(N)
    y[:,0] = y0
    f[:,0] = fun(a, y[:,0])

    for k in range(2):
        t[k+1] = t[k] + h
        k1 = fun(t[k], y[:,k])
        k2 = fun(t[k] + h/2, y[:,k] + h/2*k1)
        k3 = fun(t[k] + h/2, y[:,k] + h/2*k2)
        k4 = fun(t[k+1], y[:,k] + h*k3)
        y[:,k+1] = y[:,k] + h/6*(k1 + 2*k2 + 2*k3 + k4)
        f[:,k+1] = fun(t[k+1], y[:,k+1])

    for k in range(2, N):
        y[:,k+1] = y[:,k] + h/12.0 * (23.0 * f[:,k] - 16.0 * f[:,k-1] + 5.0 * f[:,k-2])
        t[k+1] = t[k] + h
        f[:,k+1] = fun(t[k+1], y[:,k+1])

    return (t, y)


Y0 = array([1.0,0, -1.0])
a = 0.0
b = 1.0
malla = [100]

for N in malla:
    t0 = perf_counter()
    (t, y) = AB3_sis(a, b, fun, N, Y0)
    t1 = perf_counter()

    h = (b - a) / N
    (ye1,ye2,ye3) = exacta(t)

    error1 = max(abs(ye1 - y[0,:]))
    error2 = max(abs(ye2 - y[1,:]))
    error3 = max(abs(ye3 - y[2,:]))


    print(error1)
    print(error2)
    print(error3)

#####EJERCICIO 3###################################
def ABM3(a, b, fun, N, y0):
    y = zeros((len(y0), N+1))
    t = zeros(N+1)
    f = zeros((len(y0), N+1))
    h = (b - a)/float(N) 
    t[0] = a
    y[:,0] = y0
    f[:,0] = fun(a, y[:,0])
    for k in range(2): # como el método AM3 es de orden 4, hay que hallar y_1 e y_2 con un método unipaso de orden >= 3
        t[k+1] = t[k] + h
        k1 = fun(t[k], y[:,k])
        k2 = fun(t[k] + h/2, y[:,k] + h/2*k1)
        k3 = fun(t[k] + h/2, y[:,k] + h/2*k2)
        k4 = fun(t[k+1], y[:,k] + h*k3)
        y[:,k+1] = y[:,k] + h/6*(k1 + 2*k2 + 2*k3 + k4)
        f[:,k+1] = fun(t[k+1], y[:,k+1]) # MUY IMPORTANTE: siempre se me olvida esta línea
    for k in range(2, N):
        Ck = y[:,k] + h/24*(19*f[:,k] - 5*f[:,k-1] + f[:,k-2])
        t[k+1] = t[k] + h
        pred = y[:,k] + h/12*(23*f[:,k] - 16*f[:,k-1] + 5*f[:,k-2]) # predicción (método AB3)
        y[:,k+1] = h*(9/24)*fun(t[k+1], pred) + Ck # correción (método AM3)
        f[:,k+1] = fun(t[k+1], y[:,k+1])
    return (t, y)
   

Y0 = array([1.0,0, -1.0])
a = 0.0
b = 1.0
malla = [100]

for N in malla:
    t0 = perf_counter()
    (t, y) = ABM3(a, b, fun, N, Y0)
    t1 = perf_counter()

    h = (b - a) / N
    (ye1,ye2,ye3) = exacta(t)

    error1 = max(abs(ye1 - y[0,:]))
    error2 = max(abs(ye2 - y[1,:]))
    error3 = max(abs(ye3 - y[2,:]))


    print(error1)
    print(error2)
    print(error3)
