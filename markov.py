# Takes as input any string of text and generates a sentence using
# 3rd order Markov Chains.
# Author: Keyan Pishdadian 1/15/2015

from nltk import PunktWordTokenizer
from collections import defaultdict
import numpy as np


class MarkovChain(object):
    def __init__(self, text):
        """Order represents the chain length used."""
        self.text = text
        self.tokens_list = self.tokenizer()
        self.chain_dictionary = self.make_markov_chain_dict()
        self.weighted_chains = self.calculate_weights()

    def make_markov_chain_dict(self):
        """
        Forms a dictionary in the form:
        key --> string
        value --> defaultdict

        Where the defaultdict holds the number of instances a word appears
        after a previous phrase.
        i.e. {'the man':[('went':2), ('is':10), ('will':2)]}
        """
        # TODO Performance issues?? With a book length input
        # this would be a huge dictionary!?

        tokens_list = self.tokens_list
        markov_dictionary = {}

        print tokens_list

        for x in xrange(len(tokens_list)):
            try:
                current_token = (tokens_list[x] +
                                 " " +
                                 tokens_list[x + 1])
                next_token_index = x + 2
            # When there is only one token left, stop making the dictionary.
            except IndexError:
                break

            print current_token
            # Has a defaultdict as its value, allows us to increment the list.
            if current_token in markov_dictionary:
                self.update_dictionary(markov_dictionary,
                                       tokens_list,
                                       current_token,
                                       next_token_index)
            else:
                markov_dictionary[current_token] = defaultdict(int)
                self.update_dictionary(markov_dictionary,
                                       tokens_list,
                                       current_token,
                                       next_token_index)

        return markov_dictionary

    def tokenizer(self):
        """
        Seperates input on whitespace, punctuation is included in word.
        """
        text = self.text

        # Create a list containing every word in the input text.
        word_tokenizer = PunktWordTokenizer()
        tokens_list = word_tokenizer.tokenize(text)

        return tokens_list

    def update_dictionary(self, markov_dictionary, tokens, key, x):
        """
        Takes the markov chain dictionary being built and adds or
        increments the counters which track frequency of future states.
        """
        try:
            markov_dictionary[key][tokens[x]] += 1
        except IndexError:
            return

    def convert_to_tuple_list(self):
        """
        Edits the markov chain dictionary to replace number of instances
        with a weight between 0 - 1. The value is also changed fromt
        a defaultdict to a list of tuples.
        """
        weighted_chains = {}
        # Turn the key: defaultdict pair into a key: list of tuples pair
        for key, value in self.chain_dictionary.items():
            weighted_chains[key] = value.items()

        return weighted_chains

    def word_select(self, current_word):
        """
        Selects one word in the key,value pair using a weighted random choice
        """
        pass

    def create_chain(self):
        """
        Uses word_select() to create chains of text of a specific length.
        """
        pass
        # For now, set the maxiumum text chain length to the maximum tweet
        # length.
        # characters_limit = 160


if __name__ == "__main__":
    chain_gen = MarkovChain("the young man has the young man went the young man has the young man could")
    # chain_gen.weighted_chains
    # chain_gen.chain_dictionary
