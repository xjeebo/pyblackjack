import random
import os
os.system("clear")
a = 2
my_dict = {"K":10, "Q":10, "J":10, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "A":11}
values = ['1','2','3','4','4','5','6','7','8','9','10','J','Q','K','A',]
question = ''
on = 1
class player_init(object):
	Ace = False
	num = 0
	def __init__(self,num,char):
		if char == 'A':
			self.Ace = True
		self.num = num
		self.cards = []
		self.symbol = []
		self.symbol.append(char)
		self.cards.append(num)

	def draw1(self,num,char):
		self.num += num
		if char == 'A':
			self.Ace = True

		self.symbol.append(char)
		self.cards.append(num)
		pass

	def printf(self):

		for i in self.symbol:
			if i != "10":
				print("----------")
				print("|%s       |" %(i))
				print("|        |")
				print("|        |")
				print("|        |")
				print("|        |")
				print("|       %s|" %(i))
				print("----------")		
			else:
				print("----------")
				print("|%s      |" %(i))
				print("|        |")
				print("|        |")
				print("|        |")
				print("|        |")
				print("|      %s|" %(i))
				print("----------")
		print("\nTotal: %s" %(self.num))
		pass		


print("Dealer:")
card = values[random.randint(1,14)]
dealer = player_init(my_dict[card],card)
dealer.printf()


card = values[random.randint(1,14)]
player = player_init(my_dict[card],card)

card = values[random.randint(1,14)]
player.draw1(my_dict[card],card)

print("Player:")
player.printf()

if player.num == 21:
	print("You win!!!")
	on = 0
elif player.num < 21:
	question = input("Hit or stand?(h,s): ")
elif player.num > 21:
	player.num = player.num - 10
	player.Ace = False


while on == 1:

	if question == 's' or question == 'S':

		os.system("clear")
		if dealer.num < 16:
			card = values[random.randint(1,14)]
			dealer.draw1(my_dict[card],card)
			dealer.printf()
		if dealer.num > 21 and dealer.Ace == True:
			dealer.num = dealer.num - 10
			dealer.Ace = False		
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nDealer:")
		dealer.printf()
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nPlayer:")
		player.printf()	

	elif question == 'H' or question == 'h':

		os.system("clear")
		card = values[random.randint(1,14)]
		player.draw1(my_dict[card],card)
		if player.num > 21 and player.Ace == True:
			player.num = player.num - 10
			player.Ace = False
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nDealer:")
		dealer.printf()
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nPlayer:")
		player.printf()
		if player.num == 21:
			print("You win!!!")
			break
		elif player.num < 21:
			question = input("Hit or stand?(h,s): ")			

	elif question != 's' or question != 's' or question != 'h' or question != 'H':
		question = input("Invalid input - please try again\nHit or stand?(h,s): ")	



	if dealer.num > player.num and question == 's' and dealer.num <= 21:
		print("Dealer Wins")
		break
	elif dealer.num < player.num and question == 's' and dealer.num > 16:
		print("You Win!")
		break

	if dealer.num == 21 and player.num == 21:
		print("Push")
		break
	elif player.num == 21:
		print("You win!!!")
		break
	elif dealer.num == 21:
		print("Dealer Wins")
		break
	elif player.num > 21:
		print("You bust!!!!")
		break
	elif dealer.num > 21:
		print("Dealer bust!! You win!!!")
		break	