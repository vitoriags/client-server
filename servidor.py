# servidor
from socket import *

host = ''
port = 55555
conexaoS = socket(AF_INET, SOCK_STREAM)  # servidor TCP-IP

# qual o host e qual a porta que vou usar
conexaoS.bind((host, port))

# quantidade de conexões
conexaoS.listen(5)

# enquanto houver conexão:
while True:
    conexao, endereco = conexaoS.accept()
    print(f'Conexão com o Cliente Feita')

    while True:
        entrada = conexao.recv(1024).decode()
        entrada = entrada.split(" ")
        entrada = list(map(int, entrada))

        if entrada[0] == 1:
            result = entrada[1] + entrada[2]
            result = str(result)
            conexao.send(result.encode())

        elif entrada[0] == 2:
            result = entrada[1] - entrada[2]
            result = str(result)
            conexao.send(result.encode())

        elif entrada[0] == 3:
            result = entrada[1] * entrada[2]
            result = str(result)
            conexao.send(result.encode())

        elif entrada[0] == 4:
            result = entrada[1] / entrada[2]
            result = str(result)
            conexao.send(result.encode())

        else:
            conexao.send("\nEntrada Inválida\n".encode())

    conexao.close()