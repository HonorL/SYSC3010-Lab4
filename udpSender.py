# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, random

host = sys.argv[1]
textport = sys.argv[2]
textn = sys.argv[3]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
n = int(textn)
server_address = (host, port)
print(host, port)
msg_count = 1

while msg_count <= n:
    #random number in range [0,10]
    data = str(random.randint(0,10))
#    s.sendall(data.encode('utf-8'))
    s.sendto(data.encode('utf-8'), server_address)
    msg_count += 1
    buf, address = s.recvfrom(len(data)+5)
    print ("Received %s bytes from %s: %s" % (len(buf), address, buf ))

# s.shutdown(1)

