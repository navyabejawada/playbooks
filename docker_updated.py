import os
import subprocess
import docker
import sys

option=''
try:
 option=sys.argv[1]
except:
 pass

if option=='Help':
    file1 = open("myfile.txt","r+")
    print file1.read() 
else:
    apikey = input("enter apikey: ")
    a = 1
    while(a==1):
        mac = input("enter macaddress: ")
        FNULL = open(os.devnull, 'w')
        retcode = subprocess.call(["docker","build", "-t", "navya","."])
        subprocess.call(["docker","run","navya:latest",apikey,mac])
        a = int(input("do you want check another mac if yes enter 1 otherwise enter 0: "))
