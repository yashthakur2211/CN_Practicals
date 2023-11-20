import socket

def start_udp_server():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    print("UDP Server is waiting for messages...")

    while True:
        # Receive data from the client
        data, client_address = server_socket.recvfrom(1024)
        print(f"Received data from {client_address}: {data.decode()}")

        # Send a response back to the client
        response = "Hello from the server!"
        server_socket.sendto(response.encode(), client_address)

if __name__ == "__main__":
    start_udp_server()
