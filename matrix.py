import operator
import itertools
class Matrix:
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
	
	def zeros(self, n):
		z = list(itertools.repeat([0 for i in range(n)], n))
		z[1][0] = 2	
		return self.__repr__(z)
		
	def ones(self, n):
		z = list(itertools.repeat([1 for i in range(n)], n))
		return self.__repr__(z)
		
	def diagonal(self, n, k=1):
		z = [[0 for j in range(n)] for i in range(n)]
		for j in range(n):
			z[j].insert(j , k)
			#z[j].remove(z[j][-1])	
		return self.__repr__(k*z)
				
	def __str__(self, a):
		return f"Matrix({a})"
	
	def __repr__(self, a):
		return self.__str__(a)#f"Matrix({a})"
			
c = Matrix([1,2,3], [4,4,5], [10, 0, 7])
d = Matrix([1,2,3], [4,4,5], [3, 5, 5])
print(c.diagonal(3))
print(c+d)
print(c-d)
print(c*d)
print(c/d)