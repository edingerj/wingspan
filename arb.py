

'''

Players have 4 options every turn:
1) Plant a tree
2) Gain nutrients: sun, water, fire, disturbance
3) Hug a tree
4) Draw tree cards

Bonus card ideas: Michigander, tree hugger, tree climber, pyrosilviculture enthusiast, fake tree lover, utility forester, tree trimmer
generalist, food type
'''

import random, csv, time
import turtle, math
import pandas as pd
'''
###################################################################################################################################
#https://www.geeksforgeeks.org/draw-tree-using-turtle-module-in-python/
turtle.color('deep pink')
style = ('Courier', 20, 'italic')
turtle.write('Welcome to Wingspan (tree edition)!', font=style, align='center')
turtle.hideturtle()

# Function to draw rectangle
def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
  
# Function to draw triangle    
def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()
  
# Set the background color
screen = turtle.Screen ( )
screen.bgcolor("skyblue")
  
# Creating turtle object
tip = turtle.Turtle()
tip.color ("black")
tip.shape ("turtle")
tip.speed (2)
  
# Tree base
tip.penup()
tip.goto(100, -130)
tip.pendown()
drawRectangle(tip, 20, 40, "brown")
  
# Tree top
tip.penup()
tip.goto(65, -90)
tip.pendown()
drawTriangle(tip, 90, "lightgreen")
tip.penup()
tip.goto(70, -45)
tip.pendown()
drawTriangle(tip, 80, "lightgreen")
tip.penup()
tip.goto(75, -5)
tip.pendown()
drawTriangle(tip, 70, "lightgreen")
turtle.write("WELCOME TO WINGSPAN (TREE EDITION)!", font=("Verdana", 15, "normal"))

###################################################################################################################################
'''
class BonusCard:
	def __init__(self, name, bonus, description):
		self.name = name
		self.bonus = bonus
		self.description = description

michigander = BonusCard('michigander', None, 'Gain 2 points for all trees found in Michigan.')
tree_climber = BonusCard('tree climber', 10, 'Gain 10 bonus points for having the tallest combined height of trees.')
utility_forester = BonusCard('utility forester', None, 'Gain 2 points for all trees that are commonly found under power lines. ')
tree_trimmer = BonusCard('tree trimmer', 10, 'Gain 10 bonus points for having the most trees that are a fire hazard. ')
#all_bonus_cards = [michigander, tree_climber, utility_forester, tree_trimmer]
all_bonus_cards = [michigander, tree_climber]
random.shuffle(all_bonus_cards)

height_list = []

class Player:
	def __init__(self, number=None, name=None): # make the computer another instance of Player
		self.number = number
		self.name = name
		self.nutrients = []
		self.tree_cards = []
		self.Conifer = []
		self.Deciduous = []
		self.Urban = []
		self.hugs = 0
		self.tree_points = 0
		self.combined_height = 0
		self.bonus_points = 0
		#self.scores = []

	def assign_bonus_cards(self):
		self.bonus = all_bonus_cards.pop() # player is given 1 bonus card randomly (need to implement choice of bonus cards)

class Tree:
	def __init__(self, habitat, scientific_name, common_name, points, height, sun, water, fire, disturbance, michigander):
		self.habitat = habitat
		self.scientific_name = scientific_name
		self.common_name = common_name
		self.points = points
		self.height = height
		self.nutrients = []
		if sun == 1:
			self.nutrients.append('sun')
		if water == 1:
			self.nutrients.append('water')
		if fire == 1:
			self.nutrients.append('fire')
		if disturbance == 1:
			self.nutrients.append('disturbance')
		self.hugs = 0
		if michigander == 1:
			self.michigander = 1
		else:
			self.michigander = 0

	def info(self):
		return self.scientific_name + ' is a ' + self.habitat + '.'

	#def plant_facts(self): # returns a list of everything to be added to database
		#return [self.family, self.genus_species, self.common_name, self.physiognomy, self.conservatism, self.wetness]



df = pd.read_csv("trees.csv")
trees = df.values.tolist()
tree_instances = []
for t in trees:
	tree_instances.append(Tree(*t))


def draw_random_card(hand): #hand is a list of a player's tree cards
	random.shuffle(tree_instances)
	random_card = tree_instances.pop()
	hand.append(random_card)

def draw_chosen_card(hand, choice):
	i = int(choice) - 1
	chosen_card = computer.tree_cards[i]
	computer.tree_cards.pop(i)  # remove it from display
	hand.append(chosen_card)  # add it to player's hand
	draw_random_card(computer.tree_cards) # refresh display
	input('You drew a ' + str(chosen_card.common_name) + "!")

def display_3_cards(player):
	for tree in player.tree_cards:
		print('- ' + tree.common_name + ' (' + str(tree.points) + ' pts, ' + str(tree.height) + ' ft, ' + tree.habitat + ')' + ' | ' + 'requires ' + str(tree.nutrients))


def assign_tree_cards(player):
	for i in range(3):
		draw_random_card(player.tree_cards)


def roll_dice():
	dice = 5*['sun'] + 2*['water'] + ['fire'] + ['disturbance']
	return random.choice(dice)

def gain_nutrient(player, times=1):
	time.sleep(0.2)
	print('***rolling dice***')
	for i in range(times + len(player.Conifer)): #gain 1 additional nutrient for every Conifer in arb
		roll = roll_dice()
		player.nutrients.append(roll)
		print('You rolled a ' + roll + '! Adding it to your pile of nutrients...')
		time.sleep(0.3)


def display_rows(player):
	c_row, d_row, u_row = [], [], []
	for card in player.Conifer:
		c_row.append(card.common_name)
	for card in player.Deciduous:
		d_row.append(card.common_name)
	for card in player.Urban:
		u_row.append(card.common_name)
	print('Conifer: ' + str(c_row))
	print('Deciduous: ' + str(d_row))
	print('Urban: ' + str(u_row))

def game_status(player):
	time.sleep(0.5)
	print(75*"-")
	print(player.name + '\'s Arboretum:\'')
	print(75*"_")
	display_rows(player)
	print(75*"_")
	print(player.name + ' has the following cards to play:')
	for tree in player.tree_cards:
		print('- ' + tree.common_name + ' (' + str(tree.points) + ' pts, ' + str(tree.height) + ' ft, ' + tree.habitat + ')' + ' | ' + 'requires ' + str(tree.nutrients))
	print(75*"_")
	print(player.name + ' has these nutrients:')
	print(player.nutrients)
	print(75*"_")
	print('Your bonus card is: ' + player.bonus.name)
	print(75*"-")

def start_game():
	global computer
	computer = Player()
	global player_1
	global player_2
	global num
	for i in range(3):  # give the computer display 3 cards to start
		draw_random_card(computer.tree_cards)
	#num = int(input('Welcome to Wingspan (tree edition)! Enter the number of players (2, 3, or 4): '))
	#global turns
	#turns = int(input('How many turns would you like to play? '))
	name_1 = input('Player 1, enter your name: ')
	player_1 = Player(1, name_1)
	player_1.assign_bonus_cards()
	name_2 = input('Player 2, enter your name: ')
	player_2 = Player(2, name_2)
	player_2.assign_bonus_cards()
	global all_players
	all_players = [player_1, player_2]
	if num > 2:
		global player_3
		name_3 = input('Player 3, enter your name: ')
		player_3 = Player(3, name_3)
		player_3.assign_bonus_cards()
		all_players.append(player_3)
		if num > 3:
			global player_4
			name_4 = input('Player 4, enter your name: ')
			player_4 = Player(4, name_4)
			player_4.assign_bonus_cards()
			all_players.append(player_4)
	assign_tree_cards(player_1)
	gain_nutrient(player_1, 3)
	assign_tree_cards(player_2)
	gain_nutrient(player_2, 3)
	if num > 2:
		assign_tree_cards(player_3)
		gain_nutrient(player_3, 3)
		if num > 3:
			assign_tree_cards(player_4)
			gain_nutrient(player_4, 3)
	time.sleep(1)
	print('\n Setting up the game board...')
	time.sleep(1)
	game_status(player_1)
	time.sleep(1)
	game_status(player_2)
	if num > 2:
		time.sleep(1)
		game_status(player_3)
		if num > 3:
			time.sleep(1)
			game_status(player_4)
	input('Are you ready to start? Enter any key to begin. ')

def plant_tree(player, card):
	if card.habitat == 'Conifer':
		player.Conifer.append(card)
	elif card.habitat == 'Deciduous':
		player.Deciduous.append(card)
	elif card.habitat == 'Urban':
		player.Urban.append(card)
	player.tree_cards.remove(card)
	print('Planting a ' + card.common_name + '...')
	player.combined_height += card.height
	print('Your combined height is:')
	print(player.combined_height)

def remove_nutrients(player, to_be_removed):
	for n in to_be_removed:
		player.nutrients.remove(n)

def play_a_card(player):
	choice = input('Select a tree card to play: ')
	# check for valid input
	if choice in [t.common_name for t in player.tree_cards]:
		to_be_removed = []
		for card in player.tree_cards:
			if card.common_name == choice:
				print('Checking if you have enough nutrients...')
				for nutrient in card.nutrients:
					if nutrient in player.nutrients:
						to_be_removed.append(nutrient)
					else:
						option = input("Sorry, you don't have enough nutrients to plant that tree. Enter '1' to select another tree card, or '2' to go back to the main menu. \n")
						while option != '1' and option != '2':
							option = input('Invalid input. Enter 1 or 2: ')
						if option == '2':
							print("Let's try this again.\n")
							global turns
							turns += 1
							take_a_turn(player)
						if option == '1':
							play_a_card(player)
							return
				remove_nutrients(player, to_be_removed)
				plant_tree(player, card)
	else:
		option = input("Invalid input. Enter '1' to try again, or '2' to go back to the main menu. \n")
		while option != '1' and option != '2':
			option = input('Invalid input. Enter 1 or 2: ')
		if option == '1':
			play_a_card(player)
		if option == '2':
			print("Let's try this again.\n")
			#global turns
			turns += 1
			take_a_turn(player)
			
				

def hug_tree(player):
	player.hugs += (len(player.Deciduous) + 1) # 1 additional hug for each Deciduous tree in arb
	print('You have hugged ' + str(player.hugs) + ' trees <3')


def switch_players(current_player): #changes turn between 2 players
	if num == 2:
		if current_player.number == 1:
			return player_2
		else:
			return player_1
	if num == 3:
		if current_player.number == 1:
			return player_2
		if current_player.number == 2:
			return player_3
		else:
			return player_1
	if num == 4:
		if current_player.number == 1:
			return player_2
		if current_player.number == 2:
			return player_3
		if current_player.number == 3:
			return player_4
		else:
			return player_1



def evaluate_bonus_cards(player):
	all_trees = player.Conifer + player.Deciduous + player.Urban
	if player.bonus.name == 'michigander':
		for tree in all_trees:
			if tree.michigander == 1:
				player.bonus_points += 2
	#if player.bonus.name == 'tree climber': # get 10 point bonus if you have the tallest combined height
	# anyone can get 10 bonus points for having highest combined height, like longest roads in Catan
	global height_list
	if max(height_list) > 0 and player.combined_height == max(height_list):
		player.bonus_points += 10

	return player.bonus_points

def get_total_score(player):
	# return a list [tree points, hugs, bonus points]
	#tree_points = 0

	# Add tree points
	all_trees = player.Conifer + player.Deciduous + player.Urban
	for tree in all_trees:
		player.tree_points += tree.points
		#player.combined_height += tree.height
	# Add bonus points


	#print('The combined height of your trees is ' + str(player.combined_height))

	player.bonus_points = evaluate_bonus_cards(player)

	return [player.tree_points, player.hugs, player.bonus_points]
	


def end_game():
	print('GAME OVER! Adding up points...')
	time.sleep(0.5)
	global height_list
	global all_players
	for ind in all_players:
		height_list.append(ind.combined_height)
	#print('height list:')
	#print(height_list)

	scores_1 = get_total_score(player_1)
	scores_2 = get_total_score(player_2)
	#print(scores_1)
	#print(scores_2)

	total_1 = sum(scores_1)
	total_2 = sum(scores_2)

	print(75*"-")
	time.sleep(0.5)
	print('Step 1: Add up all tree points.')
	print(player_1.name + ' has ' + str(player_1.tree_points) + ' tree points.')
	print(player_2.name + ' has ' + str(player_2.tree_points) + ' tree points.')
	input(75*"-")
	time.sleep(0.5)
	print('Step 2: Count the number of trees hugged.')
	print(player_1.name + ' has hugged ' + str(player_1.hugs) + ' trees.')
	print(player_2.name + ' has hugged ' + str(player_2.hugs) + ' trees.')
	input(75*"-")
	time.sleep(0.5)
	print('Step 3: Add up bonus points.')
	print(player_1.name + ', a ' + player_1.bonus.name + ', has earned ' + str(player_1.bonus_points) + ' bonus points.')
	print(player_2.name + ', a ' + player_2.bonus.name + ', has earned ' + str(player_2.bonus_points) + ' bonus points.')
	input(75*"-")
	time.sleep(0.5)
	print('Final Step: Take the sum of all points.')
	
	print(75*"-")
	time.sleep(0.5)
	input('And the winner is...')
	print(player_1.name + ': ' + str(total_1) + ' pts')
	print(player_2.name + ': ' + str(total_2) + ' pts')
	if total_1 > total_2:
		print(player_1.name + '! Congratulations!')
	else:
		print(player_2.name + '! Congratulations!')
	# add lines for players 3 and 4
	return


def take_a_turn(player):
	time.sleep(1)
	global turns
	global num
	print('Turns remaining: ' + str(round(turns/num)))
	turns -= 1
	print("\n It's " + player.name + "'s turn!")
	game_status(player)
	print('\n' + player.name + ',')
	move = input('Select from the following options. Enter 1, 2, 3, or 4: \n 1. Plant a tree \n 2. Gain nutrients \n 3. Hug a tree \n 4. Draw tree cards \n')
	if move == '1':  # Plant a tree
		play_a_card(player)
	if move == '2':  # Gain nutrients
		gain_nutrient(player)
	if move == '3':  # Hug a tree
		hug_tree(player)
	if move == '4':  # Draw tree cards
		for i in range((len(player.Urban) + 1)):
			print('Select from the following cards. Enter 1, 2, 3, or 4 for a random card: ')
			display_3_cards(computer)
			choice = input()
			while choice != '1' and choice != '2' and choice != '3' and choice != '4':
				choice = input('Invalid input. Enter 1, 2, 3, or 4 for a random card: ')
			if choice == '4': # random card from deck
				draw_random_card(player.tree_cards)
				print('Drawing random card from deck...')
				input('You drew a ' + str(player.tree_cards[-1].common_name) + "!")
			else: # 1, 2, or 3 from display
				draw_chosen_card(player.tree_cards, choice)
	game_status(player)
	input('Enter "z" to end your turn. ')
	if turns > 0:
		take_a_turn(switch_players(player))
	else: end_game()


num = int(input('Welcome to Wingspan (tree edition)! Enter the number of players (2, 3, or 4): '))
turns = num * int(input('How many turns would you like to play? '))

start_game()

take_a_turn(player_1)




