'''
1954  MCMLIV
1990 MCMXC
2014 MMXIV
1993 MCMXCIII
9999 MMMMMMMMMCMXCIX

'''

class Solution:

	def run(self, n):
		romanValues={'M':1000,'CM':900,'D':500 ,'CD':400,'C':100 ,'XC':90,'L':50 ,'X':10 ,'IX':9 ,'VIII':8, 'VII':7 ,'VI':6 ,'V':5 ,'IV':4 ,'III':3 ,'II':2 ,'I':1 
		}

		n = str(n)
		zeros = len(n) - 1
		seperatedDigits = []
		romanChars = []

		for digit in n:
			zeroList=[]
			zeroList.append(digit)
			for zero in range(zeros):
				zeroList.append('0')
			seperated = "".join(str(x) for x in zeroList)
			seperated = int(seperated)
			seperatedDigits.append(seperated)
			zeros-=1

		for digit in seperatedDigits:
			for roman,value in romanValues.items():
				if digit == value:
					romanChars.append(roman)
					break
				elif digit-value > 0:
					multiChars = digit / value
					romanChars.append(roman)
					if multiChars.is_integer():
						multiChars = int(multiChars)
						for i in range(multiChars-1):
							romanChars.append(roman)
						break
					else:
						continue
		

		n_in_roman_alphabet = "".join(romanChars)
		print(n_in_roman_alphabet)
		return n_in_roman_alphabet

Solution.run("", 9999)