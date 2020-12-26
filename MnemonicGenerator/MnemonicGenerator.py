#!/usr/bin/python3

import os

from sys import argv
from random import choice
from string import ascii_uppercase
from itertools import permutations
from rich.console import Console
from rich.markdown import Markdown
from randomsentence.sentence_maker import SentenceMaker
from randomsentence.sentence_tools import SentenceTools

if len(argv) == 1:
    print("Provide an output file")
    exit()

console = Console()
banner = """
# Input
## Rules
* You can input multiple times
* Input a word of related things
* Input two word with spaces for association
* Input nothing to exit
## Example:
### Example 1
```python
> telocentric
> metacentric
...
```
### Example 2
```python
> amino acid:protein
> fatty acid:lipid
...
```
"""

console.print(Markdown(banner))
del console
inputs = 0

def init() -> dict:
    words = [line.rstrip('\n') for line in open('/root/MachineYadav/My-Scripts/MnemonicGenerator/words')]
    words_dict = {letter: [] for letter in ascii_uppercase}
    for word in words:
        beginning = word[0].upper()
        words_dict[beginning].append(word)
    return words_dict

def fill_mnemonic():
    global mnemonic_initial_list
    global inputs
    while True:
        initial = ""
        word = input("> ")
        inputs += 1
        if not word:
            break
        word_list = word.split(':') if ':' in word else None
        if word_list:
            for word in word_list:
                initial += word[0].upper()
        else:
            initial = word[0].upper()
        mnemonic_initial_list.append(initial)

def return_word(char: str) -> str:
    if len(char) > 1:
        randword = words_dict[char[0]]
    else:
        randword = words_dict[char]
    counter = 0
    while counter < 50:
        if choice(randword).startswith(char):
            return choice(randword)
        counter += 1
    return choice(randword)

def sentence_from_initials(initial_tuple):
    words_list = [return_word(letter) for letter in initial_tuple]
    tagged_sentence = sentence_maker.from_keyword_list(words_list)
    return sentence_tool.detokenize_tagged(tagged_sentence)

mnemonic_initial_list = []
fill_mnemonic()
output = argv[-1]
words_dict = init()
sentence_maker = SentenceMaker()
sentence_tool = SentenceTools()
permutation_generator = permutations(mnemonic_initial_list)
if inputs < 5:
    sentences = (sentence_from_initials(f) for f in permutation_generator)
else:
    sentences = []
    inputs = int(inputs ** 2.5)
    for f in permutation_generator:
        sentences.append(sentence_from_initials(f))
        inputs = inputs - 1
        if inputs < 5:
            break

with open(output + '.permutation', "w+") as f:
    temp_generator = permutations(mnemonic_initial_list)
    for p in temp_generator:
        f.write("".join(p) + '\n')

with open(output + '.sentence', "w+") as f:
    for sentence in sentences:
        print(sentence)
        f.write(sentence.rstrip('\n') + '\n')

