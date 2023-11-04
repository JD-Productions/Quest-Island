import math
import database

class Trading_Post:
	def __init__(self, user):
		self.db = database.Db(user)
		self.data = self.db.get_file()
	
	def main(self):
		print("Welcome To The Trading Post!", end=" ")
		while True:
			print("How can I help you?")
			print(f"You have {self.data['money']} dollars.")
			print("[0] Food\n[1] Weapons\n[2] Items\n[3] Leave")
			answer = int(input())
			if answer == 0:
				self.food()
			if answer == 1:
				self.weapons()
			if answer == 2:
				self.items()
			if answer == 3:
				print("Thanks for shopping by! Come back soon!")
				break
			self.db.save_file(self.data)
		
	def food(self):
		print("""TP-->Food:
			[0] Bread $5
			[1] Cake  $10""")
		answer = int(input())
		if answer == 0:
			sure = int(input("Buy Bread?\n[0] Yes\n[1] No"))
			if sure == 0:
				amount = int(input("How many loaves? (Number)  "))
				cost = amount * 5
				if self.data['money'] >= cost:
					self.db.add_item(f"bread x{amount}")
					self.data['money'] -= cost
					print(f"You bought {amount} loaves of bread for {self.data['money']} dollars.")
				else:
					print("You don't have enough money!")
			return
		if answer == 1:
			sure = int(input("Buy 1 Cake?\n[0] Yes\n[1] No"))
			if sure == 0:
				cost = 10
				if self.data['money'] >= cost:
					self.db.add_item(f"Cake x1")
					self.data['money'] -= cost
					print("You bought 1 cake for 10 dollars.")
				else:
					print("You don't have enough money!")
			return
	
	def weapons(self):
		print("Sorry! This feature is unavailiable on the demo version.")
		return
	
	def items(self):
		print("Sorry! This feature is unavailiable on the demo version.")
		return

if __name__=='__main__':
	tp = Trading_Post('Dalton')
	tp.main()
