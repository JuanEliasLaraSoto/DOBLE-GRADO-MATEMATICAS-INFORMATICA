from Crypto.Hash import SHA256, HMAC
import base64
import json
import sys
from socket_class import SOCKET_SIMPLE_TCP
import funciones_aes

# Paso 0: Crea las claves que T comparte con B y A
##################################################

# Crear Clave KAT, guardar a fichero
KAT = funciones_aes.crear_AESKey()
FAT = open("KAT.bin", "wb")
FAT.write(KAT)
FAT.close()

# Crear Clave KBT, guardar a fichero
KBT = funciones_aes.crear_AESKey()
FBT = open("KBT.bin", "wb")
FBT.write(KBT)
FBT.close()

# Paso 1) B->T: KBT(Bob, Nb) en AES-GCM
#######################################

# Crear el socket de escucha de Bob (5551)
print("Esperando a Bob...")
socket_Bob = SOCKET_SIMPLE_TCP('127.0.0.1', 5551)
socket_Bob.escuchar()

# Crea la respuesta para B y A: K1 y K2
K1 = funciones_aes.crear_AESKey()
K2 = funciones_aes.crear_AESKey()

# Recibe el mensaje
cifrado = socket_Bob.recibir()
cifrado_mac = socket_Bob.recibir()
cifrado_nonce = socket_Bob.recibir()

# Descifro los datos con AES GCM
datos_descifrado_ET = funciones_aes.descifrarAES_GCM(KBT, cifrado_nonce, cifrado, cifrado_mac)

# Decodifica el contenido: Bob, Nb
json_ET = datos_descifrado_ET.decode("utf-8" ,"ignore")
print("B->T (descifrado): " + json_ET)
msg_ET = json.loads(json_ET)

# Extraigo el contenido
t_bob, t_nb = msg_ET
t_nb = bytearray.fromhex(t_nb)#cd meto en json algo q no es un string, necesito hacerle un .hex

# Paso 2) T->B: KBT(K1, K2, Nb) en AES-GCM
##########################################
mensaje_B1 = [K1.hex(), K2.hex(), t_nb.hex()]
json_EB = json.dumps(mensaje_B1)

print(" T -> B (descifrado): " + json_EB)

motorB_AES = funciones_aes.iniciarAES_GCM(KBT)
cifrado_B1_T, mac_B1_T, nonce_B1_T = funciones_aes.cifrarAES_GCM(motorB_AES, json_EB.encode("utf-8"))

socket_Bob.enviar(cifrado_B1_T)
socket_Bob.enviar(mac_B1_T)
socket_Bob.enviar(nonce_B1_T)
# (A realizar por el alumno/a...)

# Cerramos el socket entre B y T, no lo utilizaremos mas
socket_Bob.cerrar() 

# Paso 3) A->T: KAT(Alice, Na) en AES-GCM
#########################################
print("Esperando a ALICE...")
socket_Alice = SOCKET_SIMPLE_TCP('127.0.0.1', 5551)
socket_Alice.escuchar()



# Recibe el mensaje
cifrado = socket_Alice.recibir()
cifrado_mac = socket_Alice.recibir()
cifrado_nonce = socket_Alice.recibir()

# Descifro los datos con AES GCM
datos_descifrado_ET = funciones_aes.descifrarAES_GCM(KAT, cifrado_nonce, cifrado, cifrado_mac)

# Decodifica el contenido: Bob, Nb
json_ET = datos_descifrado_ET.decode("utf-8" ,"ignore")
print("A->T (descifrado): " + json_ET)
msg_ET = json.loads(json_ET)

# Extraigo el contenido
t_A, t_na = msg_ET
t_na = bytearray.fromhex(t_na)#cd meto en json algo q no es un string, necesito hacerle un .hex

# (A realizar por el alumno/a...)

# Paso 4) T->A: KAT(K1, K2, Na) en AES-GCM
##########################################
mensaje_B1 = [K1.hex(), K2.hex(), t_na.hex()]
json_EB = json.dumps(mensaje_B1)

print(" T -> B (descifrado): " + json_EB)

motorB_AES = funciones_aes.iniciarAES_GCM(KBT)
cifrado_B1_T, mac_B1_T, nonce_B1_T = funciones_aes.cifrarAES_GCM(motorB_AES, json_EB.encode("utf-8"))

socket_Alice.enviar(cifrado_B1_T)
socket_Alice.enviar(mac_B1_T)
socket_Alice.enviar(nonce_B1_T)
# (A realizar por el alumno/a...)

# Cerramos el socket entre B y T, no lo utilizaremos mas
socket_Alice.cerrar() 
# (A realizar por el alumno/a...)
