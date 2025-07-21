from numpy import *
from matplotlib.pyplot import *
from scipy.interpolate import interp1d
from scipy.integrate import quad



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

print('ejercicio1')
print('apartado a')
#son puntos equidistantes asi q me lo defino con linspace q lo q hace q saca los 5 puntos equidistantes q hay en o y 1
x=linspace(0,1,5)#x=array([0,0.25,0.5,0.75,1.0])
y=exp(x)#me da y=[e^0,e^0.25,e^0.5,e^0.75,e^1.0]
tabla_dif=tabla_diferencias_divididas(x,y)
print (tabla_dif)

print('ejercicio2')
print ('apartado a')
eval1=eval_forma_newton(x,y,1/3)
print('el poli de inter evaluado en 1/3 vale:',eval1)
print('pasa por los puntos de interpolacion?', eval_forma_newton(x,y,x)==y)#los nodos los tengo guardados en x

print('apartadpob')
def eval_forma_Horner1(p,z0):#en p yo tengo p=[a0,..an] y mi x es z0 
    n=len(p)
    #defino tabla dif dividida
    cn = p[n - 1]

    for i in range(n-2,-1,-1):#n-2 es tu n-1 del pdf, acab en 0 pq acaba uno antes del -1 q es el 0
        cn=cn*(z0)+p[i]
    return cn
polinomio=array([-1,0,1]) 
t = 3
eval1=eval_forma_Horner1(polinomio,t)
print(eval1)
print('apartadpoc')

def eval_forma_Horner(x,y,z0):
    n=len(x)
    #defino tabla dif dividida
    df=tabla_diferencias_divididas(x,y) 
    peval=df[n-1,n-1]
    for i in range(n-2,-1,-1):#con n llegabamos a n-1, ahora q quiero llegar a 0 pues pongo -1
        peval=peval*(z0-x[i])+df[i,i]
    return peval
eval2=eval_forma_Horner(x,y,1/3)
print('el poli de inter evaluado en 1/3 usando horner vale:',eval2)
print('apartado d')
def evalpol_eqd(f,a,b,N,z0):
    x=linspace(a,b,N+1)#linspace me los n+1 equidistantes en el inter a b
    y=f(x)
    pz0=eval_forma_Horner(x,y,z0)
    error=max(abs(f(z0)-pz0))
    return pz0,error
#si no hago particiones de 0,01 no va a quedar e^x parecida si no que rectas que unen puntos(spline cubico)
print('apartado e')
a=-3
b=3
n=(b-a)/0.01 #es un flotante y abajo lo paso a entero
z0=linspace(a,b,int(n+1))
for N in array([5,10,15,20]):#esto me genera 4 graficas pq en cada ite hago figura
    figure()#figure para q en cada ite me de una grafica, para N=5 me de una imagen, para N=10 me de otra  imagen y asi..
    x=linspace(a,b,N+1)#N+1 pq xk con k=0,..,N q es N+1 nodos
    pz0, error=evalpol_eqd(exp,a,b,N,z0)
    plot(z0,exp(z0),z0,pz0,x,exp(x),'o')#'o' para q solo pinte los puntos, y no pinta linea
   #esto d arriba es lo mismo q lo d debajo
   #plot(z0,exp(z0))
    #plot(z0,pz0)
    #plot(x,exp(x),'o')
    print('error para', N,'intervalos',error)
"""podemos observar que el error de interpolacion se va reduciendo conforme 
aumentamos N,ya que estamos refinando la particion y por ello, estamos diviendo la distancia de cada intervalo N veces y tenemos más intervalos y por ello
mas nodos de interpolacion en la particion, por tanto, tenemos más rectas que unen la imagen de cada nodo con la imagen de su siguiente nodo
y estas tienen menor longitud, pudiendo asi dar mas precision a la grafica, dandole una forma
más curvilinea y menos rectilinea.""" 


"""el error que se produce al unir cada imagen de cada nodo con
su siguiente es menor debido que las distancia con su siguiente es menor y"""
"""tenemos mas informacion, mas nodos y de esta forma el error que se produce al 
 unir la imagen de cada nodo con su siguiente es menor debido a que la distancia
 entre nodos es menor y hay mucho menos margen de error (la idea es q los puntos de
 la imagen se unen por rectas y conforma mas puntos tenga pues mas rectas hay de 
 menor longitud y mas curva es la funcion y menos picos tiene)"""

print('apartado f')
def f2(x):
    return 1/(1+x**2)
a=-5
b=5
n=(b-a)/0.01 #es un flotante y abajo lo paso a entero
z0=linspace(a,b,int(n+1))
for N in array([5,10,15,20]):#esto me genera 4 graficas pq en cada ite hago figura
    figure()#figure para q en cada ite me de una grafica, para N=5 me de una imagen, para N=10 me de otra  imagen y asi..
    x=linspace(a,b,N+1)#N+1 pq xk con k=0,..,N q es N+1 nodos
    pz0, error=evalpol_eqd(f2,a,b,N,z0)#evaluo el polinomio en z0
    plot(z0,f2(z0),z0,pz0,x,f2(x),'o')#'o' para q solo pinte los puntos, y no pinta linea
   
    print('error para', N,'intervalos',error)
print('apartado g')

def evalpol_Cheb(f,a,b,N,z0):
    k=linspace(0,N,N+1)
    x=cos((2*k+1)*pi/(2*N+1))#nodos en [-1,1] ahira cada compo de k es cos((2*k+1)*pi/(2*N+1))
    x=a+(b-a)/2*(x+1) #nodos en [a,b]
    y=f(x)
    pz0=eval_forma_Horner(x,y,z0)
    error=max(abs(f(z0)-pz0))
    return pz0,error

#ahora calculamos el polinomia lineal a trozos

#inter1d devuelve una funcion y yo lo q tendre q hacer es evaluarlo en putnos para q nos de unos resultados:handle es la funcion q me devuelve inter1d
print('Ejercicio 3')
print('Apartado a')
def spline_lineal_trozos(f,a,b,N):#calcula el spline cubico
    x=linspace(a,b,N+1)
    y=f(x)
    pol=interp1d(x,y,kind='linear')
    return pol

def spline_cubico_trozos(f,a,b,N):#calcula el spline cubico
    x=linspace(a,b,N+1)
    y=f(x)
    pol=interp1d(x,y,kind='cubic')
    return pol
print('APARTADO b')
print('para spline lineal a trozos')
a=-3
b=3
n=(b-a)/0.01 #es un flotante y abajo lo paso a entero
z0=linspace(a,b,int(n+1))
for N in array([5,10,15,20]):
    figure()#figure para q para N=5 me de una imagen, para N=10 me de otra  imagen y asi..
    pol=spline_lineal_trozos(exp,a,b,N)#pol inter lineal a trozos, es la funcion no es nada  y me falata evaluarlo en los z0)
    pz0=pol(z0)
    x=linspace(a,b,N+1)#nodos de interpolacion
    plot(z0,exp(z0),z0,pz0,x,exp(x),'o')#coger poli inte ry evaluarlo, esto es si me piden evaluar 
    plot(z0,exp(z0),x,exp(x),x,exp(x),'o')#esto es lo mismo q la linea anterior, aqui lo q hace es saber como pinta python q coge los puntos y une rectas , si no me pide evaluar es decir obtener la expresion del poli pues hago esto
print('para spline cubico a trozos')   
a=-3
b=3
n=(b-a)/0.01 #es un flotante y abajo lo paso a entero
z0=linspace(a,b,int(n+1))
for N in array([5,10,15,20]):
    figure()#figure para q para N=5 me de una imagen, para N=10 me de otra  imagen y asi..
    pol=spline_cubico_trozos(exp,a,b,N)#pol inter lineal a trozos, es la funcion no es nada  y me falata evaluarlo en los z0)
    pz0=pol(z0)
    x=linspace(a,b,N+1)#nodos de interpolacion
    plot(z0,exp(z0),z0,pz0,x,exp(x),'o')
    """#coger poli inte ry evaluarlo, esto es si me piden evaluar """
    plot(z0,exp(z0),x,exp(x),x,exp(x),'o') 
    """#esto es lo mismo q la linea anterior, aqui lo q hace es saber como
     pinta python q coge los puntos y une rectas , si no me pide evaluar es
     decir obtener la expresion del poli pues hago esto"""
    #si no me dan f y me dan tabla de datos mi f es el poli de inter 
    #def polInterp(z):
            #return eval_forma_newton(x,y,z)
    #en vex de poner exp pongo polinter(x) o polinter(z0) lo q sea q quiera saber lo q vale el polinter en ese punto        
#no tengo f=>mi poliniomio de f hara de f:
#imagina que te dan dos arrays y no te dan funcion:
