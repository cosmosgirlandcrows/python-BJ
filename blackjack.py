''' 

We need to start with a Deck class that generates a deck of cards in a random order.

'''
import random


class Deck(object):

	#we need to somehow get the cards into the deck class in our deck generation method!


	def __init__(self):

		self.numCount = 0
		self.deckOfCards = []


	def generateDeck(self):

		values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
		names = ["One of", "Two of", "Three of", "Four of", "Five of", "Six of", "Seven of", "Nine of", "Ten of", "Jack of", "Queen of", "King of", "Ace of"]
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]


			#The bug is that if we go through three for-loops to distrivute the three attributes itll get stuck incrementing the value of a card while printing the same card over and over!
			#there should be a way to do this though, maybe a different order of for loops? 

			

		for x in range(0, len(suits)):

			for y in range(0, len(names)):

					newCard = Card(suits[x], names[y], values[y])
					self.deckOfCards.append(newCard)


		self.shuffleDeck()

		



	def shuffleDeck(self):

		random.shuffle(self.deckOfCards)

			


	def getnumCount(self):

		return self.numCount

	def incrementnumCount(self):

		self.numCount += 1


	def exportCard(self):


		returnCard = self.deckOfCards[self.getnumCount()]

		self.incrementnumCount()

		return returnCard;

	def generateDeckList(self):

		for i in range(0,52):

			self.deckList.append(i)

	def getDeckList(self):

		return self.deckOfCards



class Card(object):

	def __init__(self, suit, name, value):

		self.value = value
		self.name = name
		self.suit = suit

	def getAttribs(self):

		attributeList = [self.value, self.name + " " + self.suit]

		return attributeList


class Hand(object):

	def __init__(self):

		self.handList = []

	def addCardToHand(self, card):

		self.handList.append(card)

	def gethandList(self):

		return self.handList


class Player(object):

	def __init__(self, name, credits, luck):

		self.name = name;
		self.credits = credits;
		self.luck = luck;
		self.hand = Hand()

	pass

	def checkCards(self):
		print(self.hand.gethandList);	




class Dealer(object):

	def __init__(self):

		self.hand = Hand()

	def dealerHas():

	pass


def gamePlayLoop:

		gamePlayerName= input('Hey, welcome to The Nexus Casino! Please enter your name: ')
		gameCredits = input('Thanks ' + gamePlayerName, '! How many credits would you like to start with? >')
		gameLuck = input('And finally, what would you like your luck to be? >')


		dealer = Dealer()
		player = Player(gamePlayerName, gameCredits, gameLuck)

	while(true):

		break




myDeck = Deck()

myHand = Hand()

myDeck.generateDeck()

for i in range(0, len(myDeck.deckOfCards)):

	print(myDeck.deckOfCards[i].name + " " + myDeck.deckOfCards[i].suit)
	
print(len(myDeck.deckOfCards))
	

