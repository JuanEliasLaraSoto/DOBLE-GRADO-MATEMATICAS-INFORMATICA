from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter

key = get_random_bytes(16) # Clave aleatoria de 128 bits
IV = get_random_bytes(16//2) # Nonce aleatorio de 64 bits para GCM
BLOCK_SIZE_AES = 16 # Bloque de 128 bits
data = "Hola amigos de la seguridad".encode("utf-8") # Datos a cifrar
print(data)
mac_size=16
aes_cipher = AES.new(key, AES.MODE_GCM, nonce=IV, mac_len=mac_size)
ciphertext, mac_cifrado = aes_cipher.encrypt_and_digest(pad(data,BLOCK_SIZE_AES))
print(ciphertext)
try:
  aes_decipher = AES.new(key, AES.MODE_GCM, nonce=IV)
  text=unpad(aes_decipher.decrypt_and_verify(ciphertext, mac_cifrado),  BLOCK_SIZE_AES).decode("utf-8", "ignore")
  print(text)
except (ValueError,KeyError) as e:
  print("ERROR")