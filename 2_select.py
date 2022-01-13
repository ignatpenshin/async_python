import socket
import select

to_monitor = []

server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_soc.bind(('localhost', 5001))
server_soc.listen()

def accept_con(server_soc):
    client_soc, addr = server_soc.accept()
    print(addr, ' connected')
    to_monitor.append(client_soc)

def send_message(client_soc):

    request = client_soc.recv(4096)
    if request:
        response = "Hello".encode()
        client_soc.send(response)
    else:
        client_soc.close()


def event_loop():
    while True:
        ready_to_read, _, _ = select.select(to_monitor, [], []) # r, w, err

        for sock in ready_to_read:
            if sock is server_soc:
                accept_con(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    to_monitor.append(server_soc)
    event_loop()