# Remember it goes
# 2 : TOP
# 1: MIDDLE
# 0: BOTTOM

# Importing necessary libraries
import math
import random

# Creating a Card class to make it easier to mark our card
class Card:
    # Constructor
    def __init__(self, card_number, marked):
        self.card_number = card_number
        self.marked = marked

    # Convert card number to ternary and returns the output as a list data type
    def toTernary(self, chosenNumber):
        # Prevent mutating original card number
        number = chosenNumber
        ternary_sequence = []
        while not math.floor(number) == 0:
            remainder = number % 3
            ternary_sequence.append(remainder)
            number = math.floor(number / 3)
        
        sequence_length = len(ternary_sequence)
        if not len(ternary_sequence) == 3:
            for i in range(0, 3 - sequence_length):
                ternary_sequence.append(0)

        return ternary_sequence
    
    # Prints the number of our card
    def printCard(self):
        print(self.card_number)

    # Prints out card marker
    def printMarker(self):
        print(self.marked)

# Class Deck
class Deck:
    # Constructor
    def __init__(self, deck):
        self.deck = deck
        self.pile0 = []
        self.pile1 = []
        self.pile2 = []
    
    # Shuffles the given cards 
    def shuffleDeck(self):
        # Creating a list of a random sequence of indices
        shuffledSequence = []
        while not len(shuffledSequence) == 27:
            randomIndex = random.randint(0, 26)
            if randomIndex not in shuffledSequence:
                shuffledSequence.append(randomIndex)
        shuffledDeck = []
        for i in shuffledSequence:
            shuffledDeck.append(self.deck[i])
        self.deck = shuffledDeck

    # Deal out three piles
    def createPiles(self):
        # Pile 0 Indicies: 0, 3, 6, ... , 24
        # Pile 1 Indicies: 1, 4, 7, ... , 25
        # Pile 2 Indicies: 2, 5, 8, ... , 26
        self.pile0 = []
        self.pile1 = []
        self.pile2 = []

        for i in range(0, 25, 3):
            self.pile0.append(self.deck[i])
        for j in range(1, 26, 3):
            self.pile1.append(self.deck[j])
        for k in range(2, 27, 3):
            self.pile2.append(self.deck[k])

    # Form the deck with the marked deck in the appropriate position
    def formDeck(self, deckWithCard, digit):
        newDeck = []
        deckWithoutCard1 = []
        deckWithoutCard2 = []

        # Figuring out which deck is uhm not the pile with the marked card?
        notDeckWithCard = []
        for i in range(0, 3):
            pile = getattr(self, "pile" + str(i))
            if not pile == deckWithCard:
                notDeckWithCard.append(pile)
        deckWithoutCard1 = notDeckWithCard[0]
        deckWithoutCard2 = notDeckWithCard[1]

        if digit == 0:
            newDeck.extend(deckWithCard)
            newDeck.extend(deckWithoutCard1)
            newDeck.extend(deckWithoutCard2)
        if digit == 1:
            newDeck.extend(deckWithoutCard1)
            newDeck.extend(deckWithCard)
            newDeck.extend(deckWithoutCard2)
        if digit == 2:
            newDeck.extend(deckWithoutCard1)
            newDeck.extend(deckWithoutCard2)
            newDeck.extend(deckWithCard)
        self.deck = newDeck

    # Find the pile that has the marked card
    def findMarker(self):
        pileWithMarker = self.pile0
        for i in range(0, 3):
            pile = getattr(self, "pile" + str(i))
            for card in pile:
                if card.marked == True:
                    pileWithMarker = pile
                    break
        return pileWithMarker

    # Print out deck
    def printDeck(self):
        for i in self.deck:
            i.printCard()
    
    # Print out piles
    def printPiles(self):
        print("PILE 0: ")
        for i in self.pile0:
            i.printCard()
        print("PILE 1: ")
        for j in self.pile1:
            j.printCard()
        print("PILE 2: ")
        for k in self.pile2:
            k.printCard()
        
# Returns the given list but in reverse order
def reverseList(list):
    reverseList = []
    for i in range(0, len(list)):
        reverseList.insert(0, list[i])
    return reverseList

# Main entry function
def main():
    # Flooding our cards
    cards = []
    for i in range(1, 28):
        cards.append(Card(i, False))

    # Randomly marking our card
    marker = 9
    markedCard = cards[marker]
    markedCard.marked = True
    
    # Getting ternary sequence
    chosen_number = 9
    ternary_sequence = markedCard.toTernary(chosen_number - 1)

    myCards = Deck(cards)
    myCards.shuffleDeck()

    # Iteration
    for i in ternary_sequence:
        myCards.createPiles()
        firstMarkedDeck = myCards.findMarker()
        myCards.formDeck(firstMarkedDeck, i)
    
    print(myCards.printDeck())

    return 0
    
main()
