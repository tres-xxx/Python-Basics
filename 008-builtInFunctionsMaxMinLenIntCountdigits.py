x,y = 10,15
print "var x = ", x, "var y = ", y
print "min = ", min(x,y)
print "max = ", max(3,4)
word = "This is a word"
print "String = \"", word, "\""
print "lenth = ", len(word)
#print "String to int = ", int(word)
print "Int to string = ", str(x), " ...psst... is the same but different"
def count_digits(x, sum = 0):
	if (x/10) > 0:
		return count_digits(x/10, sum = sum+1)
	sum = sum + 1
	return sum
print "Count digits (12345)= ", count_digits(12345)
