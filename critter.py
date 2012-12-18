import random  


class critter(Object):

	def __init__(self, startingEnergy, startingSmell, smellRadius, location, hungryLimit, hornyLimit):
		self.energy = startingEnergy
		self.smellStrength = startingSmell
		self.smellRadius = smellRadius
		self.metabolism = 1
		self.location = location
		self.hungryLimit = hungryLimit		
		self.hornyLimit = hornyLimit
		self.hungry == true
 
	def decide(self, critter, fruit):		
		if self.hungry:			
			self.pickHighest(fruit)			
		else:
			self.pickHighest(critter)
		self.metabolize()

	def iterate(self, passed):		
		'''	'''
		if passed = critter:		
			self.mate(passed)
		if passed = fruit:
			self.eat(passed)
		else:
			pass	

	def amhorny(self):
		if self.hungry != true:
			if self.energy < self.hungryLimit:
				self.hungry == true
		if self.hungry:				
			if self.energy > self.hornyLimit:
				self.hungry == false
				

	def mate(self, critterList):
		self.amhorny()
		if self.hungry == false: 	
			smelly, smelling, hungry, horny = critter #this will be a list
			newEnergy = self.energy/2
			newSmelly = 0				
			if smelly > self.smellStrength:
				newSmelly = random.random((self.smellStrength-1), (smelly+1))
			else:
				newSmelly = random.random((smelly-1), (self.smellStrength+1))
			newSmelling = 0
			if smelling > self.smellRadius:
				newSmelling = random.random((self.smellRadius-1), (smelling+1))
			else:
				newSmelling = random.random((smelling-1), (self.smellRadius+1))
			newHungry = 0 
			if hungry > self.hornyLimit:
				newHorny = random.random((self.hornyLimit-1), (horny+1))
			else:
				newHorny = random.random((horny-1), (self.hornyLimit+1))
			newHorny = 0
			if horny > self.hornyLimit:
				newHorny = random.random((self.hornyLimit-1), (horny+1))
			else:
				newHorny = random.random((horny-1), (self.hornyLimit+1))
			return (self.energy/2, newSmelly, newSmelling, newHungry, newHorny)
			self.energy = self.energy/2
		else:
			self.energy -= self.metabolism
		
	def eat(self, fruit):
		self.energy += fruit.energy()
		self.amhorny()


	def pickHighest(self, choices):
		i = 0	
		j = 0			
		for number in choices:
			if number > i
				i = number
		#get the slot number for the value i
		return slotnumber

	def metabolize(self):
		self.energy -= self.metabolism
