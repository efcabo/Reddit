from collections import Counter
from .pos_tagging import *


def count_pronouns(text):
    """

    Conta o número de pronomes e posesivos totais e os que indican primeira persoa.
    En función da cantidade atopada, devolve True, se a maioría indican primeira persoa e False en caso contrario.
    No caso de que a cantidade de pronomes sexa inferior a 3 considérase que non é unha cantidade suficientemente
    representativa par a comparación polo que se devolve None.

    """
    tokens_tag = pos_tagging(text)

    words = ['i', 'we', 'me', 'us', 'mine', 'ours', 'myself', 'ourselves', 'my', 'our']
    # words = ['i', 'me', 'mine', 'myself', 'my']

    counts_total = Counter(tag for line in tokens_tag for word, tag in line if tag in ['PRP', 'PRP$'])
    counts_first_person = Counter(tag for line in tokens_tag for word, tag in line
                                  if tag in ['PRP', 'PRP$'] and word.lower() in words)

    total = 0
    first_person = 0

    # Personal pronoun
    if counts_total['PRP'] != 0:
        total += counts_total['PRP']
        first_person += counts_first_person['PRP']

    # Possesive pronoun
    if counts_total['PRP$'] != 0:
        total += counts_total['PRP$']
        first_person += counts_first_person['PRP$']

    if total < 3:
        return None

    elif first_person / total > 0.5:
        return True

    else:
        return False


def person_classification(data):
    """

    Clasifica os textos en dous grupos (primeira persoa e non primeira persoa en función do resultado da función
    "count_pronouns".
    En primeiro lugar comproba title, e se o resultado é None realiza a misma comprobación para body.
    No caso de que ao comprobar body tamén retorne None clasifícase o texto como non primeira persoa

    """
    first_person = []
    no_first_person = []

    for post in data:

        result = count_pronouns(post['title'])

        if result is None:
            result = count_pronouns(post['body'])

        if result:
            first_person.append(post)
        else:
            no_first_person.append(post)

    return first_person, no_first_person
