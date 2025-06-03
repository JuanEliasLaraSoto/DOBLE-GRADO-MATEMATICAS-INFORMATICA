# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 17:53:22 2025

@author: Msi
"""
from pylab import *
from time import perf_counter
print('EXAM JUNE 17-18- ej4')

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