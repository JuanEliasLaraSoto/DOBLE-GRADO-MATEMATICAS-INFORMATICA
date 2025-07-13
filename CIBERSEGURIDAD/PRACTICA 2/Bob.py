import funciones_rsa as r
import funciones_aes as a
import socket_class as socket

"""Cargar la clave privada de Bob y la clave pública de Alice."""
kprivB=r.cargar_RSAKey_Privada("privBobi.txt","batisole")
kpubA=r.cargar_RSAKey_Publica("pubAli.txt")
"""Recibir el texto cifrado y la firma digital a través del socket servidor de la clase
SOCKET_SIMPLE_TCP(), descrita en los apéndices"""

socketServidor = socket.SOCKET_SIMPLE_TCP('127.0.0.1', 5551)
socketServidor.escuchar()
cifrado=socketServidor.recibir()
firma=socketServidor.recibir()


"""Descifrar el array de 16 bytes (K1) y mostrarlo por pantalla."""
descifrado=r.descifrarRSA_OAEP(cifrado,kprivB)
print(descifrado)

"""Comprobar la validez de la firma digital"""
r.comprobarRSA_PSS(descifrado,firma,kpubA)

"""Tras el último paso del apartado 1, Bob cifrará la cadena “Hola Alice” utilizando AESCTR-128 con la clave K1, y firmará esa cadena con su clave privada. A continuación,
enviará dicho cifrado y la firma a través del socket ya abierto en el apartado 1."""
(cifrado,nonce)=a.iniciarAES_CTR_cifrado(descifrado)#le paso la klave de sesion
cifrado=a.cifrarAES_CTR(cifrado,"HOLA ALICE".encode("utf-8"))#cifro con clave seion cifrada
firma=r.firmarRSA_PSS("HOLA ALICE".encode("utf-8"),kprivB)
socketServidor.enviar(nonce)#envio nonce
socketServidor.enviar(cifrado)
socketServidor.enviar(firma)

"""Finalmente, Alice repetirá los pasos a) y b) en reverso: enviando a Bob la cadena
cifrada “Hola Bob” con K1 en AES-CTR-128, junto con la firma digital de dicha
cadena, y Bob se encargará de descifrar y comprobar la firma digital."""

nonce=socketServidor.recibir()
cifrado=socketServidor.recibir()
firma=socketServidor.recibir()
descifrado=a.iniciarAES_CTR_descifrado(cifrado,nonce)
descifrado=a.descifrarAES_CTR(descifrado,cifrado)
firma=r.comprobarRSA_PSS(descifrado,firma,kpubA)
socketServidor.cerrar()