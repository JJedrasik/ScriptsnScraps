#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

#Clear screen...
subprocess.call('clear', shell = True)

#Get input
rmtServer = raw_input("Remote host server name is: ")
rmtServerIP = socket.gethostbyname(rmtServer)

#Output something...nicer?
print "-"*60
print"Scanning remote host......", rmtServerIP
print "-"*60

#Check what time scan started
t1 = datetime.now()

#Using the range funciton to specify ports..
#Maybe some error handling?

try:
    for port in range(1,2000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((rmtServerIP,port))
        if result == 0:
            print "Port {}: OPEN".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Cntrl + C"
    sys.exit()

except socket.gaierror:
    print "Cannot resolve hostname"
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

#check time again..
t2 = datime.now()

total = t2 - t1

print "Scan completed in: ", total
