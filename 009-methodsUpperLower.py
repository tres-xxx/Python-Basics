s = "up"
s2 = "DOWN"
print "Strings = ", s, " ", s2
print "Up => ", s.upper()
print "Down => ", s2.lower()
print "Compare two strings"
def istrcmp(s,ss):
	if s.upper() == ss.upper():
		print True
		return
	print False
istrcmp(s="uP",ss="Up")
istrcmp(s,s)

