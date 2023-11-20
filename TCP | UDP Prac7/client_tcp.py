import socket

def start_tcp_client():
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    # Send data to the server
    message = "Hello from the client!"
    client_socket.send(message.encode())

    # Receive the server's response
    response = client_socket.recv(1024)
    print(f"Server says: {response.decode()}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_tcp_client()
