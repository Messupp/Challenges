'''
Finds the singleton in a list of pairs.
'''
class Solution:

	def run(self, student_list):
		
		single_student_number = None
		for i in student_list:
			if student_list.count(i) % 2 == 1:
				single_student_number = i
					
		return single_student_number




Solution.run("", [5,3,2,2,3,5,4,6,9,6,4,12,8,9,12])
