
from Crypto.Hash import SHA256, HMAC
import base64
import json
import sys
from socket_class import SOCKET_SIMPLE_TCP
import funciones_aes
from Crypto.Random import get_random_bytes

# Paso 0: Inicializacion
########################
KAT = open("KAT.bin", "rb").read()
# (A realizar por el alumno/a...)
socket_T = SOCKET_SIMPLE_TCP('127.0.0.1', 5551)
socket_T.conectar()

# Crea los campos del mensaje
t_n_origen = get_random_bytes(16)
# Paso 3) A->T: KAT(Alice, Na) en AES-GCM
#########################################
msg_TE = []
msg_TE.append("ALICE")
msg_TE.append(t_n_origen)
json_ET = json.dumps(msg_TE)

# Cifra los datos con AES GCM
aes_engine = funciones_aes.iniciarAES_GCM(KAT)
cifrado, cifrado_mac, cifrado_nonce = funciones_aes.cifrarAES_GCM(aes_engine,json_ET.encode("utf-8"))
# Envia los datos
socket_T.enviar(cifrado)
socket_T.enviar(cifrado_mac)#MAC POR LA CARA(eSTOY USANDO GCM)
socket_T.enviar(cifrado_nonce)#NONCE POR LA CARA

# (A realizar por el alumno/a...)

# Paso 4) T->A: KAT(K1, K2, Na) en AES-GCM
##########################################
cif=socket_T.recibir()
nonce=socket_T.recibir()
mac=socket_T.recibir()
# Descifro los datos con AES GCM
datos_descifrado_ET = funciones_aes.descifrarAES_GCM(KAT, cifrado_nonce, cifrado, cifrado_mac)
# Decodifica el contenido: Bob, Nb
json_ET = datos_descifrado_ET.decode("utf-8" ,"ignore")
print("B->T (descifrado): " + json_ET)
msg_ET = json.loads(json_ET)
# Extraigo el contenido
K1,K2, t_nb = msg_ET
t_nb = bytearray.fromhex(t_nb)
K1 = bytearray.fromhex(K1)
K2 = bytearray.fromhex(K2)
if(t_nb == t_n_origen):
    print("El nonce es el mismo")
else:
    print("El nonce no es el mismo")
    exit
# (A realizar por el alumno/a...)
socket_T.cerrar()
# Paso 5) A->B: KAB(Nombre) en AES-CTR con HMAC
###############################################
socket_B = SOCKET_SIMPLE_TCP('127.0.0.1', 5551)
socket_B.conectar()
apellido = "JUANA"
aes_cifrado, nonce_16_ini = funciones_aes.iniciarAES_CTR_cifrado(K1)
datos_cifrado = funciones_aes.cifrarAES_CTR(aes_cifrado,
apellido.encode("utf-8"))
# Crear el hmac
hsend = HMAC.new(K2, msg=apellido.encode("utf-8"), digestmod=SHA256)
mac = hsend.digest()
mensaje = []
mensaje.append(datos_cifrado.hex())
mensaje.append(nonce_16_ini.hex())
mensaje.append(mac.hex())

# Envia los datos
mensaje_json=json.dumps(mensaje)
socket_B.enviar(mensaje_json.encode("utf-8"))


# (A realizar por el alumno/a...)

# Paso 6) B->A: KAB(Apellido) en AES-CTR con HMAC
#################################################
paquete=socket_B.recibir()##solo espero un paquete pq hay hmac y todo viene en el mismo paq

# Descifro los datos con AES CTR
# Decodifica el contenido: Bob, Nb
json_ET = paquete.decode("utf-8" ,"ignore")
print("T->B (descifrado): " + json_ET)
msg_ET = json.loads(json_ET)
# Extraigo el contenido
datos_cifrado,nonce,mac = msg_ET##ES EL MAC VERDADERO EH, AQUI NO ENVIO MAC PORLACAA PQ ES CTR Q NO LLEVA MAC
datos_cifrado=bytearray.fromhex(datos_cifrado)
nonce=bytearray.fromhex(nonce)
#####EL MAC NO LO PASO A HEXARRAY PQ LUEGO LE APLICO LA FUNC HEXVEIFY, SI LO PASO A HEXARRAY, ENTONCES TENDRIA Q USAR LUEGO LA FUNCION VERIFY Y NO LA HEXVERIFY
aes_descifrado = funciones_aes.iniciarAES_CTR_descifrado(K1, nonce)
datos_claro = funciones_aes.descifrarAES_CTR(aes_descifrado,
datos_cifrado)
mensaje_claro_json = datos_claro.decode("utf-8")
print("A -> B (descifrado): " + mensaje_claro_json)
hmacB = HMAC.new(K2, digestmod=SHA256)
hmacB.update(mensaje_claro_json.encode("utf-8"))
try:
    hmacB.hexverify(mac)
    print("Mensaje correcto")
except ValueError:
    print("Mensaje manipulado")
    socket_B.cerrar()
    exit()
# (A realizar por el alumno/a...)

# Paso 7) A->B: KAB(END) en AES-CTR con HMAC
############################################
apellido = "END"
aes_cifrado, nonce_16_ini = funciones_aes.iniciarAES_CTR_cifrado(K1)
datos_cifrado = funciones_aes.cifrarAES_CTR(aes_cifrado,
apellido.encode("utf-8"))
# Crear el hmac
hsend = HMAC.new(K2, msg=apellido.encode("utf-8"), digestmod=SHA256)
mac = hsend.digest()
mensaje = []
mensaje.append(datos_cifrado.hex())
mensaje.append(nonce_16_ini.hex())
mensaje.append(mac.hex())

# Envia los datos
mensaje_json=json.dumps(mensaje)
socket_B.enviar(mensaje_json)

socket_T.cerrar()
# (A realizar por el alumno/a...)
