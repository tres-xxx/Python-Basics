call = 0
def add3num(x,y,z):
	global call
	call = call + 1
	return x+y+z
print add3num(3,2,1)
print add3num(2,3,4)
print call
