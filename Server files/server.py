import socket, time, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 5050))
s.listen()

def register_socket(user, pwd, conn):
    with open('login.txt', 'r') as file:
        for i in file:
            if user in i:
                conn.send(bytes('Username not avilable', 'utf-8'))
                i = i
        if user not in i:
            register(user, pwd, conn)




def register(user, pwd, conn):
    with open('login.txt', 'a') as file:
        file.write(f'\n{user}:{pwd}')
        conn.send(bytes('Registered!', 'utf-8'))

def login_socket(user, pwd, conn):
    with open('login.txt', 'r') as file:
        for i in file:
            if f'{user}:{pwd}' in i:
                conn.send(bytes('Authenticated', 'utf-8'))
            elif user and not pwd in i:
                conn.send(bytes('Wrong password', 'utf-8'))
            else:
                conn.send(bytes('Incorrect login', 'utf-8'))




def check(addr, conn):
    content = conn.recv(5000).decode('utf-8')

    if content == 'LoginAPP':
        print(f'New connection from {addr} logging in...')
        user = conn.recv(5000).decode('utf-8')
        pwd = conn.recv(5000).decode('utf-8')

        logining = threading.Thread(target=login_socket, args=(user, pwd, conn))
        logining.start()

    elif content == 'RegisterAPP':
        print(f'New connection from {addr} Registering...')
        user = conn.recv(5000).decode('utf-8')
        pwd = conn.recv(5000).decode('utf-8')

        registering = threading.Thread(target=register_socket, args=(user, pwd, conn))
        registering.start()

while True:
    conn, addr = s.accept()

    check_thread = threading.Thread(target=check, args=(addr, conn))
    check_thread.start()

print('[+] Starting listener')
while True:
    check()
