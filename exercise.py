# function to do an accumulative sum
def cum_sum(x):
	y = []
	for xx in x:
		z = 0
		for yy in x[0:xx]:
			z = z + yy
		y.append(z)
	return y
def unique(x):
	y = []
	t = 0
	for xx in x:
		exist = False
		if xx in x[t+1:]: exist = True
		if xx in x[:t]: exist = True
		if not exist: y.append(xx)
		t = t+1
	return y
print cum_sum([1,2,3,4])
print unique([1,1,2,3,3,4])
