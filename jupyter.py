#!/usr/bin/python3
import cgi
import subprocess
import cgitb
import random
import time
from IPython.lib import passwd
cgitb.enable()
print("Content-type: text/html\r\n\r\n")
print("<center><h1>HI there launching a jupyter notebook please wait </h1></center>")
form = cgi.FieldStorage()
password=passwd(form.getvalue("passwd"))
print("<center>")
ports=[line.split(":")[-1] for line in subprocess.getoutput("netstat -tunlep | grep LISTEN | awk '{print $4}'")]
print('</br><img src="https://i.gifer.com/W5IY.gif">')
while True:
        port=random.randrange(2000,65535)
        if port not in ports:
                break
port=str(port)
try:
        subprocess.getoutput("sudo docker run -d -p "+port+":8888 jupyter/datascience-notebook start-notebook.sh --NotebookApp.password='"+password+"'")
        url="http://13.235.104.102:"+port
        print('<meta http-equiv="Refresh" content="3; url='+url+'" />')
except:
        print("Can't start conatiner sorry")
print("</br>")
print("</center>")