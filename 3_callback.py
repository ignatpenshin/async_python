import socket
import selectors
# selectors is a high-level multiplexing tool

selector = selectors.DefaultSelector()


def server(): 
    server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_soc.bind(('localhost', 5001))
    server_soc.listen()

    selector.register(fileobj=server_soc, events=selectors.EVENT_READ, data=accept_con)



def accept_con(server_soc):
    client_soc, addr = server_soc.accept()
    print(addr, ' connected')

    selector.register(fileobj=client_soc, events=selectors.EVENT_READ, data=send_message)

def send_message(client_soc):

    request = client_soc.recv(4096)
    if request:
        response = "Hello".encode()
        client_soc.send(response)
    else:
        selector.unregister(client_soc)
        client_soc.close()


def event_loop():
    while True:
        
        events = selector.select() # (key --> object of SelectorKey, events --> just bit mask)
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)




if __name__ == '__main__':
    server()
    event_loop()