import funciones_rsa as f

""" Crear una clave pública y una clave privada RSA de 2048 bits para Alice. Guardar
cada clave en un fichero. """

""" Crear una clave pública y una clave privada RSA de 2048 bits para Bob. Guardar
cada clave en un fichero. """

k1=f.crear_RSAKey()
k2=f.crear_RSAKey()

f.guardar_RSAKey_Privada("privAli.txt",k1,"betis")
f.guardar_RSAKey_Publica("pubAli.txt",k1)
f.guardar_RSAKey_Privada("privBobi.txt",k2,"betisole")
f.guardar_RSAKey_Publica("pubBobi.txt",k2)