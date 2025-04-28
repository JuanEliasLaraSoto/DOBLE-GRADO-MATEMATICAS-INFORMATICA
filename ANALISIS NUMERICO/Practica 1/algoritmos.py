# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 13:52:06 2025

@author: Msi
"""
from pylab import *
from time import perf_counter


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

def df(t, y):
    return t - 0.25*(t**2 - y)


def dfdf(t,y):
    return 1 - 1/2*t + 1/8*t**2 - 1/8*y


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

