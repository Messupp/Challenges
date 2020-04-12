class Solution:

	def run(self, a):
		
		maxSum = 0  # or: float('-inf')
		tempSum = 0
		for x in a:
			tempSum = max(0, tempSum + x)
			maxSum = max(maxSum, tempSum)

		print(maxSum)
		return maxSum




Solution.run("", [7, -1, 3, 6])