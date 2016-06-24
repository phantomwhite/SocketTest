import socket
from time import ctime
import threading

def tcplink(tcpClientSock,addr):
    total = b''
    while True:
        try:
            data=tcpClientSock.recv(1024)
            if not data or len(data) < 1024:
                break
            total += data
        except Exception as e:
            print(e)
            tcpClientSock.close()
            break
    #s='Hi,you send me :[%s] %s' %(ctime(), data.decode('utf8'))
    print([ctime()], ':', total.decode('utf8'))
    s = input('>')
    tcpClientSock.send(s.encode('utf8'))

    tcpClientSock.close()

HOST = '192.168.2.109'
PORT=54321
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen(5)
while True:
    print('waiting for connection')
    tcpClientSock, addr=sock.accept()
    print('connect from ', addr)

    t = threading.Thread(target=tcplink, args=(tcpClientSock,addr))
    t.start()
    
sock.close()

