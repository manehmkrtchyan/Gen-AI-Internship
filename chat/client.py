import threading 
import socket
alias = input('Choose an alias>>>')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))

def client_recieve():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'alias?':
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('ERROR!')
            client.close()
            break

def client_send():
    while True:
        message = (f'{alias}: {input("")}').encode('utf-8')
        client.send(message)

receive_thread = threading.Thread(target=client_recieve)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()