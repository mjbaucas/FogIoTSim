# size of block - in bytes
# 2 - 120
# 109 - 1080 
# 235 - 2200
# 456 - 4216
# 971 - 8800~
# 1788 - 16184
# 3650 - 33048

import sys

import socket
import time
from utils import size_selector, send_msg, recv_msg

host_ip = sys.argv[1]
port = int(sys.argv[2])
data = size_selector(sys.argv[3])
limit = 120

transmission_time = []
process_time = []

for i in range(0,3):
    total = 0.0
    total_process = 0.0
    counter = 0

    timer = time.time()
    current = time.time()
    while current-timer < limit:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host_ip, port))
        start = time.time()
        send_msg(s, str.encode(data))
        recieved = recv_msg(s)
        end = time.time()
        diff_net = end-start
        diff = end-current
        current = end
        print(total_process)
        total += diff
        total_process += ((diff - diff_net) + (float(recieved)/1000))
        counter += 1

    print("Total Time: " + str(total))
    print("Total Packets: " + str(counter))
    print("Average time: " + str(total/counter))
    transmission_time.append(total/counter)
    print("Average Processor time: " + str(total_process/counter))
    process_time.append(total_process/counter)

print("Average Times: " + str(transmission_time))
print("Average Processor Times: " + str(process_time))

