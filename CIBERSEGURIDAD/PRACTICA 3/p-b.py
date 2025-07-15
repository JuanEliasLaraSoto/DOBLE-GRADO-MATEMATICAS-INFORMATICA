

from Crypto.Hash import SHA256, HMAC
import base64
import json
import sys
from socket_class import SOCKET_SIMPLE_TCP
import funciones_aes
from Crypto.Random import get_random_bytes

# Paso 0: Inicializacion
########################

# Lee clave KBT
KBT = open("KBT.bin", "rb").read()

# Paso 1) B->T: KBT(Bob, Nb) en AES-GCM
#######################################

# Crear el socket de conexion con T (5551)
print("Creando conexion con T...")
socket = SOCKET_SIMPLE_TCP('127.0.0.1', 5551)
socket.conectar()

# Crea los campos del mensaje
t_n_origen = get_random_bytes(16)

# Codifica el contenido (los campos binarios en una cadena) y contruyo el mensaje JSON
msg_TE = []
msg_TE.append("Bob")
msg_TE.append(t_n_origen.hex())##33333333# Conversion de Bytes a Hexadecimal
json_ET = json.dumps(msg_TE)##3333333333333## Convertimos un Array Python a string
print("B -> T (descifrado): " + json_ET)

# Cifra los datos con AES GCM
aes_engine = funciones_aes.iniciarAES_GCM(KBT)
cifrado, cifrado_mac, cifrado_nonce = funciones_aes.cifrarAES_GCM(aes_engine,json_ET.encode("utf-8"))

# Envia los datos
socket.enviar(cifrado)
socket.enviar(cifrado_mac)
socket.enviar(cifrado_nonce)

# Paso 2) T->B: KBT(K1, K2, Nb) en AES-GCM
##########################################
cifrado=socket.recibir()
cifrado_nonce=socket.recibir()
cifrado_mac=socket.recibir()

# Descifro los datos con AES GCM
datos_descifrado_ET = funciones_aes.descifrarAES_GCM(KBT, cifrado_nonce, cifrado, cifrado_mac)

# Decodifica el contenido: Bob, Nb
json_ET = datos_descifrado_ET.decode("utf-8" ,"ignore")
print("T->B (descifrado): " + json_ET)
msg_ET = json.loads(json_ET)###333333#### Recuperamos un string a Array Python

# Extraigo el contenido
t_k1,t_k2, t_nb = msg_ET
k1 = bytearray.fromhex(t_k1)###3333333#### De Hexadecimal a Bytes
k2 = bytearray.fromhex(t_k2)
t_nb = bytearray.fromhex(t_nb)

if(t_nb == t_n_origen):
    print("El nonce es el mismo")
else:
    print("El nonce no es el mismo")
    exit
# (A realizar por el alumno/a...)

# Cerramos el socket entre B y T, no lo utilizaremos mas
socket.cerrar() 

# Paso 5) A->B: KAB(Nombre) en AES-CTR con HMAC
###############################################

##CREAMOS NUEVO SOCKET PQ YA NO ES LA COMUNICACION B->T SINO Q ES A->B
#RECUERDA SIEMPRE CERRAR EL DE ANTES

socket = SOCKET_SIMPLE_TCP('127.0.0.1', 5551)
socket.conectar()

paquete=socket.recibir()##solo espero un paquete pq hay hmac y todo viene en el mismo paq


# Descifro los datos con AES CTR

# Decodifica el contenido: Bob, Nb
json_ET = paquete.decode("utf-8" ,"ignore")
print("T->B (descifrado): " + json_ET)
msg_ET = json.loads(json_ET)

# Extraigo el contenido
datos_cifrado,nonce,mac_OFICIAL_EL_DE_HMAC_ = msg_ET##ES EL MAC VERDADERO EH, AQUI NO ENVIO MAC PORLACAA PQ ES CTR Q NO LLEVA MAC
datos_cifrado=bytearray.fromhex(datos_cifrado)
nonce=bytearray.fromhex(nonce)
#####EL MAC NO LO PASO A HEXARRAY PQ LUEGO LE APLICO LA FUNC HEXVEIFY, SI LO PASO A HEXARRAY, ENTONCES TENDRIA Q USAR LUEGO LA FUNCION VERIFY Y NO LA HEXVERIFY

aes_descifrado = funciones_aes.iniciarAES_CTR_descifrado(k1, nonce)
datos_claro = funciones_aes.descifrarAES_CTR(aes_descifrado,
datos_cifrado)
mensaje_claro_json = datos_claro.decode("utf-8")
print("A -> B (descifrado): " + mensaje_claro_json)
hmacB = HMAC.new(k2, digestmod=SHA256)
hmacB.update(mensaje_claro_json.encode("utf-8"))
try:
    hmacB.hexverify(mac_OFICIAL_EL_DE_HMAC_)
    print("Mensaje correcto")
except ValueError:
    print("Mensaje manipulado")
    socket.cerrar()
    exit()
# (A realizar por el alumno/a...)

# Cerramos el socket entre B y T, no lo utilizaremos mas

# (A realizar por el alumno/a...)

# Paso 6) B->A: KAB(Apellido) en AES-CTR con HMAC
#################################################
apellido = "LARA SOTO"
aes_cifrado, nonce_16_ini = funciones_aes.iniciarAES_CTR_cifrado(k1)
datos_cifrado = funciones_aes.cifrarAES_CTR(aes_cifrado,
apellido.encode("utf-8"))
# Crear el hmac
hsend = HMAC.new(k2, msg=apellido.encode("utf-8"), digestmod=SHA256)
mac_OFICIAL_EL_DE_HMAC_ = hsend.digest()###3333####HMAC como array de bytes
mensaje = []
mensaje.append(datos_cifrado.hex())
mensaje.append(nonce_16_ini.hex())
mensaje.append(mac_OFICIAL_EL_DE_HMAC_.hex())




# Envia los datos
mensaje_json=json.dumps(mensaje)
socket.enviar(mensaje_json.encode("utf-8"))

# (A realizar por el alumno/a...)

# (A realizar por el alumno/a...)

# Paso 7) A->B: KAB(END) en AES-CTR con HMAC
############################################
paquete=socket.recibir()##solo espero un paquete pq hay hmac y todo viene en el mismo paq

# Decodifica el contenido: Bob, Nb
json_ET = paquete.decode("utf-8" ,"ignore")
print("T->B (descifrado): " + json_ET)
msg_ET = json.loads(json_ET)

# Extraigo el contenido
datos_cifrado,nonce,mac_OFICIAL_EL_DE_HMAC_ = msg_ET##ES EL MAC VERDADERO EH, AQUI NO ENVIO MAC PORLACAA PQ ES CTR Q NO LLEVA MAC
datos_cifrado=bytearray.fromhex(datos_cifrado)
nonce=bytearray.fromhex(nonce)
#####EL MAC NO LO PASO A HEXARRAY PQ LUEGO LE APLICO LA FUNC HEXVEIFY, SI LO PASO A HEXARRAY, ENTONCES TENDRIA Q USAR LUEGO LA FUNCION VERIFY Y NO LA HEXVERIFY

aes_descifrado = funciones_aes.iniciarAES_CTR_descifrado(k1, nonce)
datos_claro = funciones_aes.descifrarAES_CTR(aes_descifrado,
datos_cifrado)
mensaje_claro_json = datos_claro.decode("utf-8")
print("A -> B (descifrado): " + mensaje_claro_json)
hmacB = HMAC.new(k2, digestmod=SHA256)
hmacB.update(mensaje_claro_json.encode("utf-8"))
try:
    hmacB.hexverify(mac_OFICIAL_EL_DE_HMAC_)
    print("Mensaje correcto")
except ValueError:
    print("Mensaje manipulado")
    socket.cerrar()
    exit()
# (A realizar por el alumno/a...)

socket.cerrar() 
#33333333333333##– .hexdigest() => HMAC como cadena de caracteres hexadecimales
