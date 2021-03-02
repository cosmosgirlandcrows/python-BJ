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

	def addCardToHand(self, value):

		self.handList.append(value)

	def gethandList(self):

		return self.handList


class Player(object):

	pass

class Dealer(object):

	pass

myDeck = Deck()

myHand = Hand()

myDeck.generateDeck()

for i in range(0, len(myDeck.deckOfCards)):

	print(myDeck.deckOfCards[i].name + " " + myDeck.deckOfCards[i].suit)
	
print(len(myDeck.deckOfCards))
	

