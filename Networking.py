import socket
import threading


HEADER = 30
PRINT_DO = True

def set_header(integer):
    global HEADER
    HEADER = integer

class server:
    def __init__(self, PORT):
        self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = PORT
        self.SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ADDR = (self.IP, self.PORT)
        self.SERVER.bind(self.ADDR)
        if PRINT_DO:
            print(f"Server Hosted On {self.ADDR}")
        self.CLIENTS = []
    
    def listen_for_client(self):
        self.SERVER.listen()
        conn, addr = self.SERVER.accept()
        
