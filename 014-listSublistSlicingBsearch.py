a = range(10)
a = a + [11]
print a
a = range(10)
a.append(11)
print a
a = range(10)
print a[0:5]
print a[5:10]
print a[-10:-5]
print a[-5:]
print a[4:]
print a[:-5]
print a[:4]
print a[0:10:2] # the last number is the way it moves to select
print a[::-1] # returns the list in reverse order without the need of "having" the size of the list
print a[:]
print "Existence of a value or key"
print "key = 5 ", 5 in a
print "key = 14 ", 14 in a
