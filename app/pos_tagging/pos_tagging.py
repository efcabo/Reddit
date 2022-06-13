import re
import nltk
import contractions
from nltk import pos_tag_sents
from nltk.tokenize import word_tokenize

nltk.download('averaged_perceptron_tagger')


def pos_tagging(text):
    """

    Etiqueta morfolóxicamente cada unha das palabras do texto

    """
    text_corrected = ' '.join([contractions.fix(word) for word in text.split()])
    text_corrected = text_corrected.replace(' i ', ' I ')

    lines = re.split('[.?!] ', text_corrected)

    tokenized_text = [word_tokenize(line) for line in lines if line != '']

    return pos_tag_sents(tokenized_text)






