import socket
import sys
import threading
import time

class Server:                                       #Server class
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.cache = {}
        self.proxy = {}

    def listen(self):                                         #This function listens to the connected port
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            print("Connected with ",address)
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):                   #Connects with client
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Sends the response back to the recieved data
                    response = self.process_data(data)
                    client.send(response)
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

    def process_data(self, data):                                #This function handles Put,Get and Dump data from the server side
        data = data.decode('utf-8')
        if data.startswith('PUT'):
            print("Start keyValDict: ",self.cache)
            print("messageReceivedFromClient : ",data)
            print("---PUT---")
            data = data.split(' ')[1]
            print(data)
            key, value = data.split('=')
            self.cache[key] = value
            print("KeyValDict: ",self.cache)
            return f'Request forwarded to the SERVER\n\nOutput: {data}'.encode('utf-8')
        elif data.startswith('GET'):
            key = data.split(' ')[1]
            if key in self.proxy:
                return f"Request forwarded to the SERVER\n\nOutput (From Proxy Server) : {self.proxy[key]}".encode('utf-8')
            elif key in self.cache:
                print("Start keyValDict: ",self.cache)
                print("messageReceivedFromClient : ",data)
                print("---GET---")
                print("responseTOclient: ",self.cache[key])
                print("KeyValDict: ",self.cache)
                self.proxy[key] = self.cache[key]
                return f"Request forwarded to the SERVER\n\nOutput: {self.cache[key]}".encode('utf-8')
            else:
                return 'Key not found'.encode('utf-8')
        elif data.startswith('DUMP'):
            print("Start keyValDict: ",self.cache)
            print("messageReceivedFromClient : ",data)
            print("---DUMP---")
            print("KeyValDict: ",self.cache)
            return str("Request forwarded to the SERVER\n\nOutput: "+" ".join(self.cache.keys())).encode('utf-8')
        else:
            return 'Invalid command'.encode('utf-8')
        

if __name__ == "__main__":
    port_num = int(8000)
    try:
        server = Server('',port_num)
        print("Socket created")
        print("Waiting for Client to get connected!")
        server.listen()
    except KeyboardInterrupt:
        print('Server stopped')
        sys.exit()