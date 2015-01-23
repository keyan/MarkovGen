# Takes as input any string of text and generates a sentence using
# 2nd order Markov Chains.
# Author: Keyan Pishdadian 1/15/2015

from nltk import PunktWordTokenizer
from collections import defaultdict
import numpy as np
import random


class MarkovChain(object):
    def __init__(self, text):
        """Order represents the chain length used."""
        self.text = text
        self.tokens_list = self.tokenizer()
        self.chain_dictionary = self.make_markov_chain_dict()
        self.weighted_chains = self.convert_to_tuple_list()

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

        for x in xrange(len(tokens_list)):
            try:
                current_token = (tokens_list[x] +
                                 " " +
                                 tokens_list[x + 1])
                next_token_index = x + 2
            # When there is only one token left, stop making the dictionary.
            except IndexError:
                break

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
        denominator = sum(value for key, value in current_word)
        weights = [float(value) / denominator for key, value in current_word]
        words = [key for key, value in current_word]

        return str(np.random.choice(words, size=1, replace=False, p=weights))

    def create_chain(self):
        """
        Uses word_select() to create chains of text of a specific length.
        """
        # Randomly select a starting phrase from the dictionary.
        current_state = ""
        while current_state is "":
            current_state = random.choice(self.weighted_chains.keys())
        final_string = ""
        for _ in range(10):
            final_string += " " + current_state
            possible_future_states = self.weighted_chains[current_state]
            print possible_future_states
            current_state = self.word_select(possible_future_states)

        print final_string


if __name__ == "__main__":
    chain_gen = MarkovChain("the young man has the young man went the young man has the young man could")

    print chain_gen.create_chain()
