''' 

We need to start with a Deck class that generates a deck of cards in a random order.

'''
import random
import sys

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


	def checkCardValue(self)


class Player(object):

	def __init__(self, name, credits, luck):

		self.name = name;
		self.credits = credits;
		self.luck = luck;
		self.hand = Hand()

	pass

	def checkCards(self):
		print(self.hand.gethandList);	


	def makeBet(self, credits):
		return credits;

	def addCredits(self, addCredits):

		self.credits += addCredits

	def loseCredit(self, loseCredits):

		self.credits -= loseCredits




class Dealer(object):

	def __init__(self):

		self.hand = Hand()

	def dealerHas():

		self.hand.gethandList()

	pass

class Game(object):


		def __init__(self):

			pass

		def gameStart(self):

			gamePlayerName="jim" #input('Hey, welcome to The Nexus Casino! Please enter your name: ')
			gameCredits = 100 #input('Thanks ' + gamePlayerName, '! How many credits would you like to start with? >')
			gameLuck = 100#input('And finally, what would you like your luck to be? >')




			self.dealer = Dealer()
			self.player = Player(gamePlayerName, gameCredits, gameLuck)




			x = "play"

			while(x != "play"):

				x = "play"#nput("type 'play' to start playing, or q to quit. >")

				if(x == "q"):
					sys.exit()

			self.gameLoop1()

		def gameLoop1(self):
			while(True):

				self.gameDeck = Deck()

				self.gameDeck.generateDeck()

				print("You drew: ")
				self.generatePlayerCard()
				self.generatePlayerCard()
				print("Total value:\n")



				break
		def generatePlayerCard(self):

				card = self.gameDeck.exportCard()

					#hell yeah
				print(">- {} -< ".format(card.getAttribs()[1]))

				self.player.hand.addCardToHand(card)







newGame = Game()
newGame.gameStart()

