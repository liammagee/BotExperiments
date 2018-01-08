
# Adapted from https://gist.github.com/benrules2/4d869d71f21913da7b85bbb230a45e48


import random
import sys
import re
import numpy as np
from numpy.random import choice


def build_chain(text, chain={}, chain_counts={}):
    words = text.split(' ')
    index = 1
    for word in words[index:]:
        key = words[index - 1]
        if key in chain:
            if word in chain[key]:
                idx = chain[key].index(word)
                chain_counts[key][idx] = chain_counts[key][idx] + 1
            else:
                chain_counts[key] = np.append(chain_counts[key], 1)
                chain[key].append(word)
        else:
            chain[key] = [word]
            chain_counts[key] = np.array([1])
        index += 1
    for k in chain_counts:
        v = chain_counts[k]
        s = sum(v)
        chain_counts[k] = v / s
    return chain, chain_counts

def read_file(filename):
    with open(filename, "r") as file:
        contents = file.read()
    s = re.findall("\*\*\* START(.*)\*\*\* END", contents, re.DOTALL)[0].replace('\n', ' ').replace('\r', ' ').replace('--', ' ')
    s = re.sub(r"[;\.,]", "", s)
    return s



def write_file(filename, messages):
    with open(filename, "w") as file:
        for message in messages:
            file.write(message + '\n')


def generate_message(chain, chain_counts, count=10):
    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message.split(' ')) < count:
        word2 = choice(chain[word1], size=None, replace=True, p=chain_counts[word1])
        # word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2
    message += '!'

    return message

if __name__ == '__main__':
    message = read_file(sys.argv[1])
    chain, chain_counts = build_chain(message)
    message_count = 1
    messages = []
    if len(sys.argv) > 2:
        message_count = (int)(sys.argv[2])
    for i in np.arange(message_count):
        messages.append(generate_message(chain, chain_counts))
    print(messages)
    write_file('shandy.txt', messages)

