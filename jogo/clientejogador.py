import socket
import json

# Configurações do cliente
HOST = 'localhost'  # Pode ser o IP do seu servidor
PORT = 12345  # Porta do servidor

# Cria um socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
client_socket.connect((HOST, PORT))

flag = client_socket.recv(1024)
flag = flag.decode('utf-8')
#print(flag)
if flag == '1'or 1:
    sua_vez = True
else:
    sua_vez = False    
while True:    

    if sua_vez == True:
        req = client_socket.recv(1024)

        if not req:
            # O servidor desconectou
            print('Servidor desconectado.')
            break

        sua_vez = False
        # Decodifica a mensagem recebida
        mensagem = req.decode('utf-8')

        # Exibe a mensagem de solicitação do servidor
        print(mensagem)
        # Prepara os dados da jogada
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))
        jogada = {'linha': linha, 'coluna': coluna}


        # Converte a jogada em JSON
        message = json.dumps(jogada)
        

        # Envia a mensagem para o servidor
        client_socket.sendall(message.encode('utf-8'))
    else:
        sua_vez = True

    data = client_socket.recv(1024)
    #Decodifica mensagem recebida matriz
    matrix = data.decode('utf-8')
    print(matrix)

# Fecha o socket do cliente
client_socket.close()
