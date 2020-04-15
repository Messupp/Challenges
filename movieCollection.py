'''
n = movies in stack
m = number of movies wants to watch
movies = array representing the ID numbers of movies he wants

output = array with integers of boxes above

84,887,[10,20,30,32,11,73,58,74,3,20,63,68,84,71...
	    9,19,29,31,13,72,58,73,10,7,64,69,83...

'''

class Solution:

	def run(self, n, m, movies):
		#
		# Write your code below; return type and arguments should be according to the problem's requirements
		#
		
		stack = []

		for i in range(n):
			stack.append(i+1)

		result = []
		for movie in movies:
			for i in range(len(stack)):
				if stack[i] == int(movie):
					result.append(i)
					stack.pop(i)
					stack.insert(0,movie)
					
		movies_array = ",".join(str(x) for x in result)
		return movies_array

n = 3
m = 3
movies = [3,1,1]
# "3,0,4"
Solution.run("", n,m,movies)