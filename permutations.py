def toString(List):
	return ''.join(List)
def permute(a, m, r):
	if m==r:
		print toString(a)
	else:
		for i in xrange(m,r+1):
			a[m], a[i] = a[i], a[m]
			permute(a, m+1, r)
			a[m], a[i] = a[i], a[m] 
string = "1234"
n = len(string)
a = list(string)
permute(a, 0, n-1)
