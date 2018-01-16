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
import select
import sys



sendMessage=[]
lengthMsg=[]
newCode=[]
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

if len(sys.argv)<3:
	print "Please Enter it in a valid way IP followed by port followed by username"
	exit()


IP_ADDRESS = str(sys.argv[1])
port = int(sys.argv[2])
server.connect((IP_ADDRESS,port))
user =str(sys.argv[3])
length1=sys.getsizeof(user)-38

def set_user(useer,mbbs,l):
	userName =[]
	if length1<mbbs:
		userName.append(useer)
		userName.append(",")
		userName.append(str(length1))
		userName.append(",")
		userName.append("USERNAME")
		x =''.join(userName)
		server.send(x)
		userName =[]
	else:
		print "please re choose the username in less than 16 characters"
		exit()


def send_it(message):
	server.send(message)
	#sys.stdout.write("You "+message.split(',')[0])
	sys.stdout.flush()


while True:

	sockets_list = [sys.stdin,server]
	

	read_sockets,write_sockets,error_sockets= select.select(sockets_list,[],[])
    
	for socks in read_sockets:
		
		if socks ==server:
			
			message =socks.recv(2048)
		
			if message.split(',')[0] =="UNameL" and message.split(',')[3]=="MessageL":
				lengthUser=int(message.split(',')[1])
				set_user(user,lengthUser,length1)
				lengthMsg.append(message.split(',')[4])

			print message
			
		else:
			message= sys.stdin.readline()
			length2=sys.getsizeof(message)-38
			if length2<int(lengthMsg[0]):
				sendMessage.append(str(message))
				sendMessage.append(",")
				sendMessage.append(str(length2))
				sendMessage.append(",")
				sendMessage.append("MESSAGE")
				newCode.append(str(length1))
				newCode.append(",")
				newCode.append(str(length2))
				newCode.append(",")
				newCode.append(user)
				newCode.append(",")
				newCode.append(str(message))
				if len(sendMessage)<=0:
					sendMessage=[]
					newCode=[]
				z =''.join(sendMessage)
				k=''.join(newCode)
				print k
				send_it(z)
				sendMessage=[]
				newCode =[]

			else:
				print "overSize msg pleas limit it to 154 characters"
			



		
server.close()