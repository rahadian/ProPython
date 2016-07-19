import sys
from socket import *

s = socket(AF_INET,SOCK_STREAM)
server_address = ('127.0.0.1',1500)
print >>sys.stderr,'build up server %s port %s' %server_address
s.bind(server_address)
s.listen(5)

while True:
    connection,client_address = s.accept()
    print>>sys.stderr,'waiting connection ...'

    try:
        print>>sys.stderr,'connection from ', client_address

        while True:
            data=connection.recv(20)

            if data:
                connection.sendall(data)
                print>>sys.stderr,'sending back to client...'

            else:
                print>>sys.stderr,'no more data in client...'
                break

    finally:
        connection.close()
