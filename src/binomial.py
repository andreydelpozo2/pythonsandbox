def factorialRec(n):
	if n < 0 or type(n) != int:
		raise ValueError("argument has to be a non-negative integer")
	if n == 1 or n == 0:
		return 1
	
	return n*factorialRec(n-1)

def factorial(n):
	if n < 0 or type(n) != int:
		raise ValueError("argument has to be a non-negative integer")
	
	if n == 1 or n == 0:
		return 1
	
	v = n
	n = n-1

	while n > 1:
		v = v * n
		n = n-1
	
	return v
		
def binomial(n,k):
	return factorial(n)/(factorial(k)*factorial(n-k));


def binomialRec(r,n,k):

	if n == k or k == 0:
		return 1

	if k > n or n == 0:
		return 0

	if r[k-1][n-1] == -1:
		r[k-1][n-1] = binomialRec(r,n-1,k-1)

	if r[k][n-1] == -1:
		r[k][n-1] = binomialRec(r,n-1,k)	

	return r[k-1][n-1] + r[k][n-1];


def binomial2(n,k,res=None):
	if res ==None:
		res = [[-1]*(n+1) for i in xrange(k+1)]

	res[k][n] = binomialRec(res,n-1,k-1) + binomialRec(res,n-1,k)
	return res[k][n]

def binomial3(n,k,res=None):
	if res ==None:
		res = [[-1]*(n+1) for i in xrange(k+1)]

	for i in xrange(len(res)):
		res[i][0] = 0;

	for i in xrange(len(res[0])):
		res[0][i] = 1;
		res[1][i] = i

	for i in xrange(len(res[0])):
		if i >= len(res):
			break
		res[i][i] = 1;

	for i in xrange(1,n+1):
		for j in xrange(1,k+1):
			res[j][i] = res[j-1][i-1] + res[j][i-1]
	
	return res[k][n]

def binomial4(n,k,res=None):
	if res ==None:
		res = [[-1]*(n+1) for i in xrange(k+1)]

	for i in xrange(n+1):
		for j in xrange(k+1):
			
			if j == 0:
				res[j][i] = 1
				continue
			if j == 1:
				res[j][i] = i
				continue
			if i == 0:
				res[j][i] = 0
				continue
			if i == j:
				res[j][i] = 1
				continue

			res[j][i] = res[j-1][i-1] + res[j][i-1]
	
	return res[k][n]
