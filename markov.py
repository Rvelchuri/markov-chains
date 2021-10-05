"""Generate Markov text from text files."""

from random import choice
from pprint import pprint


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    
    # your code goes here
    words = open(file_path).read()
    # print(words)
    return words


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    words = text_string.split()
    chains = {}
    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = (words[i+2])
        if key not in chains:
            chains[key]= []
        chains[key].append(value)
    # pprint(chains)

    return chains


def make_text(chains):
    """Return text from chains."""
    
    words = []
    starter_key = choice(list(chains.keys()))
    random_word = choice((chains[starter_key]))
    pprint(random_word)
    pprint(starter_key)
    # words = [starter_key[0],starter_key[1]]
    print(type(words))
    print(type(starter_key))
    
    while random_word is not  None:
        words.append(starter_key[0])
        words.append(starter_key[1])
        words.append(random_word)

        
    return ' '.join(words)
input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
