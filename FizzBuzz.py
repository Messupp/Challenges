'''
FizzBuzz Challenge
If number is divisible by 3 - Fizz
If number is divisible by 5 - Buzz
If number is divisible by 3 and 5 - FizzBuzz


'''

class Solution:

	def run(self, N, M):
		#
		# Write your code below; return type and arguments should be according to the problem's requirements
		#
		alist = []

		# 5,6,7,8,9,10,11,12,13,14,15
		for i in range(N,M+1):
			if i % 15 == 0:
				alist.append('FizzBuzz')
			elif i % 3 == 0:
				alist.append('Fizz')
			elif i % 5 == 0:
				alist.append('Buzz')
			else:
				alist.append(i)


		sequence = ', '.join((map(str, alist)))
		
		return sequence
