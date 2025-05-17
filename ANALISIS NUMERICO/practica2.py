from pylab import *
from time import perf_counter

######################EJERCICIO 1 a) ###############
print('EJERCICIO 1')
def fun(t,y):
    return -y+exp(-t)*cos(t);


def exacta(t):
    return exp(-t)*sin(t);



def AB2(a,b,fun, N,y0):
    
    y = zeros(N+1)
    t = zeros(N+1)
    f = zeros(N+1)#novedad
    t[0] = a
    h = (b-a)/float(N) 
    y[0] = y0
    f[0] = fun(a,y[0])    
    y[1] = y[0] + h*f[0]#uso euler para arrancar(para hallar el y1 ya que es bipaso),paso de euler para calcular el y1 pq esto es metodo bipaso asi que necesito conocer el y0,y1 
    t[1] = a+h
    f[1] = fun(t[1], y[1])
    for k in range(1,N):#bucle en tiempo, va desde el  1 pq y ahe caluclado el y1 y va hasta N ojo con el detalle, pq llego hasta el k+1
        y[k+1] = y[k]+0.5*h*(3.0*f[k] - f[k-1])
        t[k+1] = t[k] + h
        f[k+1] = fun(t[k+1], y[k+1])#guardo la f para q el programa sea muy eficaz, pq sino hay q evaluarla muchas veces y gasta mucho
        
    return (t,y)


y0 = 0.0
a = 0.0
b = 5.0
N = 30
tini = perf_counter()
(t,y) = AB2(a,b,fun, N,y0)
tfin = perf_counter()
ye = exacta(t)
plot(t,y, '*')
plot(t,ye)
h = (b - a)/float(N)
error = max(abs(y-ye))
tcpu = tfin-tini
print('---------------')
print('h = '+ str(h))
print('Error= '+str(error))
print('Tiempo CPU= '+str(tcpu))
print('---------------')


# Datos del problema
y0 = 0.0
a = 0.0
b = 5.0
malla=[10,20,40,80,160]


for N in malla:
    tini = perf_counter()

    (t, y) = AB2(a, b, fun, N, y0)
    
    
    tfin = perf_counter()
    
    plot(t, y, "-*")
    
    h=(b-a)/float(N)
    
    ye = exacta(t)

    
    # Calculo del error cometido
    error = max(abs(y-ye))
    tcpu=tfin-tini 
    
    print('N = '+str(N))
    print('Error='+str(error))
    print('Tiempo CPU='+str(tcpu))
    
    
    
    if N > malla[0]:
        order=(log(errorold)-log(error))/log(2)
        print('orden aprox ' +str(order))
        
    print('---------------------')
    errorold=error
    

plot(t,ye)
leyenda=['N = '+str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)


######################EJERCICIO 1 b) ###############


def AB3(a, b, fun, N, y0):
    y = zeros(N+1)
    t = zeros(N+1)
    f = zeros(N+1)
    t[0] = a
    h = (b - a) / float(N)
    y[0] = y0
    f[0] = fun(a, y[0])

    for k in range(2):#Usamos un método unipaso (como Runge-Kutta 2) para "arrancar" el método multipaso AB3, porque este último necesita al menos 3 puntos iniciales para funcionar.
        z = y[k] + 0.5 * h * f[k]
        y[k+1] = y[k] + h * fun(t[k] + 0.5 * h, z)
        t[k+1] = t[k] + h
        f[k+1] = fun(t[k+1], y[k+1])

    for k in range(2, N):
        y[k+1] = y[k] + h/12.0 * (23.0 * f[k] - 16.0 * f[k-1] + 5.0 * f[k-2])
        t[k+1] = t[k] + h
        f[k+1] = fun(t[k+1], y[k+1])

    return (t, y)




# Datos del problema
y0 = 0.0
a = 0.0
b = 5.0
malla=[10,20,40,80,160]


for N in malla:
    tini = perf_counter()

    (t, y) = AB3(a, b, fun, N, y0)
    
    
    tfin = perf_counter()
    
    plot(t, y, "-*")
    
    h=(b-a)/float(N)
    
    ye = exacta(t)

    
    # Calculo del error cometido
    error = max(abs(y-ye))
    tcpu=tfin-tini 
    
    print('N = '+str(N))
    print('Error='+str(error))
    print('Tiempo CPU='+str(tcpu))
    
    
    
    if N > malla[0]:
        order=(log(errorold)-log(error))/log(2)
        print('orden aprox ' +str(order))
        
    print('---------------------')
    errorold=error
    

plot(t,ye)
leyenda=['N = '+str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)

######################EJERCICIO 1 c) ###############
print('---- Comparación de coste computacional ----')

# Método unipaso (RK2) puro
def RK2(a, b, fun, N, y0):
    y = zeros(N+1)
    t = zeros(N+1)
    h = (b - a)/float(N)
    t[0] = a
    y[0] = y0
    for k in range(N):
        z = y[k] + 0.5 * h * fun(t[k], y[k])
        t[k+1] = t[k] + h
        y[k+1] = y[k] + h * fun(t[k] + 0.5 * h, z)
    return t, y

# Unipaso (RK2)
N = 3000
tini = perf_counter()
t_rk, y_rk = RK2(a, b, fun, N, y0)
tfin = perf_counter()
error_rk = max(abs(y_rk - exacta(t_rk)))
print(f"[RK2] Error = {error_rk}, Tiempo = {tfin - tini:.5f} s")

# Multipaso (AB3)
tini = perf_counter()
t_ab, y_ab = AB3(a, b, fun, N, y0)
tfin = perf_counter()
error_ab = max(abs(y_ab - exacta(t_ab)))
print(f"[AB3] Error = {error_ab}, Tiempo = {tfin - tini:.5f} s")
# el método AB3 calcula mejores aproximaciones en menos tiempo que el método de Heun y el de punto medio



######################EJERCICIO 2 a) ###############
print('EJERCICIO 2')
#elaboramos el AM3 para problemas lienales
#este solo sirve cuando f es lineal, si f no es lienal no lo puedo usar

def AM3_flineal(a, b, fun, N, y0): # Lo apellido _2a porque no sirve en el caso general (ver apartado siguiente)
    y = zeros(N+1)
    t = zeros(N+1)
    f = zeros(N+1)
    h = (b - a)/float(N) 
    t[0] = a
    y[0] = y0
    f[0] = fun(a, y[0])
    for k in range(2): # como el método AM3 es de orden 4, hay que hallar y_1 e y_2 con un método unipaso de orden >= 3
        t[k+1] = t[k] + h
        k1 = fun(t[k], y[k])
        k2 = fun(t[k] + h/2, y[k] + h/2*k1)
        k3 = fun(t[k] + h/2, y[k] + h/2*k2)
        k4 = fun(t[k+1], y[k] + h*k3)
        y[k+1] = y[k] + h/6*(k1 + 2*k2 + 2*k3 + k4)
        f[k+1] = fun(t[k+1], y[k+1]) # MUY IMPORTANTE: siempre se me olvida esta línea
    for k in range(2, N):
        t[k+1] = t[k] + h
        Ck = y[k] + h/24*(19*f[k] - 5*f[k-1] + f[k-2])
        y[k+1] = (9/24*h*exp(-t[k+1])*cos(t[k+1]) + Ck)/(1 + 9/24*h)
        f[k+1] = fun(t[k+1], y[k+1])
    return (t, y)


# Datos del problema
y0 = 0.0
a = 0.0
b = 5.0
malla=[10,20,40,80,160]


for N in malla:
    tini = perf_counter()

    (t, y) = AM3_flineal(a, b, fun, N, y0)
    
    
    tfin = perf_counter()
    
    plot(t, y, "-*")
    
    h=(b-a)/float(N)
    
    ye = exacta(t)

    
    # Calculo del error cometido
    error = max(abs(y-ye))
    tcpu=tfin-tini 
    
    print('N = '+str(N))
    print('Error='+str(error))
    print('Tiempo CPU='+str(tcpu))
    
    
    
    if N > malla[0]:
        order=(log(errorold)-log(error))/log(2)
        print('orden aprox ' +str(order))
        
    print('---------------------')
    errorold=error
    

plot(t,ye)
leyenda=['N = '+str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)


######################EJERCICIO 2 B) ###############

def AM3_generico(a, b, fun, N, y0):
    tol=1.e-12
    nmax=200
    y = zeros(N+1)
    t = zeros(N+1)
    f = zeros(N+1)
    h = (b - a)/float(N) 
    t[0] = a
    y[0] = y0
    f[0] = fun(a, y[0])
    maxiter = 0
    for k in range(2):#usamos rk4 pq el orden de am3 es 4
        t[k+1] = t[k] + h
        k1 = fun(t[k], y[k])
        k2 = fun(t[k] + h/2, y[k] + h/2*k1)
        k3 = fun(t[k] + h/2, y[k] + h/2*k2)
        k4 = fun(t[k+1], y[k] + h*k3)
        y[k+1] = y[k] + h/6*(k1 + 2*k2 + 2*k3 + k4)
        f[k+1] = fun(t[k+1], y[k+1])
    for k in range(2, N):
        Ck = y[k] + h/24*(19*f[k] - 5*f[k-1] + f[k-2])#ojo con tk
        t[k+1] = t[k] + h
        dist = tol + 1
        count = 0
        z = y[k]
        while(dist >tol and count < nmax):
            znew = 9/24*h*fun(t[k+1], z) + Ck
            dist = abs(z - znew)
            count += 1
            z = znew

        if count == nmax:
            print('El método de punto fijo no ha convergido')
        maxiter = max(maxiter, count)
        y[k+1] = z
        f[k+1] = fun(t[k+1], y[k+1])
    return (t, y, maxiter)


y0 = 0.0
a = 0.0
b = 5.0
malla=[10,20,40,80,160]

figure()

for N in malla:
    tini = perf_counter()

    (t, y, maxiter) = AM3_generico(a, b, fun, N, y0)
    
    
    tfin = perf_counter()
    plot(t, y, "-*")
    
    h=(b-a)/float(N)
    
    ye = exacta(t)

    
    # Calculo del error cometido
    error = max(abs(y-ye))
    tcpu=tfin-tini 
    
    print('N = '+str(N))
    print('Error='+str(error))
    print('Tiempo CPU='+str(tcpu))
    print('Máximo número de iteraciones de punto fijo: ' + str(maxiter))

    
    
    if N > malla[0]:
        order=(log(errorold)-log(error))/log(2)
        print('orden aprox ' +str(order))
    print('---------------------')
    errorold=error
    

plot(t,ye)
leyenda=['N = '+str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)
   

# el número máximo de iteraciones va decreciendo porque la semilla mejora cuando el paso de malla se hace pequeño

######################EJERCICIO 2 C) ###############


def AM3_Newton(a, b, fun, N, y0):
    tol=1.e-12
    nmax=200
    y = zeros(N+1)
    t = zeros(N+1)
    f = zeros(N+1)
    h = (b - a)/float(N) 
    t[0] = a
    y[0] = y0
    f[0] = fun(a, y[0])
    maxiter = 0
    for k in range(2):#usamos rk4 pq el orden de am3 es 4
        t[k+1] = t[k] + h
        k1 = fun(t[k], y[k])
        k2 = fun(t[k] + h/2, y[k] + h/2*k1)
        k3 = fun(t[k] + h/2, y[k] + h/2*k2)
        k4 = fun(t[k+1], y[k] + h*k3)
        y[k+1] = y[k] + h/6*(k1 + 2*k2 + 2*k3 + k4)
        f[k+1] = fun(t[k+1], y[k+1])
    for k in range(2, N):
        t[k+1] = t[k] + h
        Ck = y[k] + h/24*(19*f[k] - 5*f[k-1] + f[k-2])#ojo con tk, siempre ponerlo primero mejor
        dist = tol + 1
        count = 0
        z = y[k]
        while(dist >tol and count < nmax):
            F = z - 9*h/24*fun(t[k+1], z) - Ck # al escribir 9*24/h y 9*h/24 pueden obtenerse resultados ligeramente distintos
            dF = 1 - 9*h/24*dyfun(t[k+1], z)
            znew = z - F/dF
            dist = abs(z - znew)
            count += 1
            z = znew

        if count == nmax:
            print('El método de punto fijo no ha convergido')
        maxiter = max(maxiter, count)
        y[k+1] = z
        f[k+1] = fun(t[k+1], y[k+1])
    return (t, y, maxiter)


def dyfun(t, y): # derivada parcial de f(t,y) = -y + e^{-t}cos(t) con respecto a y
    return -1

y0 = 0.0
a = 0.0
b = 5.0
malla=[10,20,40,80,160]

figure()

for N in malla:
    tini = perf_counter()

    (t, y, maxiter) = AM3_Newton(a, b, fun, N, y0)
    
    
    tfin = perf_counter()
    plot(t, y, "-*")
    
    h=(b-a)/float(N)
    
    ye = exacta(t)

    
    # Calculo del error cometido
    error = max(abs(y-ye))
    tcpu=tfin-tini 
    
    print('N = '+str(N))
    print('Error='+str(error))
    print('Tiempo CPU='+str(tcpu))
    print('Máximo número de iteraciones de punto fijo: ' + str(maxiter))

    
    
    if N > malla[0]:
        order=(log(errorold)-log(error))/log(2)
        print('orden aprox ' +str(order))
    print('---------------------')
    errorold=error
    

plot(t,ye)
leyenda=['N = '+str(N) for N in malla]
leyenda.append('exacta')
legend(leyenda)
   

# el número máximo de iteraciones va decreciendo porque la semilla mejora cuando el paso de malla se hace pequeño


######################EJERCICIO 2  D) ###############
print('\n\n\nEJERCICIO 2(d.i)')

def fun2(t,y):
    return 1+y**2;


def exacta2(t):
    return tan(t);

def dyfun(t, y): # derivada parcial de f(t,y) = -y + e^{-t}cos(t) con respecto a y
    return 2*y

y0 = 0.0
a = 0.0
b = 1.0
N=320
figure('EJERCICIO 2(d.i)')

tini = perf_counter()

(t, y, maxiter) = AM3_generico(a, b, fun2, N, y0)


tfin = perf_counter()
plot(t, y, "-*")

h=(b-a)/float(N)

ye = exacta2(t)


# Calculo del error cometido
error = max(abs(y-ye))
tcpu=tfin-tini 

print('N = '+str(N))
print('Error='+str(error))
print('Tiempo CPU='+str(tcpu))
print('Máximo número de iteraciones de punto fijo: ' + str(maxiter))



plot(t,ye)
leyenda=['N = 320']
leyenda.append('exacta')
legend(leyenda)

print('\n\n\nEJERCICIO 2(d.i)')

y0 = 0.0
a = 0.0
b = 1.0
N=320
figure('EJERCICIO 2(d.ii)')

tini = perf_counter()

(t, y, maxiter) = AM3_Newton(a, b, fun2, N, y0)


tfin = perf_counter()
plot(t, y, "-*")

h=(b-a)/float(N)

ye = exacta2(t)


# Calculo del error cometido
error = max(abs(y-ye))
tcpu=tfin-tini 

print('N = '+str(N))
print('Error='+str(error))
print('Tiempo CPU='+str(tcpu))
print('Máximo número de iteraciones de punto fijo: ' + str(maxiter))



plot(t,ye)
leyenda=['N = 320']
leyenda.append('exacta')
legend(leyenda)
   
