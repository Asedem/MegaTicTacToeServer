import socket
from _thread import start_new_thread

server = '127.0.0.1'
port = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((server, port))
except socket.error as exception:
    print(str(exception))

server_socket.listen(2)
print(f'Server started on {port}! Waiting for connections:\n')


def threaded_client(connection: socket, player: int):
    connection.send('Welcome')
    while True:
        try:
            data = connection.recv(2048).decode()

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", data)
                print("Sending: ", data)

            connection.sendall(data)
        except socket.error as ex:
            print(ex)

    print("Lost connection!")
    connection.close()


while True:
    conn, addr = server_socket.accept()
    print('New connection from: ', addr)

    start_new_thread(threaded_client, (conn, 0))
