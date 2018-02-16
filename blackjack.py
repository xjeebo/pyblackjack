import random # to use the random number generator
import os	# to use the system clear function
os.system("clear")
a = 2
my_dict = {"K":10, "Q":10, "J":10, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "A":11} # assigning their value in black jack
values = ['1','2','3','4','4','5','6','7','8','9','10','J','Q','K','A',] 	# your typical deck of cards
question = ''				 # user input determines this value
on = 1 					# This variable will activate or end the while loop. It is initially set to 1 to activate the loop
class player_init(object):                     # initialize a player with different methods such as draw 1 card..and to display their hand 
	Ace = False			# variable to deal with an Ace draw, which can be a value of 1 or 11
	num = 0
	def __init__(self,num,char):     # when a player is initiated they will obtain a card.. this value is generated by a random number generator
		if char == 'A': 	 # the card value is added to a list and added up 
			self.Ace = True  # if an ace is drawn this flag is set to True... this is give ace two different values...1 or 11
		self.num = num		 # the player will be given the option to draw another card...so if they have an Ace in there hand, but 
		self.cards = []		 # end up going over 21..the Ace will become a value of 1
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

		for i in self.symbol:				# display the card drawn..the else is for values over 10 to keep the display a fit
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
card = values[random.randint(1,14)]       # the card is a random number generated
dealer = player_init(my_dict[card],card)  # the number generated is then compared to the dictionary value to utilize the print function
dealer.printf()				  # the card number and its symbol are utilized


card = values[random.randint(1,14)]
player = player_init(my_dict[card],card)

card = values[random.randint(1,14)]
player.draw1(my_dict[card],card)

print("Player:")
player.printf()

if player.num == 21:          # if the players hand total is 21 then print that they have won
	print("You win!!!")
	on = 0                # disable the while loop 
elif player.num < 21:         # allow the user to draw another card or not
	question = input("Hit or stand?(h,s): ")  # if they pick to stand then the dealer will continue to draw until his hand is atleast a sum of  15
elif player.num > 21:
	player.num = player.num - 10
	player.Ace = False


while on == 1: # loop forever until break

	if question == 's' or question == 'S':

		os.system("clear")
		if dealer.num < 16:  # dealer will keep drawing until he has a hand greater than 15
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
