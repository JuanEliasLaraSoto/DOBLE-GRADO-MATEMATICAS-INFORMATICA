# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:23:20 2023

@author: Msi
"""
from scipy.integrate import quad
from numpy import *
from matplotlib.pyplot import *
from scipy.interpolate import interp1d


def puntofijo(f,f1,x0,eps,nmax):
    error=eps+1
    it=0 
    while(error>eps and it<nmax):
        x1=x0-(f(x0)/f1(x0))
        error=abs(x1-x0)
        print(it,error,x1)
       
        it+=1
        
        x0=x1
        
    if(error<=eps):
        print('Se ha alcanzado el criterio de parada')
        print('Tras',it,'iteraciones la solucion obtenida es', x1,'con error ',error)
    else:#si no ha salido por eerrror entonces ha salido por q ha superado el nmax 
        print('se ha alcanzado el num de it sin encontrar el punto fijo')
        print('Tras',it,'iteraciones la solucion obtenida es', x1,'con error ',error)
    return x1
def f(x):
    return cos(2*x)
def f1(x):
    return -2*sin(2*x)
def f2(x):
    return -cos(x)
print('gfffffff'+str(puntofijo(f,f1,2.5,1e-12,100)))


print('Ejercicio 2: ')
def metodoHalley(f,df,df2,x):
    result = x- ((2*f(x)*df(x))/(2*(df(x)**2)-f(x)*df2(x)))
    return result
def halley(f,df,df2,x0,epsilon,nmax):
    xanterior = x0
    xactual = metodoHalley(f,df,df2,xanterior)
    error = abs(xactual     -xanterior)
    iteraciones = 1
    print("Aproximación actual: ", xactual)
    print("Error actual: ", error)
    print("Número de iteraciones: ", iteraciones)
    while    (iteraciones    <nmax and error>=epsilon):
        xanterior = xactual
        xactual = metodoHalley    (    f    ,df    ,df2    ,xanterior    )
        error = abs    (xanterior    -xactual    )
        iteraciones = iteraciones    +    1
        print    ("Aproximación actual: ", xactual    )
        print    ("Error actual: ", error    )
        print    ("Número de iteraciones: ", iteraciones    )
    if    (iteraciones==nmax):
        print    ("Se ha excedido el número máximo de iteraciones"
                  )
    print    ("Aproximación final: ", xactual
    )
    print    ("Error final: ", error
    )
    print    ("Número final de iteraciones: ", iteraciones
    )
    return    (xactual, error, iteraciones    )
print(halley(f,f1,f2,0.5,1e-6,100))
def f(x):
    return cos(x)
def f1(x):
    return -sin(x)
def f2(x):
    return -cos(x)
print('khjhjhkjkj'+str(halley(f,f1,f2,0.5,1e-6,100)))

print("Ejercicio 3: ")
def metodonewton(f, df, x0, epsilon, nmax):
    k=0
    xant=x0
    xact= x0 - f(x0)/df(x0)
    error=abs(xact-xant)
    while(k<nmax and error>=epsilon):
        xant=xact
        xact=xant - f(xant)/df(xant)
        error=abs(xact-xant)
        print("Resultado actual: ", xact)
        print("Error en la iteracion ", k, ": ", error, '\n')
        k=k+1
    if(k>=nmax):
        print("Se ha excedido el número máximo de iteraciones")
        return
    else:
        print("Resultado: ", xact)
        print("Error: ", error)
        print("Número de iteraciones: ", k)
    return xact

def f2(x):
    return cos(2*x)
def df2(x):
    return -2*sin(2*x)
p=metodonewton(f2,df2,2.5,1e-12, 500)
print('gffggfgf'+str(p))

def ej1(x):
    n=len(x)
    suma=0
    for i in range(n):
        suma=suma+x[i]
    return suma, suma/n
        
print(ej1([1,2,3,4,5,6,7,8,9]))



def ff(x):
    n=len(x)-1
    x1=x[0:n]
    x2=x[1:n+1]
    y=(x1+x2)/2
    return y
x=array([2,3,4,5,6])
print(ff(x))


def iterNecesarias(a,b,epsilon):
    cota = (log(b-a)-log(epsilon))/(log(2)) -1
    n=1
    while(n<=cota):
        n=n+1
    print("Hacen falta", n, "iteraciones.")
    return n 
    
def dicotomia(f,a,b,epsilon):
    nmax = iterNecesarias(a,b,epsilon) + 1
    iter=1
    an = a
    bn = b
    cn=0
    esRaiz = False
    while(iter<nmax and esRaiz==False):
        cn = (an+bn)/2
        fcn=f(cn)
        fan=f(an)
        fbn=f(bn)
        print("cn=", cn, "f(cn)=", fcn, "Iteracion: ", iter
        )
        if(fcn==0):
            esRaiz=True
        elif(fcn*fan>0):
            an=cn
            
            
        elif(fcn*fan<0):
            bn=cn
        iter=iter+1
    print("Aproximacion final:", cn, "Iteraciones: ", iter-1)
    return cn
def f(x):
    return sin(2*x)
print('fffffff'+str(dicotomia(f,1,2,1e-8)))


x=array([-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1])
y=array([-0.0385, -0.0588, -0.1000, -0.2000, -0.5000 , -1.0000, -0.5000, -0.2000, -
0.1000, -0.0588, -0.0385])

def tabla_diferencias_divididas(x,y):
    """ Calcula la tabla completa de las diferencias divididas a partir de los datos x e y.
    Devuelve una matriz (df) triangular inferior que en la columna k-esima contiene las
    diferencias divididas de orden k"""

    n= len(y)
    df=zeros([n,n])
    df[:,0]=y
    yn=y
    for i in range(0, len(x)-1):
        dx=x[i+1: len(x)]-x[0:n-(i+1)]
        yn=diff(yn)/dx
        df[i+1:n,i+1]=yn
    return df
    
def eval_forma_newton(x,y,z_0):
    """ Calcula en primer lugar el polinomio de interpolacion de Lagrange que interpola los datos x e
    y mediante la formula de Newton y lo evalua en z0."""  
    n= len(y)
    df=tabla_diferencias_divididas(x,y)
    peval=df[0,0]
    prod=1.0
    for i in range(1,n):
        prod=prod*(z_0-x[i-1])
        peval=peval+df[i,i]*prod
    return peval 
    

def pol(z0):
    return eval_forma_newton (x,y,z0)

def spline_lineal_trozos(z0):#calcula el spline cubico
   
    pol=interp1d(x,y,kind='linear')
    return pol(z0)

a=-1 
b=1
n=(b-a)/0.01 #es un flotante y abajo lo paso a entero
z0=linspace(a,b,int(n+1))
figure()#figure para q para N=5 me de una imagen, para N=10 me de otra  imagen y asi..
polx=pol(x)#pol inter lineal a trozos, es la funcion no es nada  y me falata evaluarlo en los z0)
pz0=pol(z0)
plot(z0,pz0,x,polx,x,polx,'o')
title('1')

a=-1 
b=1
n=(b-a)/0.01 #es un flotante y abajo lo paso a entero
z0=linspace(a,b,int(n+1))
figure()#figure para q para N=5 me de una imagen, para N=10 me de otra  imagen y asi..
polx=spline_lineal_trozos(x)#pol inter lineal a trozos, es la funcion no es nada  y me falata evaluarlo en los z0)
pz0=spline_lineal_trozos(z0)
plot(z0,pz0,'k',x,polx,'r',x,polx,'o')
title('2')


def trapeciocomp(x, y):
    n = len(x) - 1  # n es el número de intervalos
   
    result = y[0] + y[n]  

    result += 2 * sum(y[1:n])

    return ((x[n]-x[0])/ (2*n)) * result
print(trapeciocomp(x,y)) 
(i,error)=quad(spline_lineal_trozos,-1,1)
print(i)
