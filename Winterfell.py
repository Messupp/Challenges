'''
Predicts who would win in a GoT style battle. Input is the number of dragons and number of White Walkers, then the output is the
team that wins and after how many rounds

Input:
"Seven Kingdom Army",4,1

Expected Result:
White Walker Army|6

Input:
"Seven Kingdom Army",10,5

Expected Result:
Seven Kingdom Army|5

Input is:
Army name, how many dragons, how many white walkers

output is:
who will win, how many turns 
'''

class Solution:
	def run(self, first_strike_army_name, no_of_dragons, no_of_white_lords):

		class SevenKingdomArmy():
			class Dragon():
				def __init__(self):
					self.damage=600
					self.defence=600
				def take_damage(self, damage):
					self.defence -= damage
					return self.defence
				def restore_damage(self):
					if self.defence>= 0:
						self.defence=600
				
					
			class SevenInfantry():
				def __init__(self):
					self.damage=2
					self.defence=2

				def take_damage(self, damage):
					self.defence -= damage
					return self.defence
				
				def restore_damage(self):
					if self.defence>= 0:
						self.defence=2
			
					
		class WhiteWalkerArmy():
			class WhiteLord():
				def __init__(self):
					self.damage=50
					self.defence=100
				def take_damage(self, damage):
					self.defence -= damage
					return self.defence
				def restore_damage(self):
					if self.defence>= 0:
						self.defence=100
				
			class WhiteInfantry():
				def __init__(self):
					self.damage=1
					self.defence=3
				def take_damage(self, damage):
					self.defence -= damage
					return self.defence
				def restore_damage(self):
					if self.defence>= 0:
						self.defence=3

		def restoreHealth(sevenkingdom, whitewalker):
			for i in range(len(sevenkingdom)):
				sevenkingdom[i].restore_damage()
			for i in range(len(whitewalker)):
				whitewalker[i].restore_damage()
			return sevenkingdom, whitewalker

		def kingdomDamage(sevenkingdomDamage, whitewalker):
			try:
				
				unitDamage = sevenkingdomDamage[0]
				sevenkingdomDamage.pop(0)
				health = whitewalker[0].take_damage(unitDamage)
				if health <= 0:
					whitewalker.pop(0)
					if health < 0:

						sevenkingdomDamage.append(abs(health))
			except:
				battle = False

			return sevenkingdomDamage, whitewalker

		def walkerDamage(whitewalkerDamage, sevenkingdom):
			try:
				unitDamage = whitewalkerDamage[0]
				whitewalkerDamage.pop(0)
				health = sevenkingdom[0].take_damage(unitDamage)
				if health <= 0:
					sevenkingdom.pop(0)
					if health < 0:
						
						whitewalkerDamage.append(abs(health))
			except:
				battle = False

			return whitewalkerDamage, sevenkingdom

		def attack(sevenkingdom, whitewalker, battle, rounds):
			battle = True
			sevenkingdomDamage = []

			for i in sevenkingdom:
				sevenkingdomDamage.append(i.damage)

			while len(sevenkingdomDamage) != 0:
				sevenkingdomDamage, whitewalker = kingdomDamage(sevenkingdomDamage, whitewalker)
			rounds += 1
		


			######

			whiteWalkerDamage = []
			for i in whitewalker:
				whiteWalkerDamage.append(i.damage)

			if len(whitewalker) > 0:
				rounds += 1
			while len(whiteWalkerDamage) != 0:
				whiteWalkerDamage, sevenkingdom = walkerDamage(whiteWalkerDamage, sevenkingdom)


			#####


			sevenkingdom, whitewalker = restoreHealth(sevenkingdom, whitewalker)

			output = ''
			if len(sevenkingdom) == 0:
				battle = False
				output = 'White Walker Army'


			if len(whitewalker) == 0:
				output = 'Seven Kingdom Army'
				battle = False
			return sevenkingdom, whitewalker, battle,output, rounds
					

					



		KingdomList = []
		WalkerList = []

		for i in range(5000):
			KingdomList.append(SevenKingdomArmy.SevenInfantry())
		for i in range(10000):
			WalkerList.append(WhiteWalkerArmy.WhiteInfantry())
		for i in range(no_of_dragons):
			KingdomList.append(SevenKingdomArmy.Dragon())
		for i in range(no_of_white_lords):
			WalkerList.append(WhiteWalkerArmy.WhiteLord())

		output = 'none'
		battle = True
		rounds = 0
		while battle == True:
			battle = True
			
			KingdomList, WalkerList, battle, output, rounds = attack(KingdomList, WalkerList, battle, rounds)
			
		# White Walker Army|6
		a = ('{output}|{rounds}'.format(output=output, rounds=rounds))
		
		result = a
		print(result)
		
		return result







solutions = Solution()
solutions.run("Seven Kingdom Army", 4, 1)
