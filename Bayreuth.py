# -*- coding: utf-8 -*-

import random
from Strategies import Strategy, RandomizingStrategy

###############################################################################
#
# Strategies from students from the University of Bayreuth
#
###############################################################################

class BayAnikaDoerge(RandomizingStrategy):
    """submitted by Anika Dörge
    - starts with cooperation
    - punishes defections with a 75% chance
    """
    def firstMove(self):
        return 1
    def nextMove(self, myMoves, opMoves):
        if opMoves[-1] == 1:  return 1
        else:
            if random.random() >= 0.25:
                return 0
            else:
                return 1
anikaDorge = BayAnikaDoerge()



class BayChristophSiemroth(Strategy):
    """submitted by Christoph Siemroth
    1. starts with cooperation
    2. plays TFT until last round, where it defects
    3. tries to break mutual defection series by a single (if ignored) cooperation offer
    4. tries to break mutual alternating series by a single (if ignored) cooperation offer
    """
    def firstMove(self):
        self.d = 0  # Anzahl der Defektionen des Gegners in Folge
        self.u = 0  # unforgivable, bei 1 hat Gegner das Kooperationsangebot nicht angenommen
        self.x = 0  # Hilfsvariable für Kooperationsangebot
        return 1

    def nextMove(self, myMoves, opMoves):
        n = len(myMoves) + 1
        if n == 1000:
            return 0
        else:
            if opMoves[-1] == 1:  # opponent cooperated in the last round
                self.d = 0;  self.x = 0
                return 1
            else:                 # opponent did not cooperate
                if opMoves[-1] == 0 and self.x == 1: # Erster Vergleich überflüssig
                    self.u = 1
                    return 0
                else:
                    if self.u == 0 and (self.d == 5 or \
                                        (len(myMoves) >= 5 and \
                                         myMoves[-5:] == [1,0,1,0,1])):
                        self.x = 1
                        self.d = 0
                        return 1      # Kooperationsangebot
                    else:
                        if opMoves[-1] == 0: # Vergleich überflüssig
                            self.d += 1
                            return 0
christophSiemroth = BayChristophSiemroth()


class BayBernhardHannenheim1(Strategy):
    """submitted by Bernhard Hannenheim
    1. plays TIT FOR TAT
    2. but every 7th round defects or cooperates with a ration of 2:1
    3.    in case it cooperates, it does so two times in sequence
    """
    def firstMove(self):
        return 1
    def nextMove(self, myMoves, opMoves):
        n = len(myMoves)+1
        if n % 21 == 0 or n % 21 == 1:
            return 1
        elif n % 7 == 0:
            return 0
        else:
            return opMoves[-1]
bernhardHannenheim1 = BayBernhardHannenheim1()


class BayBernhardHannenheim2(Strategy):
    """submitted by Bernhard Hannenheim
    play TIT FOR TAT, but:
    1. in case of 20 rounds of alternating cooperation and defection moves in
    sequence: cooperates one time instead of defecting
    2. in case of 50 rounds of mutual defection, cooperates twice
    3. switched to "ALWAYS D" if the opponent's defection rate was 40% or more
       after the first 100, but still checks
    """
    def firstMove(self):
        self.state = "TFT"
        return 1

    def nextMove(self, myMoves, opMoves):
        n = len(myMoves)

        if (n == 100 and (100-sum(opMoves)) >= 40):
            self.state = "ALL D"

        if self.state == "TFT":
            if n >= 20 and myMoves[-20:] == [0,1]*10:
                return 1
            elif n >= 50 and myMoves[-50:] == [0]*50 and opMoves[-50:] == [0]*50:
                self.state = "suspend TFT"
                return 1
            else:
                return opMoves[-1]
        elif self.state == "suspend TFT":
            self.state = "TFT"
            return 1
        elif self.state == "ALL D":
            if n >= 50 and myMoves[-50:] == [0]*50 and opMoves[-50:] == [0]*50:
                self.state = "suspend ALL D"
                return 1
            else:
                return 0
        elif self.state == "suspend ALL D":
            if myMoves[-2:] == [1, 1]:
                if opMoves[-1] == 1:
                    self.state = "TFT"
                    return 1
                else:
                    self.state = "ALL D"
                    return 0
            else:
                return 1
        else:
            assert False
bernhardHannenheim2 = BayBernhardHannenheim2()


class BayStefanFrisch(Strategy):
    """submitted by Stefan Frisch
    1. starts with a defection followed by a cooperation
    2. if opponent played cooperation in the first round and
       defection (punishment!) in the second round play TIT FOR TAT
    3. otherwise play ALWAYS D
    4. ALWAYS defect in the 1000th round.
    """
    def firstMove(self):
        return 0
    def nextMove(self, myMoves, opMoves):
        n = len(myMoves) + 1
        if n == 2: return 1
        elif n == 3:
            if opMoves == [1, 0]:
                self.state = "TFT"
                return 1
            else:
                self.state = "ALWAYS D"
                return 0
        elif n == 1000:
            return 0
        else:
            if self.state == "TFT":
                return opMoves[-1]
            elif self.state == "ALWAYS D":
                return 0
            else:
                assert False
stefanFrisch = BayStefanFrisch()


class BayJuliaLohmann(Strategy):
    """submitted by Julia Lohmann
    1. play TIT FOR TAT
    2. After 10 rounds: if opponent defected more than three times,
       play ALWAYS D
    """
    def firstMove(self):
        self.state = "TFT"
        return 1
    def nextMove(self, myMoves, opMoves):
        if len(myMoves) == 10 and sum(opMoves) < 7:
                self.state = "ALWAYS D"
        if self.state == "TFT":
            return opMoves[-1]
        elif self.state == "ALWAYS D":
            return 0
        else:
            assert False
juliaLohmann = BayJuliaLohmann()


class BayPhilippSchaechtele1(Strategy):
    """submitted by Philipp Schaechtele
    """
    def firstMove(self):
        return 1
    def nextMove(self, myMoves, opMoves):
        n = len(myMoves)+1
        if n <= 2:
            return 1
        else:
            if 0 in myMoves[-2:]:
                return 1
            else:
                return opMoves[-1]
philippSchaechtele1 = BayPhilippSchaechtele1()


class BayPhilippSchaechtele2(Strategy):
    """submitted by Philipp Schaechtele
    1. cooperates in the first two rounds
    2. defects if opponent has defected two times in sequence
    3. always cooperates after a defection
    """
    def firstMove(self):
        return 1
    def nextMove(self, myMoves, opMoves):
        n = len(myMoves)+1
        if n <= 2:
            return 1
        else:
            if myMoves[-1] == 0:
                return 1
            elif opMoves[-2:] == [0, 0]:
                return 0
            else:
                return 1
philippSchaechtele2 = BayPhilippSchaechtele2()


class BayAugmentedTFT(Strategy):
    """submitted by Christoph Siemroth
    - starts with cooperation and plays TFT
    - defects in last round
    - tries to break mutual defection series by a single (if ignored) cooperation offer
    - tries to break mutual alternating series by a single (if ignored) cooperation offer
    - attempts to identify random strategies and, once identified, to defect against them (v2)
    - grants change of status "unforgiving" if cooperation offer was made (v2)
    """
    def firstMove(self):
        self.u = 0  # unforgivable; if not 0, opponent did not accept cooperation offer
        self.x = 0  # if 1, cooperation offering in process
        self.patterns = set()
        return 1

    def nextMove(self, myMoves, opMoves):
        if len(opMoves) >= 4:
            pattern = (myMoves[-1], myMoves[-2], myMoves[-3], myMoves[-4],
                       opMoves[-1], opMoves[-2], opMoves[-3], opMoves[-4])
            self.patterns.add(pattern)
        if len(myMoves) == 999:
            return 0
        else:
            if len(self.patterns) > 20:
                return 0
            else:
                if opMoves[-1] == 1:  # opponent cooperated in the last round
                    self.x = 0;  self.u = 0
                    return 1
                else:                 # opponent did not cooperate
                    if self.x == 1:
                        self.u += 1 # forgives one rejection (for random strategies), might be exploitable
                        return 0
                    else:
                        if self.u < 2 and (opMoves[-5:] == [0,0,0,0,0] or \
                                                (len(myMoves) >= 5 and \
                                                 myMoves[-5:] == [1,0,1,0,1])): #worth improving: evade endgame effect
                            self.x = 1
                            self.d = 0
                            return 1
                        else:
                            return 0
bayAugmentedTFT = BayAugmentedTFT()


class BayJohannesWerner(Strategy):
    """submitted by Johannes Werner

    """
    def firstMove(self):
        self.anweisung = ""
        self.i = 0
        return 1            # Kooperiert in der 1. Runde

    def nextMove(self, myMoves, opMoves):
        # to-report strategie
        if opMoves[-1] == 1:        # lexteaktion = "ja"
            self.anweisung = "Frieden"
        else:
            if len(opMoves) >= 3 and (opMoves[-2] == 0 or opMoves[-3] == 0):
                self.anweisung = "Vergeltung"
            elif len(opMoves) > 7:
                if float(sum(opMoves)) / float(len(opMoves)) < 0.9:    # Mehr als 10 % Defektionen vom Gegner
                    self.anweisung = "Vergeltung"
                else:
                    self.anweisung = "Frieden"
            else:
                self.anweisung = "Frieden"

        # to verhalten
        if self.i != 0:
            if self.i > 2:
                self.i = self.i - 1
                return 0            # handlung = "defektion"
            else:
                self.i = self.i - 1
                return 1            # handlung = "kooperation"
        else:
            if self.anweisung == "Vergeltung":
                self.i = 3
                return 0            # handlung = "defektion"
            else:
                return 1            # handlung = "kooperation"

bayJohannesWerner = BayJohannesWerner()


class BayMartinSchymalla(Strategy):
    """submitted by Martin Schymalla
    """
    def firstMove(self):
        self.immer_c = 0
        self.immer_d = 0
        self.tft = 0
        return 1
    def nextMove(self, myMoves, opMoves):
        i = len(myMoves)
        n = 1000
        if i <= 2:  return 0
        elif i == 3:
            if opMoves == [1,1,1]:
                self.immer_c = 1
                return 0
            elif opMoves[-2:] == [1, 0]:
                if opMoves[0] == 1:
                    self.tft = 1
                return 1
            elif opMoves == [0,0,0]:
                self.immer_d = 1
                return 0
            elif opMoves == [1,0,0]:
                return 1
            else:
                return opMoves[-1]
        elif i >= n-2:
            if opMoves[:5] == [1,0,0,1,1]:
                return 1
            else:
                return 0
        else:
            if opMoves[-1] == 0:
                self.immer_c = 0
            elif opMoves[-1] == 1:
                self.immer_d = 0
            if self.immer_d == 1 or self.immer_c == 1:
                return 0
            elif i == 4 and self.tft == 1:
                return 1
            else:
                return opMoves[-1]
martinSchymalla = BayMartinSchymalla()


class BaySteffenHahn(RandomizingStrategy):
    """submitted by Steffen Hahn
    """
    def firstMove(self):
        self.coopFlag = False
        r = random.random()
        if r < 0.5: return 1    # first Move of TFT
        elif r < 0.7: return 0  # HAWK
        else:
            self.coopFlag = True # cooperate 2 times
            return 1
    def nextMove(self, myMoves, opMoves):
        if len(myMoves) >= 999: return 0
        elif self.coopFlag:
            self.coopFlag = False
            return 1
        else:
            r = random.random()
            if r < 0.5: return opMoves[-1] # TFT
            elif r < 0.7: return 0         # Hawk
            else:
                self.coopFlag = True       # cooperate 2 times
                return 1
steffenHahn = BaySteffenHahn()
