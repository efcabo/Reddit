from collections import Counter
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from yellowbrick.text import PosTagVisualizer

from .pos_tagging import *


def pos_visualization(texts):
    """

    Mostra unha gráfica para cada unha das categorías coas palabras máis frecuentes e o número de repeticións

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

    ignore = ['person', 'anything', 'anyone', 'something', 'someone', 'nobody', 'nothing', 'x200b', '*']

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

    for key in counts.keys():
        count = counts[key]

        most_common_counts= count.most_common(10)
        most_common_counts = [elem for elem in most_common_counts if elem[1] > 5]

        plt.bar([elem[0] for elem in most_common_counts], [elem[1] for elem in most_common_counts])

        plt.ylabel('Count')
        plt.xlabel('Words')
        plt.title(key)

        plt.show()

        wordcloud = WordCloud(background_color='white', width=1920, height=1080)

        wordcloud.generate_from_frequencies(dict(count))
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.show()
