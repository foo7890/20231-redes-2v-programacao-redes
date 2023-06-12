import socket
import math

def handle_request(request):
    tokens = request.split()
    if tokens[0] == 'soma':
        if len(tokens) != 3:
            return "Mensagem inválida."
        try:
            num1 = float(tokens[1])
            num2 = float(tokens[2])
            return str(num1+num2)
        except:
            return "Mensagem inválida"
    elif tokens[0] == 'raiz':
        if len(tokens != 2):
            return "Mensagem inválida"
        try:
            num = float(tokens[1])
            return str(math.sqrt(num))
        except ValueError:
            return "Mensagem inválida"
    else:
        return "Mensagem inválida"

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Servidor inicializado. Aguardando conexões...")
    while True:
        client_socket, client_adress = server_socket.accept()
        print("Conexão com o IP cliente: ", client_adress)
        while True:
            request = client_socket.recv(1024).decode().strip()
            if not request:
                break
        response = handle_request(request)
        client_socket.send((response + '\n').encode())
        client_socket.close()
        print("conexão encerrada com: ", client_adress)

if __name__=='__main__':
    host = 'localhost'
    port = 2000
    start_server(host, port)
    
