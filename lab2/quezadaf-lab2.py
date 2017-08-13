# Francisco Quezada, This work is mine unless otherwise cited.
#Lab 2 02/04/16
#
# COMMENT ALL CODE THAT YOU WRITE OR MODIFY.
#
# DELETE ANY COMMENTS OF MINE THAT DO NOT APPLY TO THE COMPLETED LAB
# (FOR EXAMPLE, THIS ONE OR THE ONE IN THE NEXT TWO LINES!)
# A primitive "Web server" (so primitive, in fact, that it ignores
# all HTTP syntax and merely returns the contents of a file).

from socket import *

# Create a new web server socket:
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare the server socket by choosing a port and then
# binding the socket to that port:
serverPort = 12345
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('',serverPort))

# Ready to receive requests:
serverSocket.listen(1)

while True:
    print '================='
    print 'Ready to serve...'
    print '================='

    # Wait for a connection request to arrive from a client: 
    connectionSocket, addr = serverSocket.accept()

    # A request arrived--process it
    try: 
        message = connectionSocket.recv(1024)

        # Split message up into lines and print them out for debugging:
        lines = message.split('\n') # split using newline character
        print "Received:"
        print "-----BEGIN-----"
        for line in lines:
          print line
        print "------END------"

# SOLUTION TO FIRST VERIFICATION TEST: MAKE SURE REQUEST HAS THREE FIELDS:
        # The first line should be the "GET" request; split it up into
        # its component words:
        requestline = lines[0].split() # split using whitespace
	requestline2 = lines[1].split() # split for Host
        filename = requestline[1] # second line, first array = hostname
	hostname = requestline[2] # second line, second array = hostname

        if len(requestline) != 3:
          #Send response message for bad request:
          connectionSocket.send('Error 400 Bad Request: need exactly 3 fields\n')

          #Close client socket
          connectionSocket.close()
          continue

	if requestline[0] != 'GET': # is GET in the first array of the first line
	  #Send response message for bad request:
	  connectionSocket.send('Error 400 Bad Request: need "GET" in cap locks\n')

          #Close client socket
          connectionSocket.close()
          continue

	if len(requestline2) != 2: # line 2 should have 2 arrays
          #Send response message for bad request:
          connectionSocket.send('Error 400 Bad Request: need exactly 2 fields\n')

          #Close client socket
          connectionSocket.close()
          continue

	if requestline2[0] != 'Host:': # is line 2, first array Host
	  #Send response message for bad request:
	  connectionSocket.send('Error 400 Bad Request: need "Host:" as shown\n')

          #Close client socket
          connectionSocket.close()
          continue

	if hostname != 'localhost': # is the hostname, line 2, second array, local host
	#Send response message for bad request:
	  connectionSocket.send('Error 400 Bad Request: need correct hostname\n')
	
	else:
          #Client Socket, send us the hostname
	  connectionSocket.send(hostname)
          #Close client socket
	  connectionSocket.close()
	  continue

	

        command = requestline[0]
        filename = requestline[1]
        protocol = requestline[2]

        # Assuming no errors in the format of the request, return the
        # requested file.

        # Obtain the file data (if no such file, exception is handled below):
        f = open(filename[1:])
        outputdata = f.read()

        #Send HTTP header lines into socket
        connectionSocket.send('HTTP/1.1 200 OK\n')
        connectionSocket.send('Date: Thu, 04 Jan 2016 14:30:00\n')
        connectionSocket.send('Last-Modified: Thu, 04 Feb 2016 14:40:00\n')
        connectionSocket.send('Content-Type: text/html\n')
        connectionSocket.send('\n')

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])

        # Once file is transferred, close connection:
        connectionSocket.close()

    except IOError: # Couldn't locate file
        #Send response message for file not found
        connectionSocket.send('Error 404 File Not Found\n')

        #Close client socket
        connectionSocket.close()

# The next line is not reachable because of the infinite loop!
serverSocket.close()
