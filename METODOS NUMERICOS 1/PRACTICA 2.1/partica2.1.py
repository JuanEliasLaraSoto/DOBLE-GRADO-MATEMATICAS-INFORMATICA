# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 18:33:09 2023

@author: Msi
"""

from numpy import *
from matplotlib.pyplot import *

# -*- coding: utf-8 -*-
print('apartado a)')
def bisec(f,a,b,N):#N es el num de iteraciones q quiero q haga
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
    for k in range(N):
        cn=(an+bn)/2.#para q haga la division en unflotante
        fcn=f(cn)
        print('iter', k+1,'c=',cn,'fn=', fcn)
        if fcn==0:
            print(str(cn)+'es raíz de la función')
            return cn
        elif fan*fcn<0:
            bn=cn
            fbn=fcn
        else:
            an=cn
            fan=fcn
    print('La aproximación de la raíz tras '+str(N)+' iteraciones es '+str(cn))#ojo con el sangrado d este pritn pq se pone este print solo al final
    return cn
print('apartado b)')
def f1(x):
    return x**5-5*x**3+1 
#la dibuja para verlo mejor
x=linspace(-3,3,100)
figure()
plot(x,f1(x))
plot(x,0*x)#0*x pq necesito un vector y no puedo ponersolo 0

bisec(f1,0,1,20)
bisec(f1,-3,-2,20)

print('apartado c')
def f2(x):
        return cos(x)-x

figure()
x=linspace(-3,3,100)
plot(x,f2(x))
plot(x,0*x)#eje x


bisec(f2,0.5,1,20)

print('apartado d')
def bisec_mod(f,a,b,eps):
    N=int((log(b-a)-log(eps))/log(2))+1 
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
    for k in range(N):
        cn=(an+bn)/2.#para q haga la division en unflotante
        fcn=f(cn)
        print('iter', k+1,'c=',cn,'fn=', fcn)
        if fcn==0:
            print(str(cn)+'es raíz de la función')
            return cn
        elif fan*fcn<0:
            bn=cn
            fbn=fcn
        else:
            an=cn
            fan=fcn
    print('La aproximación de la raíz tras '+str(N)+' iteraciones es '+str(cn))#ojo con el sangrado d este pritn pq se pone este print solo al final
    return cn


print('apartado e')
bisec_mod(f2,0.5,1,1e-7)#si pones 10e-7=1e-6 y eso no es lo q quiero

print('Ejerccio 2')

def regula_falsi(f,a,b,eps,nmax):
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
    error =eps+1
    it=0
    while(error>eps and it<nmax):
        cn=bn-(bn-an)/(fbn-fan)*fbn
        fcn=f(cn)
        print('iter', it,'c=',cn,'fn=', fcn)
        error=abs(fcn)
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
        if error<=eps:
            print('Se ha alcanzado una aproximacion satisfactoria')
        else:
            print('Se ha alcanzado el numerO MAXIMO DE ITERACIONES')
        
    print('la aprox de la raiz con cota de error' +str(eps)+'es'+str(cn) + 'it'+str(it) )
    print('la aprox de la raiz tras ' , it, 'iteracion'+'es'+str(cn) )
#ojo con el sangrado d este pritn pq se pone este print solo al final
    return cn
print('apartado d')
regula_falsi(f2,0.5,1,1e-7,50)



print('apartado a')
def regula_falsi_mod(f,a,b,eps,nmax):
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
    #cn_old=pq enun dice q lo mas seguro es q la raiz se acerque mas a a, ojo q si pongo q es 0 pues mal pq yo no se q entre a y b esta el 0 asi q como cn esta entre a y b ps eso es fallo pq cn puede q no sea 0 nunca y yo lo estoy suponiendo
    it=0
    error=eps+1#para q entre la primera vez
    while(error>eps and it<nmax):
        cn=bn-(bn-an)/(fbn-fan)*fbn
        fcn=f(cn)
        print('iter', it,'c=',cn,'fn=', fcn)
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
    if error<=eps:
        print('Se ha alcanzado una aproximacion satisfactoria')
    else:
        print('Se ha alcanzado el numerO MAXIMO DE ITERACIONES')
            
    print('la aprox de la raiz con cota de error' +str(eps)+'es'+str(cn) + 'it'+str(it) )
    print('la aprox de la raiz tras ' , it, 'iteracion'+'es'+str(cn) )
   #ojo con el sangrado d este pritn pq se pone este print solo al final
    return cn
print('apartado b')
regula_falsi_mod(f2,0.5,1,1e-7,50)



print('ej 3')
print('apar a')
def secante(f,x0,x1,eps,nmax):
    fx0=f(x0)
    fx1=x1
    fx0=f(x0)#lo guarda para q no sea tan costoso, llamar a f todo el rato
    fx1=f(x1)
    if fx0==0:
        print(str(x0)+'es raíz de la función')#puedo poner tb a+'es raiz de la fun'
        return x0
    elif fx1==0:
        print(str(x1)+'es raíz de la función')
        return x1
    
    it=0
    error=eps+1
    while(error>eps and it<nmax):
        if fx0==fx1:
            print('No hay cambio de signo: no se puede aplicar el método')
            return#return q no devuelve nada para acabar el programa
        x2=x1-(x1-x0)/(fx1-fx0)*fx1
        fx2=f(x2)
        print('iter', it,'x=',x,'fx=', fx2)
        error=abs(x2-x1)
        it+=1 
        if fx2==0:
            print(str(x2)+'es raíz de la función')
            return x2
        #se prepara para siguiente it
        x0=x1
        x1=x2
        fx0=fx1
        fx1=fx2
    if error<=eps:
        print('Se ha alcanzado una aproximacion satisfactoria '+str(it)+' iteraciones')
    else:
        print('Se ha alcanzado el numerO MAXIMO DE ITERACIONES')
            
    print('la aprox de la raiz tras con cota de error ' , str(eps), 'es'+str(x2) )
   #ojo con el sangrado d este pritn pq se pone este print solo al final
    return x2
print('apartado b')
secante(f2,0.5,1,1e-7,50)
print('apartado c')
def secante_mod(f,x0,x1,eps,nmax):
    fx0=f(x0)
    fx1=x1
    fx0=f(x0)#lo guarda para q no sea tan costoso, llamar a f todo el rato
    fx1=f(x1)
    if fx0==0:
        print(str(x0)+'es raíz de la función')#puedo poner tb a+'es raiz de la fun'
        return x0
    elif fx1==0:
        print(str(x1)+'es raíz de la función')
        return x1
    
    it=0
    error=eps+1
    while(error>eps and it<nmax):
        if fx0==fx1:
            print('No hay cambio de signo: no se puede aplicar el método')
            return#return q no devuelve nada para acabar el programa
        x2=x1-(x1-x0)/(fx1-fx0)*fx1
        fx2=f(x2)
        print('iter', it,'x=',x,'fx=', fx2)
        error=abs(x2-x1)
        it+=1 
        if fx2==0:
            print(str(x2)+'es raíz de la función')
            return x2
        #se prepara para siguiente it
        if(abs(fx2)<=eps):
            print(str(x2)+'es una aprox con  |fx|<'+str(eps))
            return x2 
        x0=x1
        x1=x2
        fx0=fx1
        fx1=fx2
        if error<=eps:
            print('Se ha alcanzado una aproximacion satisfactoria '+str(it)+' iteraciones')
        else:
            print('Se ha alcanzado el numerO MAXIMO DE ITERACIONES')
            
    print('la aprox de la raiz tras con cota de error ' , str(eps), 'es'+str(x2) )
   #ojo con el sangrado d este p ritn pq se pone este print solo al final
    return x2
print('apartado d')
secante_mod(f2,0.5,1,1e-5,50)
print('ej1bclase')
def f3(x):
    return x**3-x-1 
secante(f3, 1, 2, 1e-5, 50)
print('ej 3 clase')
def f4(x):
    return (x+sqrt(x))*(20-x+sqrt(20-x))-155
secante(f4, 6, 7, 1e-4, 50)

