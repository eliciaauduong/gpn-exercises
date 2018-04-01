#made by Elicia Au Duong 01.April.2018

import random

cups = {'i': ['am', 'am', 'do', 'do', 'do', 'would', 'would', 'do', 'do', 'do', 'do', 'do', 'do', 'do', 'do', 'would', 'would', 'would', 'do'],
'am': ['sam', 'that'],
'sam': ['sam', 'i'],
'that': ['sam-i-am', 'sam-i-am', 'sam-i-am'],
'sam-i-am': ['that', 'i', 'do', 'i', 'would', 'would'],
'do': ['not', 'you', 'not', 'not', 'not', 'not', 'not', 'not', 'not', 'not', 'not', 'not', 'not'],
'not': ['like', 'like', 'like', 'like', 'like', 'like', 'like', 'like', 'like', 'like', 'like', 'like', 'like', 'in', 'with', 'in', 'with', 'eat', 'eat', 'eat', 'like'],
'like': ['that', 'green', 'them', 'green', 'them', 'them', 'them', 'green', 'them', 'them', 'them', 'them', 'them', 'them', 'them', 'green', 'them', 'them'],
'you': ['like', 'like', 'like', 'like', 'eat', 'eat'],
'green': ['eggs', 'eggs', 'eggs', 'eggs', 'eggs'],
'eggs': ['and', 'and', 'and', 'and', 'and'],
'and': ['ham', 'ham', 'ham', 'ham', 'ham'],
'ham': ['i', 'would', 'i', 'i', 'i'],
'them': ['sam-i-am', 'here', 'here', 'anywhere', 'sam-i-am', 'in', 'with', 'in', 'with', 'here', 'anywhere', 'sam-i-am', 'in', 'with', 'here', 'anywhere', 'sam-i-am'],
'would': ['you', 'not', 'not', 'you', 'you', 'you', 'you', 'not', 'not', 'not'],
'here': ['or', 'or', 'or', 'or'],
'or': ['there', 'there', 'there', 'there'],
'there': ['i', 'i', 'i', 'i'],
'anywhere': ['i', 'i', 'i'],
'in': ['a', 'a', 'a', 'a', 'a'],
'a': ['house', 'mouse', 'house', 'mouse', 'box', 'fox', 'box', 'fox', 'house', 'mouse'],
'house': ['would', 'i', 'not'],
'with': ['a', 'a', 'a', 'a', 'a'],
'mouse': ['i', 'i', 'i'],
'eat': ['them', 'them', 'them', 'them', 'green'],
'box': ['would', 'not'],
'fox': ['not', 'not']}

print("I am a markov chain generator")
current_word = input("What word do you want to start with? ")
print(current_word , end = " ")
correct = "no"
while correct == "no":
    if current_word in cups:
        for i in range(100):
            next_word_options = cups[current_word.lower()]
            next_word = random.choice(next_word_options)
            print(next_word , end = " ")
            current_word = next_word
        correct = "yes"
    else:
        print("Sorry, you can't use that as a starting word!")
        current_word = input("What word do you want to start with? ")

