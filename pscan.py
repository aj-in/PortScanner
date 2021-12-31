

#!/usr/bin/python3

import socket            
import  sys        #to exit program ,to recivee argument
import time        #to calucte timefor scan
import threading

usage ="python3 pscan.py TARGET START_PORT END_PORT"   # 4 arguments 

print(""" 
    ____             __  _____                                 
   / __ \____  _____/ /_/ ___/_________ _____  ____  ___  _____
  / /_/ / __ \/ ___/ __/\__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 / ____/ /_/ / /  / /_ ___/ / /__/ /_/ / / / / / / /  __/ /    
/_/    \____/_/   \__//____/\___/\__,_/_/ /_/_/ /_/\___/_/     
                                                            """)
print("                                                  | Version: 1.0 | By -- AJ |")
print("-"*70)

start_time  = time.time()

if(len(sys.argv) != 4 ):
    print(usage)
    sys.exit()


try:
    target = socket.gethostbyname(sys.argv[1])

except socket.gaierror:            #g(get) a(address) i(info)
    print("Name resolution error(name maybe incorrect")
    sys.exit()


start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target ",target)

def scan_port(port):


    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # a(address) f(family) of internet
    
    s.settimeout(2)        # if open port not is not availabe under 2 sec we stop process
    conn = s.connect_ex((target, port))   # connect_ex used so that we dont terminate after one failure

    
    if(not conn):       # OR conn == 0
         print(f"port {port} is OPEN ")
    s.close()


for port in range(start_port,end_port+1):  # iterate from start to end
    thread = threading.Thread(target =scan_port,args = (port,))
    thread.start()


end_time = time.time()
final_time =end_time-start_time
print(f"Time elapsed is: {final_time} s")

    















