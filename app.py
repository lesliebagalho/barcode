import os
import barcode
from barcode.writer import ImageWriter
from IPython.display import Image, display

# Obtém a classe de código de barras EAN-13
barcode_format = barcode.get_barcode_class('ean13')

# Número do código de barras (12 dígitos)
# print("Digite ou colete os dígitos para gerar o código de barras...")
print("\nAtenção!!! Deve ter 12 dígitos para gerar o código de barras...")
barcode_number = input("\nDigite o seu número de código de barras: ")

# Cria a imagem do código de barras
barcode_image = barcode_format(barcode_number, writer=ImageWriter())

# Obter o diretório atual (onde o script está sendo executado)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Nome do arquivo e caminho completo
print("\nInsira o nome para o arquivo a ser gerado")
barcode_name = input("Nome: ")
barcode_filename = os.path.join(current_directory, f'barcode_{barcode_name}')

# Salvar o código de barras na mesma pasta do arquivo
barcode_image.save(barcode_filename)

# Exibe a imagem
display(Image(filename=f'{barcode_filename}.png'))