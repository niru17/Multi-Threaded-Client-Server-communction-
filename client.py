import socket
import time

def main():         
    host = '127.0.0.1'
    port = 8000 

    s = socket.socket()
    s.connect((host, port))
    print("Connected to server")
    print("*" * 50)
    print("Select either of one: PUT GET DUMP")
    message = input()
    while message != 'q':
        s.send(message.encode())
        time.sleep(2)
        data = s.recv(1024).decode()
        print(data)
        print("*" * 50)
        print("Select either of one: PUT GET DUMP")
        message = input()
    s.close()

if __name__ == '__main__':
    main()