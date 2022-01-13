from Ssocket import Socket
from threading import Thread

class Client(Socket):
    def __init__(self):
        super(Client, self).__init__()
        
    def set_up(self):
        self.connect(
            ("127.0.0.1", 8080)
        )
        listen_thread = Thread(target=self.listen_socket)
        listen_thread.start()

        send_thread = Thread(
            target=self.send_data
            )

        send_thread.start()

    def send_data(self):
        while True:
            self.send(input(":").encode())

    def listen_socket(self, listened_socket = None):
        while True:
            data = self.recv(1024) #take 1024 bites from server
            print(data.decode("utf-8"))


if __name__ == "__main__":
    client = Client()
    client.set_up()
    
