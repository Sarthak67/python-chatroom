

                  Readme 

Connection: 
When the server started:
Thread starts to accept connections from the clients
Client side when it starts connection:
Input: ip port number and username(which is limited to 16)
Server side: accept the connection add new user to the user list and broadcast the new user arrived.
Process
		 When new connection arrives it gets added to the connection list and , that list is broadcasted amongst the existing users
		 It then gets hashed with the dictionary datatype variable hasha . Hasha hashes all the Ip address with the connection socket object.
	

When the clients send chats:
Client side: send a chat (if it’s more than 154 length it will not fit in the header format so not accepted)
Server side: thread reads the input and broadcast it to the users.
		 First of all the server sends the tuple containing UnameL , size=16 ,”Description ” and MessageL , size=154 ,”Description ” to the client
		 And the client sets the standard user and standard msg size as manifested by the Server.
		 The Standard template is checked on both Server and Client unit. Client return the username and msg to the user id the username is less than 16 characters long , and msg is less than 154 characters long.
				 similarly when the tuple arrives to the server, we split it using commas and the server checks for the correct formatting of the tuple .
		                  Then the split ed tuple is broadcasted amongst the existing clients.

Every once in a while:
Server side : send everyone about the existing users.
(add diagram)
		 We have used apscheduler from Scheduler library  to  broadcast  the existing users every mins.
		 The send_user function has been initialized to a clock of scheduler library, which send the list_add variable to all the users everys minutes	

When the clients leave the chats:
Client side: quit the chat by closing
Server side: Send every users about one users’ leaving
(add diagram)
		 As the Existing Users list is being broadcasted amongst the users , the server checks for all the users in client list , if the sending fails it declares that user to be offline and broadcast msg amongst all online users