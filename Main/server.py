
##########################################################################################
#																						  #																						
#				        Networking project-The Chat Room								  #  
#	                     Sichag Park and Sarthak Mishra									  #
#																						  #
#						                          										  #
#																						  #
#																						  #
##########################################################################################



import socket
import sys
from thread import *
from apscheduler.scheduler import Scheduler
import logging

logging.basicConfig()
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

if len(sys.argv)<3:
	print "Please Enter it in a valid way IP followed by port number"
	exit()


IP_ADDRESS= str(sys.argv[1])
port= int(sys.argv[2])
server.bind((IP_ADDRESS,port))
server.listen(100)
list_client = []
usernameTup=[]


usernameTup.append("UNameL")
usernameTup.append(",")
usernameTup.append("16")
usernameTup.append(",")
usernameTup.append("UsernameLength")
usernameTup.append(",")
usernameTup.append("MessageL")
usernameTup.append(",")
usernameTup.append("154")
usernameTup.append(",")
usernameTup.append("MessageLength")

list_add = ['Server Text:Existing Users:']
hasha ={}
s= Scheduler()
s.start()


def send_user():
	x =''.join(list_add)
	broadcast(x,server)

s.add_cron_job(send_user, second=0)

def clientThread(conn, adrss):
	useraa=''.join(usernameTup)
	conn.send(useraa)
	conn.send("\n")
	conn.send("Welcome")
	conn.send("\n")
	x =''.join(list_add)
	conn.send(x)
	msg=conn.recv(2048)
	msg1= msg.split(',')[2]
	print msg
	broadcast(msg1+" Joined",conn)
	while True:
		try:
			msg=conn.recv(2048)
			if msg:
				msg1= msg.split(',')[2]
				if msg1 in list_add:
					print msg
				else:
					list_add.append(msg1+",")
					hasha[conn]=msg1
					print msg
				broadcast(msg1+":"+msg.split(',')[3],conn)
			else:
				broadcast("x",)
				remove(conn)
		except:
			continue


def broadcast(msg,connection):
	for clients in list_client:
		if clients!=connection:
			try:
				clients.send(msg)
			except:
				w=hasha[clients]
				q="Server Text "+w+" left \n"
				list_add.remove(w+",")
				del hasha[clients]
				clients.close()
				remove(clients)
				broadcast(q,server)



def remove(connection):
	if connection in list_client:
		list_client.remove(connection)
		
          
while True:

	conn, adrss =server.accept()
	list_client.append(conn)

	print adrss[0]+ "connected"

	start_new_thread(clientThread,(conn,adrss))

conn.close()
server.close()
	











