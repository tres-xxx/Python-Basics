import time,sys
print "Time = ",time.asctime()
print "Name of the program = ", sys.argv[0]
if len(sys.argv) > 1:
	print "First variable passed to the program = ", sys.argv[1]
