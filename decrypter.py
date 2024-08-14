import os
import pyaes

print("iniciando descriptografia")

## abrir o arquivo criptografado
file_name = "teste.txt.troll"
file = open(file_name, "rb")
file_data = file.read()
file.closed()

## chave para descriptografia
key = b"UjcoBvygEEdD4fsV2t3jug"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

##remove o arquivo
os.remove(file_name)

## cria o arquivo criptografado
new_file = "teste.txt"
new_file = open(f"{new_file}", "wb")
new_file.write(decrypt_data)
new_file.close()

print("fim da descriptografia")

