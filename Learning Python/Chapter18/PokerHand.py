"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck, Card


class PokerHand(Hand):
    """Represents a poker hand.
    Attributes:
      label: 0-8
    """

    label_names = ['Nothing', 'Pair', 'Two Pair', 'Three of a Kind',  'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush']

    def classify(self):
        if self.has_straight_flush():
            self.lable = PokerHand.label_names[8]
        elif self.has_four():
            self.lable = PokerHand.label_names[7]
        elif self.has_full_house():
            self.lable = PokerHand.label_names[6]
        elif self.has_flush():
            self.lable = PokerHand.label_names[5]
        elif self.has_straight():
            self.lable = PokerHand.label_names[4]
        elif self.has_three():
            self.lable = PokerHand.label_names[3]
        elif self.has_two_pair():
            self. lable = PokerHand.label_names[2]
        elif self.has_pair():
            self.lable = PokerHand.label_names[1]
        else:
            self.lable = PokerHand.label_names[0]

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def rank_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in atrribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val == 2:
                return True
        return False

    def has_three(self):
        """Returns True if the hand has three of a kind, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val == 3:
                return True
        return False

    def has_four(self):
        """Returns True if the hand has three of a kind, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val == 4:
                return True
        return False

    def has_two_pair(self):
        """Returns True if the hand has three of a kind, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        pairCounter = 0
        for val in self.ranks.values():
            if val == 2:
                pairCounter += 1
                if pairCounter == 2:
                    return True
        return False
    
    def has_full_house(self):
        """Returns True if the hand has three of a kind, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        return self.has_pair() and self.has_three()
    
    def has_straight(self):
        """Return True if the hand has a striahgt, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        cardList = []
        for card in self.cards:
            cardList.append(card.rank)
        cardList.sort()
        listIndex = 0
        sequenceCounter = 0
        while listIndex < len(cardList)-1:
            if cardList[listIndex] + 1 == cardList[listIndex+1]:
                sequenceCounter +=1
            if cardList[listIndex] == 13 or cardList[listIndex+1] == 13:
                for item in cardList:
                    if item == 1:
                        sequenceCounter +=1
            listIndex += 1
        if sequenceCounter == 4 : return True
        return False

    def has_straight_flush(self):
        """Return True if the hand has a striahgt, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        cardList = []
        for card in self.cards:
            cardList.append((card.rank, card.suit))
        cardList.sort()
        listIndex = 0
        sequenceCounter = 0
        while listIndex < len(cardList)-1:
            if cardList[listIndex][0] + 1 == cardList[listIndex+1][0] and cardList[listIndex][1] == cardList[listIndex+1][1]:
                sequenceCounter +=1
            if cardList[listIndex][0] == 13:
                for item in cardList:
                    if item[0] == 1 and item[1] == cardList[listIndex][1]:
                        sequenceCounter +=1
            if cardList[listIndex+1][0] == 13:
                for item in cardList:
                    if item[0] == 1 and item[1] == cardList[listIndex+1][1]:
                        sequenceCounter +=1
            listIndex += 1
        if sequenceCounter == 4 : return True
        return False

def createShuffledDeck():
    deck = Deck()
    deck.shuffle()
    return deck

def createHandsFromDeck(deck, numberHands, numberCards):
    hands =[]
    for i in range(numberHands):
        hand = PokerHand()
        deck.move_cards(hand, numberCards)
        hand.sort()
        hands.append(hand)
    return hands

def calculate_probabilities(numberIterations, numberHands, numberCards):
    handHistory = {}
    for i in range(numberIterations):
        deck = createShuffledDeck()
        hands = createHandsFromDeck(deck, numberHands, numberCards)
        for hand in hands:
            hand.classify()
            handHistory[hand.lable] = handHistory.get(hand.lable, 0) + 1
    for key, value in handHistory.items():
        handHistory[key] = round(value/(numberIterations*numberHands)*100,4)
    return handHistory

if __name__ == '__main__':
    probabilities = calculate_probabilities(100000, 5, 7)
    checkSum = 0
    for key, value in probabilities.items():
        checkSum += value
    print(probabilities)
    print(checkSum)