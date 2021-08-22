import socket
import time
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 5051))
s.send(bytes('LoginAPP', 'utf-8'))

def main():
    pass

def login():
    time.sleep(1)
    user = input('Username: ')
    pwd = input('Password: ')

    s.send(bytes(user, 'utf-8'))
    time.sleep(1)
    s.send(bytes(pwd, 'utf-8'))

    if s.recv(5000).decode('utf-8') == 'Authenticated':
        print('Authenticated')
        main()
    else:
        print(s.recv(5000).decode('utf-8'))

login()

