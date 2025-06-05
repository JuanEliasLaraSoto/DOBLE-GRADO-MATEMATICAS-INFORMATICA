# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 19:29:52 2025

@author: Msi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 17:53:22 2025

@author: Msi
"""
from pylab import *
from time import perf_counter
print('EXAM 27 JUNE 2022 ej3')

def fun(t,y):
    return array ([y[0],-20*y[1]-101*y[0]])
def exacta(t):
    return exp(-10*t)*cos(t);


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



y0 = array([1.0, -10.0])
a = 0.0
b = 7.0
malla = [25, 100, 400]

for N in malla:
    t0 = perf_counter()
    (t, y) = AB4_sistema(a, b, fun, N, y0)
    t1 = perf_counter()

    h = (b - a) / N
    ye = exacta(t)

    error = abs(ye - y[0])
    max_error = max(error)

    print(f"N = {N}, h = {h:.5f}, max error = {max_error:.3e}, tiempo = {t1 - t0:.3f}s")

    plot(t, y[0], label=f"AB4 N={N}")
    if N == max(malla):
        plot(t, ye, 'k--', label='Sol. exacta')

legend()
xlabel("t")
ylabel("x(t)")
title("Comparación entre solución exacta y método AB4")
grid(True)
show()




def AM4_sis(a, b, fun, N, y0):
    Y = zeros((len(y0), N+1))
    t = zeros(N+1)
    F = zeros((len(y0), N+1))
    h = (b - a)/float(N) 
    t[0] = a
    Y[:,0] = y0
    F[:,0] = fun(a, Y[:,0])
    maxiter = 0
    for k in range(3):
        t[k+1] = t[k] + h
        k1 = fun(t[k], Y[:,k])
        k2 = fun(t[k] + h/2, Y[:,k] + h/2*k1)
        k3 = fun(t[k] + h/2, Y[:,k] + h/2*k2)
        k4 = fun(t[k+1], Y[:,k] + h*k3)
        Y[:,k+1] = Y[:,k] + h/6*(k1 + 2*k2 + 2*k3 + k4)
        F[:,k+1] = fun(t[k+1], Y[:,k+1])
    for k in range(3, N):
        t[k+1] = t[k] + h
        Ck = Y[:,k] + h/720 * (646*F[:,k] - 264*F[:,k-1] + 106*F[:,k-2] - 19*F[:,k-3])        
        eps = 1.e-12
        error = eps + 1
        iter = 0
        z = Y[:,k]+h/24*(55*F[:,k]-59*F[:,k-1]+37*F[:,k-2]-9*F[:,k-3])
        while(error >= eps and iter < 200):
            znew = h/720 * (251 * fun(t[k+1], z)) + Ck          
            error = max(abs(z - znew)) # OJO: LA NORMA EN \R^2 ES DISTINTA (tomamos la norma infinito)
            z = znew
            iter += 1
        if iter == 200:
            print('El método de punto fijo no ha convergido')
        maxiter = max(maxiter, iter)
        Y[:,k+1] = z
        F[:,k+1] = fun(t[k+1], Y[:,k+1])
    return (t, Y, maxiter)




for N in malla:
    t0 = perf_counter()
    (t, y,MAXITER) = AM4_sis(a, b, fun, N, y0)
    t1 = perf_counter()

    h = (b - a) / N
    ye1 = exacta(t)

    error1 = max(abs(ye1 - y[0]))


    print(error1)

    print(MAXITER)