#made by Elicia Au Duong 01.April.2018

import random

source_text = """
Once upon a midnight dreary, while I pondered, weak and weary
Over many a quaint and curious volume of forgotten lore
    While I nodded, nearly napping suddenly there came a tapping
As of some one gently rapping rapping at my chamber door
Tis some visitor I muttered tapping at my chamber door
            Only this and nothing more

    Ah, distinctly I remember it was in the bleak December
And each separate dying ember wrought its ghost upon the floor
    Eagerly I wished the morrow vainly I had sought to borrow
    From my books surcease of sorrow sorrow for the lost Lenore
For the rare and radiant maiden whom the angels name Lenore
            Nameless here for evermore

    And the silken, sad, uncertain rustling of each purple curtain
Thrilled me filled me with fantastic terrors never felt before
    So that now, to still the beating of my heart I stood repeating
    Tis some visitor entreating entrance at my chamber door
Some late visitor entreating entrance at my chamber door
            This it is and nothing more
"""

cups = {}

split_text = source_text.split()
num_words = len(split_text)
for i in range(num_words -1):
    current_word = split_text[i]
    next_word = split_text[i + 1]
    if current_word not in cups:
        li = [next_word]
        cups[current_word] = li
    else:
        li.append(next_word)


print("I am a markov chain generator")
current_word = input("What word do you want to start with? ")
print(current_word , end = " ")
correct = "no"
while correct == "no":
    if current_word in cups:
        for i in range(100):
            next_word_options = cups[current_word]
            next_word = random.choice(next_word_options)
            print(next_word , end = " ")
            current_word = next_word
        correct = "yes"
    else:
        print("Sorry, you can't use that as a starting word!")
        current_word = input("What word do you want to start with? ")