class Solution:

	def run(self, p):
		
		def vowelConsCounter(p):
			p = p.lower()
			vowelCounter = 0
			consCounter = 0
			for i in p:
				if i == "a" or i== "i" or i== "e" or i=="u" or i=="o":
					vowelCounter += 1
				elif i != " ":
					consCounter +=1
			return vowelCounter, consCounter

		
		def reversedFoo(p):
			p = p.split()
			p.reverse()
			p = " ".join(p)
			
			strList = []
			for i in p:
				if i == i.lower():
					strList.append(i.upper())
				elif i == i.upper():
					strList.append(i.lower())
			output = "".join(strList)
			return output


		def sepP(p):
			p = p.split()
			p = '-'.join(p)
			return p


		def pvVowel(p):
			alist = []
			vowels = ["a","e","i","o","u"]
			for i in p:
				alist.append(i)
			indexes = []
			for i in range(len(alist)):
				if alist[i].lower() in vowels:
					indexes.append(i)
			indexes.reverse()
			for i in indexes:
				alist.insert(i, "pv")
			output = "".join(alist)
			return output
					

		vowels, cons = vowelConsCounter(p)
		reversedP = reversedFoo(p)
		seperatedP = sepP(p)
		pvP = pvVowel(p)



		combined_queries = "{vowels} {cons}::{reversedP}::{seperatedP}::{pvP}".format(vowels=vowels,cons=cons,reversedP=reversedP,seperatedP=seperatedP,pvP=pvP)
		return combined_queries

Solution.run("", "ThIs is p")