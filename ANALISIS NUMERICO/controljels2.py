# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 12:29:23 2025

@author: Usuario_UMA
"""


from pylab import *
from time import perf_counter


print('EXAMEN DE JUAN ELIAS LARA SOTO')


################################ EJERCICIO 1#####################
print('EJERCICIO 1')


def fun(t, y):
    return array([-y[0]-5*y[1],5*y[0]-y[1]])
def exacta(t):
    return array([-exp(-t)*sin(5*t),exp(-t)*cos(5*t)]);



def ABM2_sis(a, b, fun, N, y0,L):
    y = zeros((len(y0), N+1))
    t = zeros(N+1)
    f = zeros((len(y0), N+1))
    h = (b - a)/float(N) 
    t[0] = a
    y[:,0] = y0
    f[:,0] = fun(a, y[:,0])
    for k in range(1):#heun
        t[k+1] = t[k] + h
        ff = fun(t[k], y[:,k]) 
        yy = y[:,k] + h*ff
        y[:,k+1] = y[:,k] + 0.5 * h * (ff + fun(t[k+1], yy))
        f[:,k+1] = fun(t[k+1], y[:,k+1]) 
        
    for k in range(1, N):
        
        t[k+1] = t[k] + h
        Ck = y[:,k]+h/12*(8*f[:,k]-f[:,k-1])
        iter = 0
        z =y[:,k] + h/2*(3*f[:,k]-f[:,k-1]) # predicción (método AB2)
        while(iter < L):
            znew = (5/12)*h*fun(t[k+1],z) + Ck # correción (método AM2)
            error = max(abs(z - znew)) # OJO: LA NORMA EN \R^2 ES DISTINTA (tomamos la norma infinito)
            z = znew
            iter += 1
        
        y[:,k+1] = z
        f[:,k+1] = fun(t[k+1], y[:,k+1])
    return (t, y)



   

y0 = array([0,1.0])
a = 0.0
b = 5.0
malla = [30,60,120,240]
L=5

for N in malla:
    tini = perf_counter()

    (t, y) = ABM2_sis(a, b, fun, N, y0,L)
    
    
    tfin = perf_counter()
   # plot(t, y, "-*")
    
    h=(b-a)/float(N)
    
    (ye1,ye2) = exacta(t)
 
    error1 = max(abs(ye1 - y[0,:]))
    error2 = max(abs(ye2 - y[1,:]))

      
     
    
    # Calculo del error cometido
    error = max(error1,error2)
    tcpu=tfin-tini 
    
    print('N = '+str(N))
    print('Error='+str(error))
    print('Tiempo CPU='+str(tcpu))

    
    
    if N > malla[0]:
        order=(log(errorold)-log(error))/log(2)
        print('orden aproximado: ' +str(order))
    print('---------------------')
    errorold=error
    
#graficamos para N=240

figure('EJERCICIO 1 (ABM2) N=240')

subplot(131)
plot(t,y[0],t,ye1)
xlabel('t')
ylabel('y1_aprox - N=240,exacta1')
legend(['N=240','y1_exacta'])


subplot(132)
plot(t,y[1],t,ye2)
xlabel('t')
ylabel('y2_aprox - N=240,exacta2')
legend(['N=240','y1_exacta'])


subplot(133)
plot(y[0],y[1], ye1,ye2)
xlabel('y1_aprox - N=240,exacta1')
ylabel('y2_aprox - N=240,exacta2')
legend(['N=240','exacta'])





################################ EJERCICIO 2#####################
print('EJERCICIO 2')

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






A = array([[-1,-5], [5, -1]])
print('Autovalores de A: ' + str(eigvals(A)))


re = -1.
im = 5.

figure('EJERCICIO 2 (AB2)')
rho = array([1., -1., 0.]) # primero
sigma = array([0., 3., -1.])/2. # segundo
locfron(rho,sigma)
plot([re, re], [im, -im], '*k')
plot([0, re], [0, im], '--', [0, re], [0, -im], '--')

hestrella= 2*1/26

print('h<h*=(2*1/26), luego como h=T/N, y T=5, se tiene que debemos elegir N>5/h*')

print('N>' + 'N_estrella_1 = '+ str(5/hestrella))


figure('EJERCICIO 2 (AM2)')
rho = array([1., -1., 0.]) # primero
sigma = array([5., 8., -1.])/12. # segundo
locfron(rho,sigma)
plot([re, re], [im, -im], '*k')
plot([0, re], [0, im], '--', [0, re], [0, -im], '--')

print('N>' + 'N_estrella_2 = '+ str(5/hestrella))
