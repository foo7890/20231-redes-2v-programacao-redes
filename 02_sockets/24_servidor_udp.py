import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 8002)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(server_address)
    print(f"Servidor UDP iniciado em {server_address[0]}:{server_address[1]}")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode('utf-8')

        print(f"Mensagem recebida do cliente {client_address}:{message}")

        if message == "quit":
            break
    
if __name__ == '__main__':
    main()
