import funciones_rsa as r
import funciones_aes as a
import socket_class as socket

"""Cargar la clave privada de Alice y la clave pública de Bob. """
kprivA=r.cargar_RSAKey_Privada("privAli.txt","betis")
kpubB=r.cargar_RSAKey_Publica("pubBobi.txt")
"""Cifrar un array de 16 bytes (K1) utilizando la clave de Bob."""
k1=a.crear_AESKey()
cifrado=r.cifrarRSA_OAEP(k1,kpubB)
"""e. Firmar dicho array de 16 bytes (K1) utilizando la clave de Alice."""
firma=r.firmarRSA_PSS(k1,kprivA)

"""Enviar el cifrado y la firma usando un socket cliente de la clase
SOCKET_SIMPLE_TCP(), descrita en los apéndices."""
socket=socket.SOCKET_SIMPLE_TCP('127.0.0.1',5551)
socket.conectar()
socket.enviar(cifrado)
socket.enviar(firma)


"""Alice recibirá el texto cifrado con la clave simétrica y la firma digital
a través del socket ya abierto en el apartado 1. Después, descifrará la 
cadena de caracteres y la mostrará por pantalla tras comprobar la validez
de la firma digital."""
nonceBob = socket.recibir()
cadenaCifrada = socket.recibir()
cadenaFirmaBob = socket.recibir()

aes_descif = a.iniciarAES_CTR_descifrado(k1, nonceBob)
datosEnClaroBob = a.descifrarAES_CTR(aes_descif, cadenaCifrada)
validedFirmaBob = r.comprobarRSA_PSS(datosEnClaroBob, cadenaFirmaBob, kpubB)
print(f"Cadena de caracteres recibida: {datosEnClaroBob}. Validez: {validedFirmaBob}")



"""Finalmente, Alice repetirá los pasos a) y b) en reverso: enviando a Bob
la cadena cifrada “Hola Bob” con K1 en AES-CTR-128, junto con la firma 
digital de dicha cadena, y Bob se encargará de descifrar y comprobar la 
firma digital."""

(cifrado,nonce)=a.iniciarAES_CTR_cifrado(cifrado)
cifrado=a.cifrarAES_CTR(cifrado,"hola bob".encode("utf-8"))
firma=r.firmarRSA_PSS("hola bob".encode("utf-8"))
socket.enviar(nonce)
socket.enviar(cifrado)
socket.enviar(firma)
socket.cerrar()