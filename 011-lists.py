def sizeList(x, add = 0,pos = 0):
	if pos < len(x):
		return sizeList(x, add = add + len(x[pos]), pos = pos+1)
	else: return add
x = [1,2,3]
y = ["hello","guy"]
z = [x, y, ["another","list"]]
print x, " tamano = ", len(x)
print y, " tamano = ", len(y)
print z, " tamano = ", sizeList(z)
