from collections import Counter
from matplotlib import pyplot as plt
from yellowbrick.text import PosTagVisualizer

from .pos_tagging import *


def pos_visualization(texts: list):
    """
    Mostra unha gráfica para cada unha das categorías coas palabras máis frecuentes e o número de repeticións


    Parameters
    ----------
    texts : list
        Textos para os que se xerarán as gráficas.

    """

    tokens = []
    tags = {'Nouns': ['NN', 'NNS', 'NNP', 'NNPS'],
            'Personal pronouns': ['PRP'],
            'Possesives': ['PRP$'],
            'Adverbs': ['RB', 'RBR', 'RBS'],
            'Adjectives': ['JJ', 'JJR', 'JJS'],
            'Verbs': ['VBD', 'VBG', 'VBN', 'VBP', 'VBZ']}

    counts = {'Nouns': Counter(),
              'Personal pronouns': Counter(),
              'Possesives': Counter(),
              'Adverbs': Counter(),
              'Adjectives': Counter(),
              'Verbs': Counter()}

    ignore = ['person', 'people', 'thing', 'things', 'anything', 'anyone', 'something', 'someone','nobody', 'nothing',
              'other', 'more', 'much', 'many', 'few', 'first', 'last', 'x200b', '*']

    # Conteo do numero de palabras totait pot cada tipo ou etiqueta
    for text in texts:
        tokens_tag = pos_tagging(text)
        tokens.append(tokens_tag)

        for key in tags.keys():
            counts[key] += Counter(word.lower() for line in tokens_tag
                                   for word, tag in line
                                   if tag in tags[key] and word.lower() not in ignore)

    print("Numero de textos: " + str(len(texts)))

    viz = PosTagVisualizer()
    viz.fit(tokens)
    viz.show()

    # Conteo das 10 palabras máis frecuentes para cada categoría
    for key in counts.keys():
        count = counts[key]

        most_common_counts= count.most_common(10)
        most_common_counts = [elem for elem in most_common_counts if elem[1] > 5]

        plt.bar([elem[0] for elem in most_common_counts], [elem[1] for elem in most_common_counts])

        plt.ylabel('Count')
        plt.xlabel('Words')
        plt.title(key)

        plt.show()
