#modules
import os, sys, time
from time import sleep as timeout
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
#banner
os.system("clear")
os.system("figlet Web-Hunter")
print
print "     [01]> nmap  "
print "     [02]> hydra"
print "     [03]> sqlmap"
print
A = input("Web-Hunter >>> ")

if A == 1 or A == 01 :
  Nmap = raw_input("Target Host/Ip >>> ")
  os.system("nmap %s" %(Nmap))
  timeout(15)
  restart_program()

elif A == 2 or A == 02 :
    os.system("python2 brute.py")

elif A == 3 or A == 03 :
    os.system("sqlmap --sqlmap-shell")

elif A == 0 or A == 00 :
    sys.exit()

else:
    print "Errer Input !!!!!!"
    timeout(3)
    restart_program()
