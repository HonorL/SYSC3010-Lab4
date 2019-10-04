import json, socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)
print(host, port)
msg_count = 1

#x = '{ "name":"John", "age":30 "city":"New York"}'
# python dictionary

pydict = {
  "name": "John",
  "age": 30,
  "city": "New York"
}


while msg_count <= 10:

    pydict['age'] += 1

    jsondict = json.dumps(pydict)
    print(jsondict)
    
    s.sendto(jsondict.encode('utf-8'), server_address)
    msg_count += 1
    buf, address = s.recvfrom(len(jsondict)+5)
    print ("Received %s bytes from %s: %s" % (len(buf), address, buf ))






