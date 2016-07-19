import sys
from socket import *

s = socket (AF_INET,SOCK_STREAM)
server_address = ('127.0.0.1',1500)
print>>sys.stderr,'connecting to %s port %s' %server_address
s.connect(server_address)
try:
    message = 'lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet'
    print >>sys.stderr,'mengirim pesan... \n "%s"' %message
    s.sendall(message)

    m_received = 0
    m_total = len(pesan)

    while m_received < m_total:
        data=s.recv(20)
        m_received +=len(data)
        print>>sys.stderr,'received "%s"' %data

finally:
    print>>sys.stderr,'socket closed'
    s.close()

