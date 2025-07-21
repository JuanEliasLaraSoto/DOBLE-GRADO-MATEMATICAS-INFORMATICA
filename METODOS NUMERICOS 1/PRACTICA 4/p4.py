# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 18:17:12 2023

@author: Msi
"""

from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import quad
from scipy.interpolate import interp1d

def funexp(x):
    return exp(-x**2)
#quad nos da el valor de la integral y una cota error
iquad,equad=quad(funexp,0,1)#integral de la funcion e^-x2 en [0,1]
#iquad es la aproximacion de la intregal y equad es la estimacion del error
#quad es mi solucion referencia, python la calcula y nosotros para el error ps la compararemos con quad

print('La aproximacion obtenida con quad es ' , iquad, 'y la cota de error es ', equad)

print('EJERCICIO 1')
def pmedio(f,a,b):
    c=0.5*(a+b)#punto medio
    ipmedio=(b-a)*f(c)#integral del pmedio
    return ipmedio

ipmedio=pmedio(funexp,0,1)
#calculamos error cometidos por esta aprox
epmedio=abs(ipmedio-iquad)#iquad es el valor bueno de la integral 
print('La aproximacion obtenida con punto medio es ' ,ipmedio,' y la cota de error es',epmedio)

print('EJERCICIO 2')
def trapecio(f,a,b):
    c=0.5*(b-a)
    itrapecio=c*(f(a)+f(b))
    return itrapecio 
itrapecio=trapecio(funexp,0,1)
#calculamos error cometidos por esta aprox
etrapecio=abs(itrapecio-iquad)#iquad es el valor bueno de la integral 
print('La aproximacion obtenida con trapecio es ' ,itrapecio,' y la cota de error es',etrapecio)

print('EJERCICIO 3')
def simpson(f,a,b):
    c=(1/6)*(b-a)
    isimpson=c*(f(a)+4*f((b+a)/2)+f(b))
    return isimpson 
isimpson=simpson(funexp,0,1)
#calculamos error cometidos por esta aprox
esimpson=abs(isimpson-iquad)#iquad es el valor bueno de la integral 
print('La aproximacion obtenida con simpson es ' ,isimpson,' y la cota de error es',esimpson)

print('EJERCICIO 4')
#la particion es uniforme
#suma de 0 a n-1 y dentro pmedio(f,xi,xi+1)
#saca b-a/N pq la parti es cte, b-a/N me da la long de cada subint
def pmedioc(f,a,b,N):
    x=linspace(a,b,N+1)#me da una particion de N+1 puntos osea desde x0 a xN
    c=0.5*(x[0:N]+x[1:N+1])#c=0.5*([x0,...xN-1]+[x1,...,xN])=[x0+x1/2,x1+x2/2,...,xN-1+xN/2] es basicamente el vector de cada uno de los pmedios (los vectores se suman componente a componente)
    #lo q qremos hacer es f(c) q me dara f(c)=[f(x0+x1/2),f(x1+x2/2),...,f(xN-1+xN)]
    ipmedioc=((b-a)/N)*sum(f(c))
    return ipmedioc
N=10
ipmedioc10=pmedioc(funexp,0,1,N)
epmedioc10=abs(ipmedioc10-iquad)
print('Punto medio compuesta: ',N,'aprox: ',ipmedioc10, 'error:', epmedioc10)

N=20
ipmedioc20=pmedioc(funexp,0,1,N)
epmedioc20=abs(ipmedioc20-iquad)
print('Punto medio compuesta: ',N,'aprox: ',ipmedioc20, 'error:', epmedioc20)
    
print('Cociente de errores: ', epmedioc10/epmedioc20)
    
N=40
ipmedioc40=pmedioc(funexp,0,1,N)
epmedioc40=abs(ipmedioc40-iquad)
print('Punto medio compuesta: ',N,'aprox: ',ipmedioc40, 'error:', epmedioc40)
    
print('Cociente de errores: ', epmedioc20/epmedioc40)

    
N=80
ipmedioc80=pmedioc(funexp,0,1,N)
epmedioc80=abs(ipmedioc80-iquad)
print('Punto medio compuesta: ',N,'aprox: ',ipmedioc80, 'error:', epmedioc80)
    
print('Cociente de errores: ', epmedioc40/epmedioc80)
#da 4 pq hemos ido doblando el num de puntos de particiones 
#cdo divido losng d inter por 2 el error se me divide por 4,pq pmedio es de orden 2 y ((h q es la dist entre puntos)/2pq en cada paso añado el doble de puntos y como parti es equidistante pues la long d cada inter se reduce a la mitad d e lo q era)^2qes el orden meto y 2^2 es 4 y , ademas a mayor orden mas se reduce el error al refinar la particion, esto es por el orden, lo vimos en clase en la parte del orden metodo, x eso el cociente de errores siempre da 4
#si divido entre 2 la long de mi inter (añado el doble de puntos) (de 20 paso a 40 p ej)=> orden 2 pues se reduce 4 veces el error, orden 3 pues se reduce 8 veces el error es decir se reduce 2^orden veces
#si divido entre 10 la long de mi inter (añado el 10 veces mas de puntos) (de 20 paso a 200 p ej)=> orden 2 pues se reduce 100 veces el error, orden 3 pues se reduce 10000 veces el error es decir se reduce 10^orden veces
#en general divido entre x mi long d inter => se divide el error por x^orden
#esto se debe a q el error esta acotado por C(h)^p con C>=0 tal y como vimos en teoria y h es la distancia entre nodos q en este caso como es equid pues es b-a/N y por ello cuando refino la particion(añado puntos)(reduzco x veces la long de inter) el error se reduce x^p veces

"""tal y como vimos en clase teorica mediante una observacion, como el error esta acotado por C*(h/2)**(orden de formula) con C>=0 y h es la distancia entre nodos, en este caso
como es equidistante la particion, se usa h=(b-a)/N y por ello como estamos duplicando N, umaos N´=2N intervalos, y por tanto el cociente d errores siempre da 4 y el orden de la formula de cuadratura del punto medio es 2, se tiene que,
(C*((b-a)/N´)**2)entonces (C*((b-a)/2N)**2) =(C*((b-a)**2/4N)**2),observamos que el error se reduce 4 veces al usar duplicar el numero de intervalos, por ello, el cociente entre la de N intervalos y la de N´=2N intervalos es 4, obteniendo asi que el error del metodo se reduce 4 veces al duplicar N"""
""" por ello, mientras mayor sea el orden de una formula, mas rapidamente decrece el error al refinar la particion."""
"""la f´ormula del rect´angulo a la izquierda compuesta es de
orden 1, las del punto medio y trapecio compuesta de orden 2 y la de Simpson compuesta
de orden 4: """
#cd la parti es uniforme suma de 0 a N-1 de xi+1-xi/2 =b-a/N

print ('EJERCICIO 5')

def trapecioc(f,a,b,N):
    x=linspace(a,b,N+1)
    itrapecioc=((b-a)/N)*(0.5*f(a)+sum(f(x[1:N]))+0.5*f(b))#el sum el primero si lo cuenta el N no asi q este sum va de 1 a N-1 y no a N
    return itrapecioc
N=10
itrapecioc10=trapecioc(funexp,0,1,N)
etrapecioc10=abs(itrapecioc10-iquad)
print('Trapecio compuesta: ',N,'aprox: ',itrapecioc10, 'error:', etrapecioc10)
#hazlo tu para 20 40 ytal
print ('EJERCICIO 6')
def simpsonc(f,a,b,N):
    x=linspace(a,b,N+1)#me da una particion de N+1 puntos
    c=0.5*(x[0:N]+x[1:N+1])#c=0.5*([x0,...xN-1]+[x1,...,xN])=[x0+x1/2,x1+x2/2,...,xN-1+xN/2] es basicamente el vector de cada uno de los pmedios
    #lo q qremos hacer es f(c) q me dara f(c)=[f(x0+x1/2),f(x1+x2/2),...,f(xN-1+xN)]
    isimpsonc=((b-a)/(6*N))*(f(a)+2*sum(f(x[1:N]))+4*sum(f(c))+f(b))
    return isimpsonc
N=10
isimpson10=simpsonc(funexp,0,1,N)
esimpsonc10=abs(isimpson10-iquad)
print('Simpson compuesta: ',N,'aprox: ',isimpson10, 'error:', esimpsonc10)
#q ocurre cd aplico fcompuesta a datos q ya nos dan:aqui estamos aplicando f a los nodos d la parti imagina q t dan tabla q t dice q calcules aprox d integral y t dan solo los nodos y sus imagenes: (x0,f(x0))
#aqui la parti me la estoy haciendo con la particion
#aplica sormula del pmedio usando la tablita de x0 y y0,x1 y y1 ahora mi pmedio es x0+x1/2, si me dicen q es parti uniforme, mi pmedio  seria x1(me dan x0,x1 y x2)
#ahora tengo 5 puntos x0x1x2 mi primer intervalo y evaluo el y1 seria la ev del pmedioy el otro inter es x2x3x4 y el la ev del pmedio seria y3
#f(a ) es la yo, f(b) es y4 , el resto es f(x[1:N]) q es las y1,y2,y3 lo q va ahi (viendo la fromu del trapecio)


print ('EJERCICIO 7')
def gauss3(f,a,b):
    t=array([-sqrt(3/5),0,sqrt(3/5)]) #nodeos en [-1,1]
    alphatilde=array([5/9,8/9,5/9]) #pesos en [-1,1]
    x=a+0.5*(b-a)*(t+1)
    alpha=0.5*(b-a)*alphatilde
    igauss3=sum(alpha*f(x))
    return igauss3
igauss3=gauss3(funexp,0,1)
egauss3=abs(igauss3-iquad)
print('Gauss3: ',igauss3,'error: ',egauss3)

#mnewton y me dan x e y=>  tenemos una seria de datos x0,x1..
                                                ####  y0,y1...
#los inter qw considero son de tres en tres incluyendo el anterios y el pmedio es el 2 del inter de 3 p 
#es en 4*sumfc 4*los y impares, es decir los del medio d cada uno     , y seria y[1:,..,2] para q vaya d dos en dos                                                         


# Interpolación cuadrática
#quadratic_interp = interp1d(x, y, kind='quadratic')
#alfametodo=>g=x+alpha*f(x) alpha=0.1



#cosas en las que sueles fallar:
#tenemos en cuenta para hacerlas lo siguiente:
#los pmedios (f(xi+xi+1/2)) son los de medio de cada, son los impares y no se tienen en cuenta para nada mas, y el resto de puntos son los de sin punto medio, es decir los pares (f(xi))
#los limites del sumatorio son los mismos que el de la formula compuesta
# en el caso de haya tenidod q usar los pmedios pues cada intervalo es el doble pq los he cogifo de 3 en 3 y tengo que multiplicar por 2 la formula
#mi f es ahora el array 'y' y no el array x no te confundas
#hay sumas q van desde 1

#for in range no lo incluye
#x[] no incluye extremo derecha
#linsapece (a,b,n) hace n puntos en tre a y b equid, por eso si n es el num d inter, pone n+1
#h=b-a/N N es el nu d inter, el numero de nodos es n+1
#n>log... =>nmax=int(n)+1
#x[0:4] del q ya tengo



















































def metnewton(f,f1,x0,eps,nmax):
    error=eps+1
    it=0 
    while(error>eps and it<nmax):
        x1=x0-(f(x0)/f1(x0))
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





def dicotomia(f,a,b,eps):
    nmaxi=((log(b-a) -log(eps))/log(2))-1
    nmax=int(nmaxi)+1
    an=a
    bn=b
    fan=f(an)#lo guarda para q no sea tan costoso, llamar a f todo el rato
    fbn=f(bn)
    if fan==0:
        print(str(a)+'es raíz de la función')#puedo poner tb a+'es raiz de la fun'
        return a
    elif fbn==0:
        print(str(b)+'es raíz de la función')
        return b
    elif fan*fbn>0:
        print('No hay cambio de signo: no se puede aplicar el método')
        return#return q no devuelve nada para acabar el programa
    cn_old=an#pq enun dice q lo mas seguro es q la raiz se acerque mas a a, ojo q si pongo q es 0 pues mal pq yo no se q entre a y b esta el 0 asi q como cn esta entre a y b ps eso es fallo pq cn puede q no sea 0 nunca y yo lo estoy suponiendo
    it=0
    error=eps+1#para q entre la primera vez
    while(error>eps and it<nmax):
        cn=(an+bn)/2
        fcn=f(cn)
        print('iter', it+1,'c=',cn,'fn=', fcn)
        #it(n) y la saco por pantalla y ahora preparo todo para it+1(n+1)

        error=abs(cn-cn_old)
        cn_old=cn
        it+=1 
        if fcn==0:
            print(str(cn)+'es raíz de la función')
            return cn
        elif fan*fcn<0:
            bn=cn
            fbn=fcn
        else:
            an=cn
            fan=fcn
    if error<=eps:#he salido del bucle pq la condi de while no se cumple pq he llegado a una raiz con error menor q eps
        print('Se ha alcanzado una aproximacion satisfactoria')
    else:#he salido pq it>=nmax
        print('Se ha alcanzado el numero maximo de iteraciones')
            
    print('la aprox de la raiz con cota de error ' +str(eps)+' es '+str(cn) + ' iteracion '+str(it) )
    print('la aprox de la raiz tras ' , it, ' iteraciones '+' es '+str(cn) )
   #ojo con el sangrado d este pritn pq se pone este print solo al final
    return cn







#ejs que mandó para casa cómo extra a esta practica:
def trapeciocomp_sinf(x, y):
    n = len(x) - 1  # n es el número de intervalos
   
    result = y[0] + y[n]  

    result += 2 * sum(y[1:n])

    return ((x[n]-x[0])/ (2*n)) * result


def simpsoncomp_sinf(x, y):
   
    n = len(x)-1


    suma = y[0] + y[n]
    suma += 4 * sum(y[1:n:2]) + 2 * sum(y[2:n:2])

    integral = 2*((x[n] - x[0]) / (6*n)) * suma
    return integral


def pmediocex_sinf(x,y):
    n=len(x)-1
    integral=2*((x[n]-x[0])/n)*sum(y[1:n:2])
    return integral












x=array([-1,-0.5,0,0.5,1])
y=array([3,4,5,6,7])

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


#doy pol asi   , evaluar el 18 y 19 


def polinomio(z0):
    return eval_forma_newton(x,y,z0)
def cubic(z0):
    return interp1d(x,y,kind='cubic')(z0)


#los extremos del inter son los de tu vector x y tu f es el pol corres ahora y depende del plot qme diga y quita todo lo q tenga N


a=-1 
b=1 
n=(b-a)/0.01 #es un flotante y abajo lo paso a entero
z0=linspace(a,b,int(n+1))

figure()#figure para q para N=5 me de una imagen, para N=10 me de otra  imagen y asi..
pz0=cubic(z0)
plot(z0,cubic(z0),x,cubic(x),x,cubic(x),'o')
title('1')
    
a=-1 
b=1 
n=(b-a)/0.01 #es un flotante y abajo lo paso a entero
z0=linspace(a,b,int(n+1))

figure()#figure para q para N=5 me de una imagen, para N=10 me de otra  imagen y asi..
pz0=polinomio(z0)
plot(z0,polinomio(z0),x,polinomio(x),x,polinomio(x),'o')
title('2')

def trapeciocomp_sinf(x, y):
    n = len(x) - 1  # n es el número de intervalos
   
    result = y[0] + y[n]  

    result += 2 * sum(y[1:n])

    return ((x[n]-x[0])/ (2*n)) * result

print(trapeciocomp_sinf(x,y))


#estremos del inter

print(quad(cubic,-1,1))





#practicando casa:
def ff(x):
    n=len(x)-1
    x1=x[0:n]
    x2=x[1:n+1]
    y=(x1+x2)/2
    return y
x=array([-1,-2,0,1,2,3])
print(ff(x))