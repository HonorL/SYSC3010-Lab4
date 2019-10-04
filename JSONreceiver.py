import json, socket, sys, time

PACKET_SIZE = 100

textport = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('', port)
s.bind(server_address)

while True:

    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)

    buf, address = s.recvfrom(PACKET_SIZE)
    if not len(buf):
        break
    data = json.loads(buf)
    print ("Received %s bytes from %s: %s" % (len(buf), address, buf ))
    data = "ACK: " + buf.decode('utf-8')
    s.sendto(data.encode('utf-8'), address)

s.shutdown(1)