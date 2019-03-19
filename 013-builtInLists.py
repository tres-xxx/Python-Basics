# the function range creates an incremental list
a = range(4)
print a
a = range(0,4)
print a
a = range(0,4,1)
print a
print "All were getting in the same way?... nop"
a = [1,2]
b = [3,4]
print a+b
print a*2
a = range(4)
print "[",a[0],",",a[1],",",a[2],",",a[3],"]"
print "[",a[-4],",",a[-3],",",a[-2],",",a[-1],"]"
print sum(a)
b = ['d','c','b','a']
fx = zip(a,b)
print min(fx)
print max(fx)
