import os
print("Current working Directory:",os.getcwd())
print("Process id:",os.getpid())

fd=os.open("demo.txt",os.O_RDWR|os.O_CREAT)
os.write(fd,b"Hello Ayusman")
os.lseek(fd,0,0)
data=os.read(fd,100)
print(data.decode())
os.close(fd)

import sys
print("Enter Something:")
data=sys.stdin.readline()
print("You Entered: ",data)