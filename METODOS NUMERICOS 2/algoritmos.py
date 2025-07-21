# -*- coding: utf-8 -*-
from numpy import *
from numpy.linalg import *
from numpy import abs, sum, max, min

def conjugada(A):
	nd=ndim(A)
	if nd==1:
		AA=array([A])
	elif nd==2:
		AA=array(A)#array A es lo mismo q decir A
	else:
		print("error conjugada:argumento de entrada")
		AA=0;
	return conjugate(transpose(AA))

def norma_vec(X, p):
    nd=ndim(X)
    if nd!=1:
        col=shape(X)[1]
        if nd!=1 and (nd!=2 or col!=1):
            return "Error norma_vec: tipo de X."
        XX=array(X,dtype=complex)
        normainf=max(abs(XX))
        if p==inf:
            return normainf
        elif p>=1:
            if normainf<1e-100:
                return sum(abs(XX)**p)**(1/p)
            else:
                return normainf*sum((abs(XX)/normainf)**p)**(1/p)
        else:
            return "Error norma_vec: valor de p."

def conv_norma_vec(X):
    print("Vector: X = ", X)
    normainf = norma_vec(X, inf)
    print("||X||_inf = ", normainf)
    error = 1.
    p = 0
    while error >= 1e-10 and p < 200:
        p = p+1
        normap = norma_vec(X, p)
#         normap = norm(X, p)
        error = abs((normap - normainf)/normainf)
        print("p = ", p, " ||X||_p = ", normap, " Error relativo = ", error)
    if error < 1e-10:
        print("Convergencia numérica alcanzada.")
    else:
        print("Número máximo de iteraciones alcanzado.")
        
def norma_mat(A, p):
    nd = ndim(A)
    if nd == 2:
        m, n = shape(A)
    if nd != 2 or m != n:
        return "Error norma_mat: tipo de A."
    AA = array(A, dtype=complex)
    if p == inf:
        return max(sum(abs(AA),axis=1))
    elif p == 1:
        return max(sum(abs(AA),axis=0))
    elif p == 2:
        return max(svd(AA)[1])
#         return ...
    elif p == 'fro':
        return (sum(abs(AA)**2))**.5
    else:
        return "Error norma_mat: valor de p."
    
def descenso(A, B):
    m, n = shape(A)
    p, q = shape(B)
    if m != n or n != p or q <1:
        return False, "Error descenso: error en las dimensiones."
    if min(abs(diag(A))) < 1e-200:
        return False, "Error descenso: matriz singular."
    if A.dtype == complex or B.dtype == complex:
        X = zeros((n, q), dtype=complex)
    else:
        X = zeros((n, q), dtype=float)
    for i in range(n):
        X[i, :] = B[i, :]
        if i != 0:
            X[i, :] -= A[i, :i]@X[:i, :]
        X[i, :] = X[i, :]/A[i, i]
    return True, X

def remonte(A, B):
    m, n = shape(A)
    p, q = shape(B)
    if m != n or n != p or q < 1:
        return False, "Error remonte: error en las dimensiones."
    if min(abs(diag(A))) < 1e-200:
        return False, "Error remonte: matriz singular."
    if A.dtype == complex or B.dtype == complex:
        X = zeros((n, q), dtype=complex)
    else:
        X = zeros((n, q), dtype=float)
    for i in range(n-1,-1,-1): #va desde n-1 hasta 0 (-1 excluido) con saltos de -1.
        X[i, :] = B[i, :]
        if i != n-1:
            X[i, :] -= A[i, i+1:]@X[i+1:, :]
        X[i, :] = X[i, :]/A[i, i]
    return True, X

def descenso1(A, B):
    m, n = shape(A)
    p, q = shape(B)
    if m != n or n != p or q <1:
        return False, "Error descenso: error en las dimensiones."
   # if min(abs(diag(A))) < 1e-200:
      #  return False, "Error descenso: matriz singular."    esto lo quitamos porque sabemos que la matriz A no es singular
    if A.dtype == complex or B.dtype == complex:
        X = zeros((n, q), dtype=complex)
    else:
        X = zeros((n, q), dtype=float)
    for i in range(n):
        X[i, :] = B[i, :]
        if i != 0:
            X[i, :] -= A[i, :i]@X[:i, :]
       # X[i, :] = X[i, :]/A[i, i]  quitamos esta linea porque no hace falta dividir por 1
    return True, X

def remonte1(A, B):
    m, n = shape(A)
    p, q = shape(B)
    if m != n or n != p or q < 1:
        return False, "Error remonte: error en las dimensiones."
   # if min(abs(diag(A))) < 1e-200:
       # return False, "Error remonte: matriz singular."
    if A.dtype == complex or B.dtype == complex:
        X = zeros((n, q), dtype=complex)
    else:
        X = zeros((n, q), dtype=float)
    for i in range(n-1,-1,-1): #va desde n-1 hasta 0 (-1 excluido) con saltos de -1.
        X[i, :] = B[i, :]
        if i != n-1:
            X[i, :] -= A[i, i+1:]@X[i+1:, :]
       # X[i, :] = X[i, :]/A[i, i]
    return True, X

def descenso_1diag(A, B):
    m, n = shape(A)
    p, q = shape(B)
    if m != n or n != p or q <1:
        return False, "Error descenso: error en las dimensiones."
    if min(abs(diag(A))) < 1e-200:
        return False, "Error descenso: matriz singular."
    if A.dtype == complex or B.dtype == complex:
        X = zeros((n, q), dtype=complex)
    else:
        X = zeros((n, q), dtype=float)
    for i in range(n):
        X[i, :] = B[i, :]
        if i != 0:
            X[i, :] -= A[i, i-1]*X[i-1, :] #cuando se pone A[i,:i] significa que recorre la fila i desde el principio hasta la columna i
        X[i, :] = X[i, :]/A[i, i]
    return True, X

def remonte_1diag(A, B):
    m, n = shape(A)
    p, q = shape(B)
    if m != n or n != p or q < 1:
        return False, "Error remonte: error en las dimensiones."
    if min(abs(diag(A))) < 1e-200:
        return False, "Error remonte: matriz singular."
    if A.dtype == complex or B.dtype == complex:
        X = zeros((n, q), dtype=complex)
    else:
        X = zeros((n, q), dtype=float)
    for i in range(n-1,-1,-1): #va desde n-1 hasta 0 (-1 excluido) con saltos de -1.
        X[i, :] = B[i, :]
        if i != n-1:
            X[i, :] -= A[i, i+1]*X[i+1, :]
        X[i, :] = X[i, :]/A[i, i]
    return True, X

def gauss_pp(A, B):
    m, n = shape(A)
    p, q = shape(B)
    if m != n or n != p or q < 1:
        return False, "Error gauss_pp: error en las dimensiones."
    if A.dtype == complex or B.dtype == complex:
        gaussA = array(A, dtype=complex)
        gaussB = array(B, dtype=complex)
    else:
        gaussA = array(A, dtype=float)
        gaussB = array(B, dtype=float)
    for k in range(n-1):
        pos = argmax(abs(gaussA[k:, k]))#me da la pos de dn se encuentra el mayor valor del vector
        ik = pos+k#argmax me devolvia el max del vector q le paso y ese no empezaba en 0 asi q le tengo q sumar k para q sea la pos de l amatriz sacada a partir del max del vector q es la columna
        if ik != k:
            gaussA[[ik, k], :] = gaussA[[k, ik], :]#permutacion de columnas
            gaussB[[ik, k], :] = gaussB[[k, ik], :]
        #hacemos ceros
        #se mten los coientes dn habia 0
        if abs(gaussA[k, k]) >= 1e-200:#mira q pivot sea suf grande,pq si la matriz es singular pues no tengo q hacer nada, si el abs es 0 entonces es singular y no hay nada q hacer asi q no hago esto pq seria operaciones ineficientes y qme las puedo ahorra
            for i in range(k+1, n):
                gaussA[i, k] = gaussA[i, k]/gaussA[k, k]
                gaussA[i, k+1:] -= gaussA[i, k]*gaussA[k, k+1:]
                gaussB[i, :] -= gaussA[i, k]*gaussB[k, :]
    exito, X = remonte(gaussA, gaussB)
    return exito, X

def gaussjordan_pp(A, B):
    m, n = shape(A)
    p, q = shape(B)
    if m != n or n != p or q < 1:
        return False, "Error gaussjordan_pp: error en las dimensiones."
    if A.dtype == complex or B.dtype == complex:
        gaussA = array(A, dtype=complex)
        gaussB = array(B, dtype=complex)
    else:
        gaussA = array(A, dtype=float)
        gaussB = array(B, dtype=float)
    for k in range(n):#pq metodo de gauss tiene n iteraciones
        pos = argmax(abs(gaussA[k:, k]))#me da la pos de dn se encuentra el mayor valor del vector
        ik = pos+k#argmax me devolvia el max del vector q le paso y ese no empezaba en 0 asi q le tengo q sumar k para q sea la pos de l amatriz sacada a partir del max del vector q es la columna
        if ik != k:
            gaussA[[ik, k], :] = gaussA[[k, ik], :]#permutacion de columnas
            gaussB[[ik, k], :] = gaussB[[k, ik], :]
        if abs(gaussA[k, k]) >= 1e-200:#mira q pivot sea suf grande,pq si la matriz es singular pues no tengo q hacer nada, si el abs es 0 entonces es singular y no hay nada q hacer asi q no hago esto pq seria operaciones ineficientes y qme las puedo ahorra
            #cambio los de la parte triangular superior 
            for i in range(k):#de 0 a k-1
                gaussA[i, k] = gaussA[i, k]/gaussA[k, k]
                gaussA[i, k+1:] -= gaussA[i, k]*gaussA[k, k+1:]
                gaussB[i, :] -= gaussA[i, k]*gaussB[k, :]
            for i in range(k+1, n):
                gaussA[i, k] = gaussA[i, k]/gaussA[k, k]
                gaussA[i, k+1:] -= gaussA[i, k]*gaussA[k, k+1:]
                gaussB[i, :] -= gaussA[i, k]*gaussB[k, :]
    if(min(abs(diag(gaussA))))<1e-200:
        return False, "error gausjordan matriz sing"
    if A.dtype==complex or B.dtype==complex:
        X=zeros((n,q),dtype=complex)
    else:
        X=zeros((n,q),dtype=float)
    for i in range(n):
        X[i,:]=gaussB[i,:]/gaussA[i,i]
    
    return exito, X

def facto_lu(A):#analogo q el de gauss
    m, n = shape(A)
    if m != n:
        return False, "Error facto_lu: error en las dimensiones."
    if A.dtype == complex:
        lu = array(A, dtype=complex)
    else:
        lu = array(A, dtype=float)
    for k in range(n-1):
        if abs(lu[k, k]) < 1e-200:#comprobacion de q las submatrices principales son inversibles, si algun elem de la diag es 0, entonces alguna submatriz no es inversible pq tiene 0 en diag,entonces 0 en diag entonces 0 es autovalor entonces no seria inversible y sabemos por teo q la facto lu existe si y solo si las submatrices princi son inversibles
            return False, "Error facto_lu: no existe la factorización."
        else:
            for i in range(k+1, n):
                lu[i, k] = lu[i, k]/lu[k, k]
                lu[i, k+1:] -= lu[i, k]*lu[k, k+1:]
    return True, lu

def metodo_lu(A, B):
    exito,lu=facto_lu(A)
    if exito:
        exito2,Y=descenso1(lu,B)
        if exito2:
            exito3,X=remonte(lu,Y)
        else:
            exito3=False
        if exito2 and exito3:
            return True,X
        else:
            return False,"Error metodo_lu:error en la resolucion"
    else:
        return False,lu


def facto_cholesky(A):
    m, n = shape(A)
    if m != n:
        return False, "Error facto_cholesky: error en las dimensiones."
    if A.dtype == complex:
        return False, "Error facto_cholesky: matriz compleja."
    else:
        chol = array(A, dtype=float)
    for i in range(n):
        chol[i, i] -= sum(power(chol[i, 0:i], 2))
        if chol[i, i] >= 1e-100:
            chol[i, i] = sqrt(chol[i, i])
        else:
            return False, "Error facto_cholesky: no se factoriza la matriz"
        for j in range(i+1, n):
            chol[j, i] -= sum(chol[i, 0:i]*chol[j, 0:i])
            chol[j, i] = chol[j, i]/chol[i, i]
            chol[i, j] = chol[j, i]
    return True, chol


def metodo_cholesky(A, B):
    exito,lu=facto_cholesky(A)
    if exito:
        exito2,Y=descenso(lu,B)#descenso 1 asumia q en la diag habia unos pero aqui no tengo eso asi q uso descenso
        if exito2:
            exito3,X=remonte(lu,Y)
        else:
            exito3=False
        if exito2 and exito3:
            return True,X
        else:
            return False,"Error metodo_lu:error en la resolucion"
    else:
        return False,lu