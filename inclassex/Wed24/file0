# In-class exercise, 24 February 2016

filename = raw_input("Copy what file? ")

try:
   inputfile = open(filename,'rb')
   outputfile = open(filename+"copy",'wb')
   blockcount = 0
   while True:
      block = inputfile.read(1024)
      if block:
         blockcount += 1
         outputfile.write(block)
      else:
         break;
   inputfile.close()
   outputfile.close()
   print "copied " + str(blockcount) + " blocks"

except IOError:
   print "bad input or output file"
