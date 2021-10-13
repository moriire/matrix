import operator
import itertools
class Arith:
	def __init__(self,  *row):
		self.row = row
		
	def __iter__(self):
		return [*self.row]
		
	def __len__(self):
		return len(self.row[0])
		
	def __diff(self, t):
		return t[0] - t[1]
		
	def __mul__(self, other):
		z = []
		if len(self.row) == len(other.row):
				for s in range(len(self.row)):
					z.append(list(map(operator.mul, list(self.row[s]), list(other.row[s]))))
		return self.__repr__(z)
		
	def __truediv__(self, other):
		z = []
		if len(self.row) == len(other.row):
				for s in range(len(self.row)):
					z.append(list(map(operator.truediv, list(self.row[s]), list(other.row[s]))))
		return self.__repr__(z)
	
	def __add__(self, other):
		z = []
		if len(self.row) == len(other.row):
			s = 0
			l = len(self.row)
			while s < l:
			   	x = tuple(zip(self.row[s], other.row[s]))
			   	
			   	z.append(x)
			   	s += 1
			w = [list(map(sum, j)) for j in z]
			return self.__repr__(w)
			
	def __sub__(self, other):
		z=[]
		if len(self.row) == len(other.row):
			s = 0
			l = len(self.row)
			while s < l:
			   	x = list(zip(self.row[s], other.row[s]))
			   	
			   	z.append(x)
			   	s += 1
			w = [list(map(self.__diff, j)) for j in z]
			return self.__repr__(w)
		
	def size(self):
		return len(self.row), len(self)
			
	def __str__(self, a=None):
		if a is None:
			return f"Matrix({self.row})"
		return f"Matrix({a})"
	
	def __repr__(self, a):
		return self.__str__(a)

def zeros(n):
	z = list(itertools.repeat([0 for _ in range(n)], n))
	return z
		
def ones(n):
	z = list(itertools.repeat([1 for _ in range(n)], n))
	return Matrix(*z)
		
def diagonal(n, k=1):
	z = [[0 for _ in range(n)] for _ in range(n)]
	for j in range(n):
		z[j].insert(j , k)
	w = list(map(lambda li: li[:-1], z))
	return Matrix(*w)

class Matrix(Arith):
	def __init__(self, *row):
		super().__init__(*row)
		self.row = row

	def reverse(self, li):
		w = list(zip(*li))
		return w

	def dot(self, li):
		d = []
		rev = self.reverse(li)
		mul =list(zip(rev, li))
		j = [list(zip(*j)) for j in mul]
		for i in j:
			return list(map(lambda x: operator.__mul__(*x), i))

	def cofactors(self):
		return [pow(-1, n+1)*self.row[0][n] for n in range(len(self.row[0]))]

	def transpose(self, *li):
		v = []
		length = len(li[0])
		for l in range(length):
			m = list(zip(*li[1:]))
			m.remove(m[l])
			v.append(m)
		return v
