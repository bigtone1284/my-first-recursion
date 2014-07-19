def add_darray(x):
	j = 0
	for i in x:
		if type(i) == int:
			j += i
		else:	
			j += add_darray(i)
	
	return j 
	
	
#y = [1,[2,[3,4],[5,[6,7]]]]
#print add_darray(y)
