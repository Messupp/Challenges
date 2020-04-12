'''



'''
class Solution:

	def run(self, number):
		#
		# Write your code below; return type and arguments should be according to the problem's requirements
		#
		isSemiprime = 'false'
		cons = 10**8
		if number > cons:
			print('Too big')


		def divideCheck(number):
			prime = True
			halfNumber = number // 2
			upToNumbers = []
			for i in range(2,halfNumber+1):
				upToNumbers.append(i)

			divisibleNumbers = []

			for i in upToNumbers:
				if number % i == 0:
					divisibleNumbers.append(i)
					prime=False
			return divisibleNumbers, prime

		divisibleNumbers,prime = divideCheck(number)

		primeList = []
		for numberDiv in divisibleNumbers:
			alist, prime = divideCheck(numberDiv)
			if prime == True:
				primeList.append(numberDiv)

		primeListA = primeList
		primeListB = primeList

		for primeA in primeListA:
			for primeB in primeListB:
				if primeA * primeB == number:
					isSemiprime = 'true'
			
		return isSemiprime




Solution.run("", 2)