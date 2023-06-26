import socket

HOST = 'localhost'
PORT = 2000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

try:
    nome_arquivo = input("Digite o nome do arquivo: ")
    with open(nome_arquivo, "rb") as arquivo:
        tamanho = len(arquivo.read())
        arquivo.seek(0) #volta para o início do arquivo
        bytes_arquivo = arquivo.read()

    sock.send(nome_arquivo.encode())
    sock.send(str(tamanho).encode())
    sock.sendall(bytes_arquivo)
finally:
    sock.close()
