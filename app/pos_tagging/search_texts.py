from .pos_tagging import *


def search_texts(texts: list, search_word: str, search_tag: str):
    """
    Devolve unha lista cos textos nos que aparece a palabra indicada sempre que pertenza a categoría pasada
    como parámetro.

    Parameters
    ----------
    texts : list
        Textos sobre os que realizar a busca

    search_word : str
        Palabra a buscar.

    search_tag : str
        Categoría á que debe pertencer a palabra a buscar

    Returns
    -------
    list
        Lista cos textos que cumplen os parámetros indicados

    """

    toret = []

    tags = {'Nouns': ['NN', 'NNS', 'NNP', 'NNPS'],
            'Personal pronouns': ['PRP'],
            'Possesives': ['PRP$'],
            'Adverbs': ['RB', 'RBR', 'RBS'],
            'Adjectives': ['JJ', 'JJR', 'JJS'],
            'Verbs': ['VBD', 'VBG', 'VBN', 'VBP', 'VBZ']}

    for text in texts:
        tokens_tag = pos_tagging(text)

        if search_word.lower() in [word.lower() for line in tokens_tag
                                   for word, tag in line if tag in tags[search_tag]]:
            toret.append(text)

    return toret
