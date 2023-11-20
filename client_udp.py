import socket

def start_udp_client():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Server address
    server_address = ('localhost', 12345)

    # Send data to the server
    message = "Hello from the client!"
    client_socket.sendto(message.encode(), server_address)

    # Receive the server's response
    response, _ = client_socket.recvfrom(1024)
    print(f"Server says: {response.decode()}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_udp_client()
