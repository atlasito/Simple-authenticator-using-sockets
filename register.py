import socket
import time

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 5051))
c.send(bytes('RegisterAPP', 'utf-8'))


def register():
    time.sleep(1)
    user = input('Username: ')
    pwd = input('Password: ')

    c.send(bytes(user, 'utf-8'))
    time.sleep(1)
    c.send(bytes(pwd, 'utf-8'))

    print(c.recv(2041).decode('utf-8'))

register()