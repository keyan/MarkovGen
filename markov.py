# Takes as input any string of text and generates a sentence using 3rd order Markov Chains.
# 
# Author: Keyan Pishdadian 1/15/2015

from nltk import PunktWordTokenizer
from collections import defaultdict

class MarkovChain(object):
    def __init__(self, text, order):
        self.text = text
        
        #This variable can be changed to generate dictionaries of any n order chains.
        self.order = order
        self.chain_dictionary = self.make_markov_chain_dict()
    
    def make_markov_chain_dict(self):
        """
        Forms a dictionary in the form:
        key --> string
        value --> defaultdict
        
        Where the defaultdict holds the number of instances a word appears after a previous word.  
        i.e. {'the':[('man':2), ('boy':1), ('dog':2), ('world':8)]}
        """
        #TODO Performance issues?? With a book length input this would be a huge dictionary!?
        
        text = self.text
        
        #Create a list containing every word in the input text.
        word_tokenizer = PunktWordTokenizer()
        tokens_list = word_tokenizer.tokenize(text)
        
        #The main dictionary which contains the word keys
        markov_dictionary = {}
        
        #Goes through each word in the list, add to the main dictionary then add all future states to order n [default is 3].
        while tokens_list: 
            current_token = tokens_list.pop(0)

            #If the current token isn't already in the dictionary, then add it and have a defaultdict as it's value.
            #This allows us to increment the list of future states when their frequency increases.
            if current_token in markov_dictionary:
                self.update_dictionary(markov_dictionary, tokens_list, current_token)
            else:
                markov_dictionary[current_token] = defaultdict(int)
                self.update_dictionary(markov_dictionary, tokens_list, current_token)
    
        return markov_dictionary

    def update_dictionary(self, markov_dictionary, tokens, key):
        """
        Takes the markov chain dictionary being built and adds/increments the counters which track frequency of future states.
        """
        order = self.order
        
        try:
            for x in range(order):
                markov_dictionary[key][tokens[x]] += 1
        except IndexError:
            return
            
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
        

if __name__ == "__main__":
    chain_gen = MarkovChain("the fox brown fox jumped over the brown fox", 3)
    print chain_gen.chain_dictionary