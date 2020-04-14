
'''
4,4,[3,2,7,10],[2,7,15,19]
'''

class Solution:

	def run(self, n, m, a, b):
		#
		# Write your code below; return type and arguments should be according to the problem's requirements
		#
		outputList = []
		for number in a:
			if number in b:
				outputList.append(number)

		
		longest_common_subseq = ",".join(str(x) for x in outputList)
		print(longest_common_subseq)
		return longest_common_subseq


Solution.run("", 3,2,[1,4,5],[1,5])