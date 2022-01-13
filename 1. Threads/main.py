from Ssocket import Socket 
import threading

class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()
        self.users = []

    def set_up(self):
        self.bind(('', 8080))
        self.listen()
        self.start_server()

    def send_data(self, data):
        for user in self.users:
            user.send(data)

    def listen_socket(self, listened_socket):
        print(f"Listening user: {listened_socket}")
        while True:
            data = listened_socket.recv(1024)
            print(f"User sent {data}")
            self.send_data(data)

    def start_server(self):
        while True:
            user_socket, address = self.accept()
            print(f"user <{address[0]}> connected!")
            self.users.append(user_socket)
            listen_accepted_user = threading.Thread(
                target=self.listen_socket, 
                args=(user_socket,)
            )

            listen_accepted_user.start()
            # user sends messages
            print('!')
        

if __name__ == '__main__':
    server = Server()
    server.set_up()