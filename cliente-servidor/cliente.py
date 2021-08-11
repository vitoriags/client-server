# cliente
from socket import *

host = 'localhost'
port = 55555
conexaoC = socket(AF_INET, SOCK_STREAM)

# conexão do cliente com o servidor
conexaoC.connect((host, port))

while True:
    print(
        "\nEscolha uma operação entre:\n[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Divisão.\nEm seguida, os dois numeros escolhidos para a operação. Ex: 1 3 5")
    numeros = input()
    aux = list(numeros.split(" "))
    conexaoC.send(numeros.encode())
    result = conexaoC.recv(1024).decode()

    if aux[0] == "1":
        print(f'\nSOMA: {aux[1]} + {aux[2]} = {result}')

    elif aux[0] == "2":
        print(f'\nSUBTRAÇÃO: {aux[1]} - {aux[2]} = {result}')

    elif aux[0] == "3":
        print(f'\nMULTIPLICAÇÃO: {aux[1]} * {aux[2]} = {result}')

    elif aux[0] == "4":
        print(f'\nDIVISÃO: {aux[1]} / {aux[2]} = {result}')
    else:
        print(result)
