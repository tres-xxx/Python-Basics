x = 41
def iseven(x):
	if x % 2 == 0: print "even"
	else: print "odd"
	return " "
print "Number x = ", x, " is even? ", iseven(x)
def size2digits(x):
	if x < 10 == 0: print "one digit"
	elif x < 100: print "two digits"
	else: print "too much digits"
	return ""
print "Number = ", x, " size = ", size2digits(x)
print "Number = 123 size = ", size2digits(123)
