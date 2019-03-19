x = range(4)
for t in x:
	print t
for x in [1,2,3,4]:
	print x
for x in range(4):
	print x
# To make a pair (or more) of a list the word zip is used
print "------"
x = ['a','b','c']
xx = range(3)
print x,xx
fx = zip(x,xx)
print fx
for x, xx in fx:
	print x, xx
