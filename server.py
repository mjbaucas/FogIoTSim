import socket, sys, time
from utils import send_msg, recv_msg
 
host_ip = sys.argv[1]  
port = int(sys.argv[2])

print('host ip: ', host_ip)# Should be displayed as: 127.0.1.1  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.bind((host_ip, port))  
s.listen(10)  
while True:  
    #print('Hello')
    current = time.time()
    conn, addr = s.accept()  
    print('Connected by', addr)  
    data = recv_msg(conn)
    if not data: 
        break
    elapsed = time.time()
    send_msg(conn, str.encode(str(elapsed-current)))# Send back the received data intact
    print('Received', repr(data))  
    conn.close()