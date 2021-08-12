# servidor
from socket import *

host = ''
port = 55555
conexaoS = socket(AF_INET, SOCK_STREAM)  # servidor TCP-IP

# qual o host e qual a porta que vou usar
conexaoS.bind((host, port))

# quantidade de conexões
conexaoS.listen()

# enquanto houver conexão:
while True:
    ListaCadastros = []
    menu = []
    conexao, endereco = conexaoS.accept()

    print("\n\nConexão com o Cliente Feita")

    while True:
        menu = conexao.recv(1024).decode()
        menu = list(menu.split(","))
        print(f'menu: {menu}')

        if menu[0] == "1":
            # cadastro
            if menu[1] not in ListaCadastros:
                ListaCadastros = ListaCadastros + menu
                print(f'Lista Inicio: {ListaCadastros}')
                envio = "\n\nCadastrado(a) com sucesso!"
                conexao.send(envio.encode())
            else:
                envio = "\n\nVocê já está cadastrado(a)!"
                conexao.send(envio.encode())

        elif menu[0] == "2":
            # consultar cadastro
            if menu[1] in ListaCadastros:
                #envio = "\n\nVocê está cadastrado(a)!"
                if menu[1] in ListaCadastros:
                    for i in range(len(ListaCadastros)):
                        if ListaCadastros[i] == menu[1]:
                            envio = "\nVocê está cadastrado(a)! \n\n" + "Nome: " + ListaCadastros[i] + "\n" + "CPF: " + ListaCadastros[i + 1] + "\n" + "Endereço: " + ListaCadastros[i + 2]

                conexao.send(envio.encode())
            else:
                envio = "\n\nVocê não está cadastrado(a)!"
                conexao.send(envio.encode())

        elif menu[0] == "3":
            # remover cadastro
            if menu[1] in ListaCadastros:
                for i in range(len(ListaCadastros)):
                    if ListaCadastros[i] == menu[1]:
                        del(ListaCadastros[i - 1: i + 3])
                        envio = "\n\nRemoção feita com sucesso!"
                        conexao.send(envio.encode())
                        break
            else:
                envio = "\n\nVocê não está cadastrado(a), por isso não haverá remoção!"
                conexao.send(envio.encode())

        print(f'Lista Final: {ListaCadastros}')
