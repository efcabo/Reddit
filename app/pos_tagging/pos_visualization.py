from collections import Counter
from matplotlib import pyplot as plt
from yellowbrick.text import PosTagVisualizer

from .pos_tagging import *


def pos_visualization(texts):
    """

    Mostra unha gráfica para cada unha das categorías coas palabras máis frecuentes e o número de repeticións

    """

    tokens = []
    tags = {'Nouns': ['NN', 'NNS', 'NNP', 'NNPS'],
            'Possesives': ['PRP'],
            'Personal pronouns': ['PRP$'],
            'Adverbs': ['RB', 'RBR', 'RBS'],
            'Adjectives': ['JJ', 'JJR', 'JJS'],
            'Verbs': ['VBD', 'VBG', 'VBN', 'VBP', 'VBZ']}

    counts = {'Nouns': Counter(),
              'Possesives': Counter(),
              'Personal pronouns': Counter(),
              'Adverbs': Counter(),
              'Adjectives': Counter(),
              'Verbs': Counter()}

    ignore = ['person', 'anything', 'anyone', 'something', 'someone', 'nobody', 'nothing', 'x200b', '*']

    for text in texts:
        tokens_tag = pos_tagging(text)
        tokens.append(tokens_tag)

        for key in tags.keys():
            counts[key] += Counter(word.lower() for line in tokens_tag
                                   for word, tag in line
                                   if tag in tags[key] and word.lower() not in ignore)

    viz = PosTagVisualizer()
    viz.fit(tokens)
    viz.show()

    for key in counts.keys():
        count = counts[key].most_common(10)
        count = [elem for elem in count if elem[1] > 5]

        plt.bar([elem[0] for elem in count], [elem[1] for elem in count])

        plt.ylabel('Count')
        plt.xlabel('Words')
        plt.title(key)

        plt.show()



