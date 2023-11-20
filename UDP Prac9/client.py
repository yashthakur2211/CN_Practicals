import socket
import os

def start_client():
    # Define the server address (host, port)
    server_address = ('localhost', 12345)

    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send the script file
    send_file(client_socket, 'script.py', server_address)

    # Send the text file
    send_file(client_socket, 'text.txt', server_address)

    # Send the audio file
    send_file(client_socket, 'audio.wav', server_address)

    # Send the video file
    send_file(client_socket, 'video.mp4', server_address)

    # Close the socket
    client_socket.close()

def send_file(socket, file_name, server_address):
    # Send the file size
    file_size = os.path.getsize(file_name)
    socket.sendto(str(file_size).encode(), server_address)

    # Send the file content
    with open(file_name, 'rb') as file:
        file_data = file.read(1024)
        while file_data:
            socket.sendto(file_data, server_address)
            file_data = file.read(1024)

    print(f"File '{file_name}' sent successfully!")

if __name__ == "__main__":
    start_client()
