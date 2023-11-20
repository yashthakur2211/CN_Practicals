import socket
import os

def start_server():
    # Define the server address (host, port)
    server_address = ('localhost', 12345)

    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    server_socket.bind(server_address)

    print("Server is waiting for a connection...")

    # Receive the script file
    receive_file(server_socket, 'received_script.py')

    # Receive the text file
    receive_file(server_socket, 'received_text.txt')

    # Receive the audio file
    receive_file(server_socket, 'received_audio.wav')

    # Receive the video file
    receive_file(server_socket, 'received_video.mp4')

    # Close the socket
    server_socket.close()

def receive_file(socket, file_name):
    # Receive the file size
    file_size, client_address = socket.recvfrom(1024)
    file_size = int(file_size.decode())

    print(f"Receiving file '{file_name}' from {client_address}...")

    # Receive the file content
    received_data = b""
    while len(received_data) < file_size:
        chunk, _ = socket.recvfrom(1024)
        received_data += chunk

    # Save the received file
    with open(file_name, 'wb') as file:
        file.write(received_data)

    print(f"File '{file_name}' received successfully!")

if __name__ == "__main__":
    start_server()
