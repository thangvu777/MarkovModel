from collections import defaultdict
import numpy as num
import random

class Markov:
    # Constructor (k represents Markov Model order, assume text has at least length of k)
    def __init__(self, sourceText: str, order: int) -> None:
        self.order = order
        self.tran = defaultdict(float)                    # has to be (float) because we will be dividing these values later
        self.alphabet = list(set(list(sourceText)))       # all text becomes apart of a list (duplicates letters are removed)
        self.seqCollection = defaultdict(int)
        length = len(sourceText)
        sourceText += sourceText[:order] # Add from [0:order] onto source text
        # Increment occurances of the source text
        for i in range(length):
            self.tran[sourceText[i:i+ order],sourceText[i+ order]] += 1.
            self.seqCollection[sourceText[i:i+ order]] += 1

    # return order
    def order(self) -> int:
        return self.order

    # number of occurences of seq in text
    # make sure length of seq is equal to order
    def freq(self, seq) -> int:
        assert len(seq) == self.order
        return self.seqCollection[seq]

    # number of times that character ch follows seq
    # make sure length of kgram is equal to order
    def freq2(self, seq, ch) -> float:
        assert len(seq) == self.order
        return self.tran[seq,ch]

    # chooses random character following given seq
    # make sure length of kgram is equal to order
    def rand(self, seq) -> chr:
        assert len(seq) == self.order
        # total represents the number of occurences of said character in alphabet
        total = sum(self.tran[seq, alphabet] for alphabet in self.alphabet)
        # print(total)
        # choose random char in alphabet with the statistical model
        ch = num.random.choice(self.alphabet, 1, p=num.array([self.tran[seq, alphabet] for alphabet in self.alphabet])/total)
        return ch

    # returns random seq from seqCollection
    def randSeq(self, seqCollection) -> str:
        col = list(seqCollection.keys())
        str = random.choice(col)
        return str

    # returns [0:order] of the sourceText
    def getFirstSeq(self, sourceText: str, order: int) -> str:
        return sourceText[:order]

    # Generate a string of length n 1 character at a time with respect to
    # the sequence (seq). seq must be of length order and must be a pre-existing
    # string in the source text. Only then, can we proceed building the Markov Chain
    def generateMarkovChain(self, seq, n) -> str:
        # length of seq must be equal to order
        assert len(seq) == self.order
        MarkovChain = ""
        i = 0
        while (i < n):
             # ch represents random character to be appended
             ch =  self.rand(seq)[0]    # Assume that n is at least (order).
             seq = seq[1:] + ch         # Update seq
             MarkovChain += ch          # Append ch to Markov Chain
             i += 1
        return MarkovChain

    # Visualize how data is read into the dictionary
    def printdict(self, dict) -> None:    # prints out items in seqCollection dictionary
        for items in (dict):
            print(items)