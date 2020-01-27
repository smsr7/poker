import random
class player:
    def __init__(self):
        self.capital = 0
        self.hand = []
        self.turn = False
        self.highcard = 0

    def _test(self):
        self.finalHand = []
        score = 0
        self.hand.sort(reverse=True)
        self.hand.append(-1)

        self._straight()
        self._duplicates()
        self._flush()
        
            def _duplicates(self):
                list = []
                score = 0
                dupe = False
                for i in range(len(self.hand)-1):
                    index = self.hand[i]
                    if (self.hand[i+1][0] == index[0]):
                        list.append(index)
                    #    self.hand.pop(i)
                        dupe = True
                    else:
                        if(dupe):
                            list.append(index)
                        #    self.hand.pop(i)
                        if(len(list) == 2):
                            #pair
                            self.finalHand.append([list,2,list[0]])
                        if(len(list) == 3):
                            #3 of a kind
                            self.finalHand.append([list,4,list[0]])
                        if(len(list) == 4):
                            self.finalHand.append([list,8,list[0]])
                        list = 0

            def _straight(self):
                list = []
                score = 0
                dupe = False
                color = 0
                for i in range(len(self.hand)-1):
                    index = self.hand[i]
                    if (self.hand[i+1][0]+1 == index[0]):
                        list.append(index)
                        dupe = True

                        if (self.hand[i+1][1] == index[1]):
                            color += 1

                    else:
                        if(dupe):
                            if (self.hand[i-1][1] == index[1]):
                                color += 1
                            list.append(index)
                            if(len(list) == 5):
                                if(color == 5):
                                    if(list[0] == 13):
                                        self.finalHand.append([list, 10, list[0]])
                                    else:
                                        self.finalHand.append([list, 9, list[0]])
                                else:
                                    self.finalHand.append([list, 4, list[0]])
                            dupe = False
                        list = []

            def _flush(self):
                l1 = self.hand
                l1.sort(key=lambda x: x[1], reverse=True)
                for i in range(len(l1)-1):
                    index = l1[i]
                    if (l1[i+1][1] == index[1]):
                        list.append(index)
                        dupe = True

                    else:
                        if(dupe):
                            list.append(index)
                            self.finalHand.append([list, 5, list[0]])
                            dupe = False
                        list = []




class game:
    def __init__(self, playerCount, player):
        self.bet = 0
        self.deck = self._deck()
        self.playerCount = playerCount
        self.players = []
        for i in range(self.playerCount):
            self.players.append(player())

    def _deck(self, decks = 1):
        self.cards = [] # everthing is shifted one ace is 13
        self.pot = 0
        for i in range(decks * 4):
            for ii in range(13):
                self.cards.append([ii, i]) #ii is value i is suit
        self._shuffle()
        return self.cards

    def _shuffle(self):
        cards = []
        for i in range(len(self.cards)):
            index = random.randint(0,len(self.cards)) #put array in random order
            cards.append(self.cards[index])
            self.cards.pop(index)

        self.cards = cards

    def _draw(self):
        card = self.cards[0] #take card from top of deck
        self.cards.pop(0)
        return card

#    def _bets(self):


    def _stage(self):
#        if self.stage == 0:
#            self.bets()
        if self.stage == 1:
            for i in range(2):
                for ii in self.players:
                    ii.hand.append(self._draw())
#            self._bets()

        if self.stage == 2:
            self._draw()
            cards = []
            for i in range(3):
                cards.append(self._draw())
            for i in self.players:
                for ii in cards:
                    i.hand.append(ii)

#            self._bets()
        if self.stage == 3 or self.stage == 4:
            self._draw()
            card = self._draw()
            for i in self.players:
                i.append(card)
#            self._bets()
            if self.stage == 4:
                self._test()


        def _test(self):
            score = []
            for i in self.players:
                score.append(i._test())
