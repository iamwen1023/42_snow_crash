import socket
import sys

HOST = sys.argv[1] if len(sys.argv) > 1 else exit("Usage: python server.py <HOST>")
PORT = 6969

# Création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Serveur en écoute sur {HOST}:{PORT}...")

try:
    while True:
        client_socket, client_address = server_socket.accept()

        while True:
            data = client_socket.recv(1024)
            if not data:
                break  # Déconnexion du client

            message = data.decode("utf-8")
            print(f"Message received: {message}")

        client_socket.close()

except KeyboardInterrupt:
    print("\nStopping server.")
    server_socket.close()
