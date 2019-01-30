import socket
import threading
from queue import Queue

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s)
server = 'pythonprogramming.net'
port = 80

server_ip = socket.gethostbyname(server)


request = "GET / HTTP/1.1\nHost: "+server +"\n\n"
s.connect((server,port))
s.send(request.encode())
result = s.recv(4096)
while (len(result) > 0):
    print(result)
    result = s.recv(4096)

###############################################THREADED PORT SCANNER###################################3###

print_lock = threading.Lock()
ip_address = 'pythonprogramming.net'
def pscan(prt):
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = sckt.connect((ip_address,port))
        with print_lock:
            print('port',prt,'is open')
        con.close()
    except:
        pass
def threader():
    while True:
        worker = q.get()
        pscan(worker)
        q.task_done()
q = Queue()
for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()
#testing first 100 ports
for worker in range(1,101):
    q.put(worker)

q.join()