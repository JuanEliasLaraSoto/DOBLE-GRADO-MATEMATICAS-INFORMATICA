# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:38:44 2020

@author: Usuario
"""

from pylab import *
    


def locfron(rho, sigma):#ME DIBUJA LA FRONTERA DE MI DA
# Dibuja la frontera de la region de estabilidad absoluta 
# de un metodo multipaso.
# rho y sigma son los coeficientes de los polinomios caracteristicos
# ordenados de mayor a menor grado '''
    theta = arange(0, 2.*pi, 0.01)
    numer = polyval(rho, exp(theta*1j)) # rho(e^{theta*i})
    denom = polyval(sigma, exp(theta*1j)) # sigma(e^{theta*i})
    mu = numer/denom
    x = real(mu)
    y = imag(mu)
    plot(x, y)
    grid(True)
    axis('equal')

figure('AB')
# Ejemplo: AB3 y_{k+1} - y_k  = h/12*(23*f_k - 16*f_{k-1} + 5*f_{k-2})
rho = array([1., -1., 0.,0.]) # primero
sigma = array([0., 23., -16., 5.])/23. # segundo
locfron(rho,sigma)

#################  region estabilidad RK



def locfronRK(dR, N):#ME DIBUJA LA FRONTERA DE MI DA
#N ES EL NUMERO DE ETAPAS DEL METODO RK
# Localizacion de la frontera de un metodo RK
#  Devidada de la funcion R
    Npoints = 5000
    T = 2*N*pi
    h = 2*N*pi/Npoints
    z = zeros(Npoints +1 , dtype = complex)
    z[0] = 0.
    t = 0
    for k in range(len(z)-1):
        k1 = 1j*exp(1j*t)/dR(z[k])
        k2 = 1j*exp(1j*(t+0.5*h))/dR(z[k] + 0.5*h*k1)
        k3 = 1j*exp(1j*(t+0.5*h))/dR(z[k] + 0.5*h*k2)
        k4 = 1j*exp(1j*(t+h))/dR(z[k] + h*k3)
        z[k+1] = z[k]+ h*(k1+ 2*k2+ 2*k3 + k4)/6
        t = t + h
    x = real(z)
    y = imag(z)
    plot(x,y)
    grid(True)
    axis('equal')

figure('RK explicitos')

# Euler: función de estabilidad R = 1 + z

def dREuler(z):# derivada de la funcion de estabilidad R de euler
    return 1.
locfronRK(dREuler, 1)

# RK2 explicitos: función de estabilidad R = 1 + z + z**2/2

def dRK2explicit(z):
    return 1. + z
locfronRK(dRK2explicit, 2)

def dRK3explicit(z):
    return 1. + z + z**2/2.
locfronRK(dRK3explicit,3)
def dRK4explicit(z):
    return 1.+z+z**2/2+z**3/6
locfronRK(dRK4explicit,4)

def dEulerImp(z):
    return 1/(1-z)**2
locfronRK(dEulerImp,1)



print('-------------')
print('Problema 2: EN LIBRETA TIENES EL CALCULO DE LOS AUTOVALORES')
print('-------------')

figure('Problema 2. Region de estabilidad')
locfronRK(dREuler,1)
plot([-10,-10],[1,-1],'*')
plot([-10,0],[1,0],'k--')
plot([-10,0],[-1,0],'k--')
hcrit=20/101
plot([-10*hcrit,-10*hcrit],[hcrit,-hcrit],'bo')




