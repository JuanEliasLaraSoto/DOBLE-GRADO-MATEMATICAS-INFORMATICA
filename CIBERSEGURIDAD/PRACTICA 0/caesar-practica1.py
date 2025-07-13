print("EJERCICIO 1")

def cifradoCesarAlfabetoInglesMAY(cadena):
				"""Devuelve	un	cifrado	Cesar	tradicional	(+3)"""
				#	Definir	la	nueva	cadena	resultado
				resultado	=	''
				#	Realizar	el	"cifrado",	sabiendo	que	A	=	65,	Z	=	90,	a	=	97,	z	=	122
				i	=	0
				while i	<	len(cadena):
								#	Recoge	el	caracter	a	cifrar
								ordenClaro	=	ord(cadena[i])
								ordenCifrado	=	0
								#	Cambia	el	caracter	a	cifrar
								if (ordenClaro	>=	65 and ordenClaro	<=	90):
												ordenCifrado	=	(((ordenClaro	- 65)	+	3)	%	26)	+	65
								#	Añade	el	caracter	cifrado	al	resultado
								resultado	=	resultado	+	chr(ordenCifrado)
								i	=	i	+	1
				#	devuelve	el	resultado
				return resultado

claroCESARMAY='ARX VIDI ENVIDI KOLI'
print(claroCESARMAY)
cifradoCESARMAY=cifradoCesarAlfabetoInglesMAY(claroCESARMAY)
print(cifradoCESARMAY)

#def cifradoCesarAlfabetoInglesMAY(cadena,desp):
#ord de caract da numasci
#chr de num me da caract
def descifradoCesarAlfabetoInglesMAY(cadena):
				"""Devuelve	un	cifrado	Cesar	tradicional	(+3)"""
				#	Definir	la	nueva	cadena	resultado
				resultado	=	''
				#	Realizar	el	"cifrado",	sabiendo	que	A	=	65,	Z	=	90,	a	=	97,	z	=	122
				i	=	0
				while i	<	len(cadena):
								#	Recoge	el	caracter	a	cifrar
								ordenClaro	=	ord(cadena[i])
								ordenCifrado	=	0
								#	Cambia	el	caracter	a	cifrar
								
									
								if (ordenClaro	>=	65 and ordenClaro	<=	90):
												ordenCifrado	=	(((ordenClaro	- 65)	-	3)	%	26)	+	65
								#	Añade	el	caracter	cifrado	al	resultado
								if (ordenClaro==0):
									resultado	=	resultado	+	' '
								else:
									resultado	=	resultado	+	chr(ordenCifrado)
								i	=	i	+	1
				#	devuelve	el	resultado
				return resultado



descifradoCESARMAY=descifradoCesarAlfabetoInglesMAY(cifradoCESARMAY)
print(descifradoCESARMAY)

print("EJERCICIO 2")

def cifradoCesarAlfabetoInglesMAYMIN(cadena):
				"""Devuelve	un	cifrado	Cesar	tradicional	(+3)"""
				#	Definir	la	nueva	cadena	resultado
				resultado	=	''
				#	Realizar	el	"cifrado",	sabiendo	que	A	=	65,	Z	=	90,	a	=	97,	z	=	122
				i	=	0
				while i	<	len(cadena):
								#	Recoge	el	caracter	a	cifrar
								ordenClaro	=	ord(cadena[i])
								ordenCifrado	=	0
								#	Cambia	el	caracter	a	cifrar
								if (ordenClaro	>=	65 and ordenClaro	<=	90):
												ordenCifrado	=	(((ordenClaro	- 65)	+	3)	%	26)	+	65
								elif ((ordenClaro	>=	97 and ordenClaro	<=	122 )):
												ordenCifrado	=	(((ordenClaro	- 97)	+	3)	%	26)	+	97
								#	Añade	el	caracter	cifrado	al	resultado
								resultado	=	resultado	+	chr(ordenCifrado)
								i	=	i	+	1
				#	devuelve	el	resultado
				return resultado

claroCESARMAY='jjhh jjk j lolol lolo'
print(claroCESARMAY)
cifradoCESARMAY=cifradoCesarAlfabetoInglesMAYMIN(claroCESARMAY)
print(cifradoCESARMAY)

#def cifradoCesarAlfabetoInglesMAY(cadena,desp):
#ord de caract da numasci
#chr de num me da caract
def descifradoCesarAlfabetoInglesMAYMIN(cadena):
				"""Devuelve	un	cifrado	Cesar	tradicional	(+3)"""
				#	Definir	la	nueva	cadena	resultado
				resultado	=	''
				#	Realizar	el	"cifrado",	sabiendo	que	A	=	65,	Z	=	90,	a	=	97,	z	=	122
				i	=	0
				while i	<	len(cadena):
								#	Recoge	el	caracter	a	cifrar
								ordenClaro	=	ord(cadena[i])
								ordenCifrado	=	0
								#	Cambia	el	caracter	a	cifrar
								
									
								if ((ordenClaro	>=	65 and ordenClaro	<=	90 )):
												ordenCifrado	=	(((ordenClaro	- 65)	-	3)	%	26)	+	65
								elif ((ordenClaro	>=	97 and ordenClaro	<=	122 )):
												ordenCifrado	=	(((ordenClaro	- 97)	-	3)	%	26)	+	97
								#	Añade	el	caracter	cifrado	al	resultado
								if (ordenClaro==0):
									resultado	=	resultado	+	' '
								else:
									resultado	=	resultado	+	chr(ordenCifrado)
								i	=	i	+	1
				#	devuelve	el	resultado
				return resultado



descifradoCESARMAY=descifradoCesarAlfabetoInglesMAYMIN(cifradoCESARMAY)
print(descifradoCESARMAY)


print("EJERCICIO 3")
def cifradoCesarAlfabetoInglesMAYMINDESP(cadena,desp):
				"""Devuelve	un	cifrado	Cesar	tradicional	(+3)"""
				#	Definir	la	nueva	cadena	resultado
				resultado	=	''
				#	Realizar	el	"cifrado",	sabiendo	que	A	=	65,	Z	=	90,	a	=	97,	z	=	122
				i	=	0
				while i	<	len(cadena):
								#	Recoge	el	caracter	a	cifrar
								ordenClaro	=	ord(cadena[i])
								ordenCifrado	=	0
								#	Cambia	el	caracter	a	cifrar
								if (ordenClaro	>=	65 and ordenClaro	<=	90):
												ordenCifrado	=	(((ordenClaro	- 65)	+	desp)	%	26)	+	65
								elif ((ordenClaro	>=	97 and ordenClaro	<=	122 )):
												ordenCifrado	=	(((ordenClaro	- 97)	+	desp)	%	26)	+	97
								#	Añade	el	caracter	cifrado	al	resultado
								resultado	=	resultado	+	chr(ordenCifrado)
								i	=	i	+	1
				#	devuelve	el	resultado
				return resultado

claroCESARMAY='jjhh jjk j lolol lolo'
print(claroCESARMAY)
cifradoCESARMAY=cifradoCesarAlfabetoInglesMAYMINDESP(claroCESARMAY,4)
print(cifradoCESARMAY)

#def cifradoCesarAlfabetoInglesMAY(cadena,desp):
#ord de caract da numasci
#chr de num me da caract
def descifradoCesarAlfabetoInglesMAYMINDESP(cadena,desp):
				"""Devuelve	un	cifrado	Cesar	tradicional	(+3)"""
				#	Definir	la	nueva	cadena	resultado
				resultado	=	''
				#	Realizar	el	"cifrado",	sabiendo	que	A	=	65,	Z	=	90,	a	=	97,	z	=	122
				i	=	0
				while i	<	len(cadena):
								#	Recoge	el	caracter	a	cifrar
								ordenClaro	=	ord(cadena[i])
								ordenCifrado	=	0
								#	Cambia	el	caracter	a	cifrar
								
									
								if ((ordenClaro	>=	65 and ordenClaro	<=	90 )):
												ordenCifrado	=	(((ordenClaro	- 65)	-	desp)	%	26)	+	65
								elif ((ordenClaro	>=	97 and ordenClaro	<=	122 )):
												ordenCifrado	=	(((ordenClaro	- 97)	-	desp)	%	26)	+	97
								#	Añade	el	caracter	cifrado	al	resultado
								if (ordenClaro==0):
									resultado	=	resultado	+	' '
								else:
									resultado	=	resultado	+	chr(ordenCifrado)
								i	=	i	+	1
				#	devuelve	el	resultado
				return resultado



descifradoCESARMAY=descifradoCesarAlfabetoInglesMAYMINDESP(cifradoCESARMAY,4)
print(descifradoCESARMAY)
