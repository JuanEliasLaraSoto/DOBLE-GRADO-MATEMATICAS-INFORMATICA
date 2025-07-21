# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 18:23:52 2023

@author: Msi
"""

from numpy import *
from matplotlib.pyplot import *
print('ejercicio 1')
def puntofijo(g,x0,eps,nmax):
    error=eps+1
    it=0 
    while(error>eps and it<nmax):
        x1=g(x0)
        
        error=abs(x1-x0)
        print(it+1,error,x1)
        it+=1
        x0=x1
        
    if(error<=eps):
        print('Se ha alcanzado el criterio de parada')
        print('Tras',it,'iteraciones la solucion obtenida es', x1,'con error ',error)
    else:#si no ha salido por eerrror entonces ha salido por q ha superado el nmax 
        print('se ha alcanzado el num de it sin encontrar el punto fijo')
        print('Tras',it,'iteraciones la solucion obtenida es', x1,'con error ',error)
    return x1
#cd haya q calcu la g(func ite), es hacer una func equiv con un alfametoso o ponerla asi x=e^-x, asi q en los sig ejs usa ecs equiv q las saca asi
print('ej2')
def g1(x):
    return  exp(-x)
puntofijo(g1,0.5,1e-7,100)
#recurda q en newton es g=x-fx/f'x ojo q es f y f' y no g
def g_newton1(x):
        f=x-exp(-x)
        df=1+exp(-x)
        return x-f/df
puntofijo(g_newton1,0.5,1e-7,100)
#para saber si es convergente, pintetela y el eje x tb


print('ej3')
def g2(x):
    k=2/3
    alfa=0.093
    return k+alfa*sin(x)
puntofijo(g2,0.5,1e-7,100)
def g_newton2(x):
        k=2/3
        alfa=0.093
       
        return x-(g2(x)-x)/(alfa*cos(x)-1)
puntofijo(g_newton2,0.5,1e-7,100)
print('ej4')
def g3(x):
    return cos(x)
puntofijo(g3,0.5,1e-7,100)
def g_newton3(x):
    return x-(g3(x)-x)/(-1-sin(x))
puntofijo(g_newton3,0.5,1e-7,100)

print('ej5')
def rai(x):
    return x**5-5*(x**3)+1
def g_newton4(x):
    f=x**5-5*x**3+1
    df=5*x**4-15*x**2
    return x-f/df
puntofijo(g_newton4,0.6,1e-7,100)


#usa alfametodos para rpobar
figure()#para inicializar el dibujador
x=linspace(0,1)#para un eje de coord, va de 0 a 10 y dibuja 11 puntos, le puedo poner mas para q salga mejor pq los 11 puntos se uniran con rectas
plot(x,rai(x),x,0*x)
title('rai')

figure()
plot(x,g_newton4(x),x,x)
title('newton')


x=linspace(0.3,0.7)
figure()
plot(x,g_newton4(x),x,x)
title('newton zoom')

print('Despejando x**5')
def fiter4a(x):
    return ((5*x**3-1)**(1/5))
puntofijo(fiter4a,0.6,1e-7,100)
figure()
x=linspace(0,1,100)
plot(x,fiter4a(x),x,x)
title('1')
#vemos que no sale

print('Despejando x**3')
def fiter4b(x):
    return ((x**5+1)/5)**(1/3)
figure()
x=linspace(0,1,100)#converge loc
plot(x,fiter4b(x),x,x)#vemos que la pendiente en el punto de corte es menor que 1 en valor absoluto, por lo que podemos usar este método y esta funcion de iteracion
title('2')#converge loc


print('Sumando x')
def fiter4c(x):
    return x+x**5-5*x**3+1
figure()
x=linspace(0,1,100)
plot(x,fiter4c(x),x,x)
title('3')

print('alpha metodo')
def fiter4d(x):
    alpha=0.1
    return x+alpha*(x**5-5*x**3+1)
puntofijo(fiter4d,0.6,1e-7,100)#converge loc
figure()
x=linspace(0,1,100)
plot(x,fiter4d(x),x,x)
title('4')#converge loc



print('ej6a')
def puntofijo_bis(f,g,x0,eps,nmax):
    error=eps+1
    it=0 
    while(error>eps and it<nmax):
        x1=g(x0)
        it+=1
        error=abs(f(x1))
        x0=x1
        
    if(error<=eps):
        print('Se ha alcanzado el criterio de parada')
        print('Tras',it,'iteraciones la solucion obtenida es', x1,'con error ',error)
    else:
        print('se ha alcanzado el num de it sin encontrar el punto fijo')
        print('Tras',it,'iteraciones la solucion obtenida es', x1,'con error ',error)
    return x1



def f5(x):
    return x+(x-1)*exp(x)
x=linspace(0,1)
figure()
plot(x,f5(x),x,0*x)
print("\n Como vemos en la gráfica la función tiene raíz única en el intervalo [0, 1] \n")
print('ej6b')
def g7(x):
    return -(x-1)*exp(x)

puntofijo_bis(f5,g7,0.6,1e-8,100)



x=linspace(0,1)
figure()
plot(x,g7(x),x,x)
##esta es la sol, lo de arriba han sido cosas q ha puesto la seño 
puntofijo_bis(f5,g7,0.6,1e-8,100)#0.6 es una buena semilla si lo ves en la graf del b, vemos q la raiz estará por ahi

print('ejc')
def g_newton7(x):
    f=x+(x-1)*exp(x)
    df=1+(x-1)*exp(x)+exp(x)
    return x-(f/df)
puntofijo_bis(f5,g_newton7,0.6,1e-8,100)




