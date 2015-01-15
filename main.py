# Takes as input any string of text and generates a sentence using 3rd order Markov Chains.
# 
# Author: Keyan Pishdadian 1/15/2015

from nltk import PunktWordTokenizer
from collections import defaultdict

class MarkovChain(object):
    def __init__(self, text, order):
        self.text = text
        self.order = order
        self.chain_dictionary = self.make_markovchain_dict()
    
    def make_markovchain_dict(self):
        """
        Forms a dictionary in the form:
        key --> string
        value --> defaultdict
        
        Where the defaultdict holds the number of instances a word appears after a previous word.  
        i.e. {'the':[('man':2), ('boy':1), ('dog':2), ('world':8)]}
        """
        #TODO Performance issues?? With a book length input this would be a huge dictionary!?
        
        #This variable can be changed to generate dictionaries of any n order chains.
        order = 3
        text = self.text
        
        #Create a list containing every word in the input text.
        word_tokenizer = PunktWordTokenizer()
        words = word_tokenizer.tokenize(text)
        
        #The main dictionary which contains the word keys
        markov_dictionary = {}
        
        #Goes through each word in the list, add to the main dictionary then add all future states to order n [default is 3].
        for word in words:
            if word in markov_dictionary:
                markov_dictionary = update_dictionary(markov_dictionary, word)
            else:
                markov_dictionary[word] = defaultdict(int)
                markov_dictionary = update_dictionary(markov_dictionary, word)
    
    def update_dictionary(current_dictionary, key):
        """
        Takes a key as an argument, finds the 
        """
        
        return updated_dictionary
        
    def word_select(self, current_state):
        """
        Selects one (? or more ?) words based on the distribution of n+3 states.
        """
        
        #TODO How to select word based on distribution? Bisect?
    
    def create_chain(self):
        """
        Uses word_select() to create chains of text of a specific length.
        """
        
        #For now, set the maxiumum text chain length to the maximum tweet length.
        characters_limit = 160
        