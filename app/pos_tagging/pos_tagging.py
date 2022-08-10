import re
import nltk
import contractions
from nltk import pos_tag_sents
from nltk.tokenize import word_tokenize

nltk.download('averaged_perceptron_tagger')


def pos_tagging(text: str):
    """
    Etiqueta morfolóxicamente cada unha das palabras do texto.

    Parameters
    ----------
    text : str
        Texto a etiquetar.

    Returns
    -------
    list
        Lista de palabras etiquetadas.

    """

    # Sustituir as contraccións pola súa forma completa
    text_corrected = ' '.join([contractions.fix(word) for word in text.split()])
    text_corrected = text_corrected.replace(' i ', ' I ')

    # Dividir o texto en liñas
    lines = re.split('[.?!] ', text_corrected)

    # Tokenizar o texto
    tokenized_text = [word_tokenize(line) for line in lines if line != '']

    # Etiquetar o texto.
    tags = pos_tag_sents(tokenized_text)

    return tags






