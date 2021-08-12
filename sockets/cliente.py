# cliente
from socket import *

host = 'localhost'
port = 55555
conexaoC = socket(AF_INET, SOCK_STREAM)

# conexão do cliente com o servidor
conexaoC.connect((host, port))

while True:
    print(
        "_______________________________\n\nSeja bem-vindo(a)!\nO que deseja fazer?\n(1) Cadastro\n(2) Consultar Cadastro\n(3) Remover Cadastro\n(Qualquer Tecla) Sair")
    numero = input()

    if numero == "1":
        nome = input("_______________________________\n\nCADASTRO\n\nNome: ").lower().replace(" ", "")
        CPF = input("CPF: ")
        endereco = input("Endereço: ").lower().replace(" ", "")
        lista = numero + "," + nome + "," + CPF + "," + endereco
        conexaoC.send(lista.encode())
        print(conexaoC.recv(1024).decode())

    elif numero == "2":
        nome = input("_______________________________\n\nCONSULTAR CADASTRO\n\nDigite seu nome: ").lower().replace(" ",
                                                                                                                   "")
        lista = numero + "," + nome
        conexaoC.send(lista.encode())
        print(conexaoC.recv(1024).decode())

    elif numero == "3":
        nome = input("_______________________________\n\nREMOÇÃO DE CADASTRO\n\nDigite seu nome: ").lower().replace(" ",
                                                                                                                    "")
        lista = numero + "," + nome
        conexaoC.send(lista.encode())
        print(conexaoC.recv(1024).decode())

    else:
        exit()
