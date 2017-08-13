# Francisco Quezada, This work is mine unless otherwise cited.
# Lab 3 02/18/16
#
# COMMENT ALL CODE THAT YOU WRITE OR MODIFY.
#
# We need the time package to calculate round-trip times
# Source: Professor Roos
import time 

from socket import *

#host = localhostname
port = 12345
timeout = 1 # in seconds
addr = ("",port)
 
# Create UDP client socket
# Note the use of SOCK_DGRAM for UDP datagram packet
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set socket timeout as 1 second
clientSocket.settimeout(1)


# Ping 10 times:

success = 0
unsuc = 10
ecount = 0

for i in range(1,11):
    message = 'ping # ' + str(i)
    try:
        print "Sending: " + message
	# Save current time (this is the start time):
	start = time.time()
	# Send the UDP packet containing the ping message
	clientSocket.sendto(message, addr)
	# Receive the server response
	data, server = clientSocket.recvfrom(1024)
	success = success + 1
	# Save current time (this is the end time)
	end = time.time()
	# elapsed
	elapsed = end - start
	ecount = ecount + elapsed
	# Display the server response as an output (elapsed=?)
	print str(data) + " " + str(i) + " " + str(elapsed)
	# print round trip time (difference between end time and start time):

    except:
        # Server does not respond; assume packet is lost and print message:
	print 'Requested Time Out'
    continue
# Number of Successes
print "Number of successes: " + str(success)

# Number of Unsuccessful
print "Number of Unsuccessful: " + str(unsuc-success)

# Average
print "Average: " + str(ecount/success)


# Close the client socket
clientSocket.close()
 
