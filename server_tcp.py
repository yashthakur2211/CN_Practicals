import socket

def start_tcp_server():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Listen for incoming connections (maximum 1 connection in the queue)
    server_socket.listen(1)

    print("TCP Server is waiting for a connection...")

    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    # Receive data from the client
    data = client_socket.recv(1024)
    print(f"Received data from client: {data.decode()}")

    # Send a response back to the client
    response = "Hello from the server!"
    client_socket.send(response.encode())

    # Close the connection
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_tcp_server()
