import re
import html
import nltk
import contractions
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from cleantext import clean

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('omw-1.4')


def data_preprocessing(text: str, options: dict):
    """
    Limpa e preprocesa o texto de entrada en función dos parámetros indicados.

    Parameters
    ----------
    text : str
        Texto que será preprocesado.

    options : dict
        Conxunto de parámetros que indican os procesos a aplicar sobre o texto de entrada.

    Returns
    -------
    list
        Lista formada polo texto de entrada tokenizado e preprocesado.
    """

    preprocessed_text = []

    if len(text) > options['min_words']:

        if options['remove_htlm']:
            text = html.unescape(text)

        if options['remove_subreddits']:
            text = re.sub(r'(?<![\w/])/?[ru]/\w+/?(?![\w/+])', " ", text)  # u/user r/subreddit

        if options['remove_hashtags']:
            text = re.sub(r"#\S+", " ", text)

        if options['remove_contractions']:
            text = ' '.join([contractions.fix(word) for word in text.split()])

        if options['use_clean_text']:

            text = clean(text,
                         fix_unicode=True,
                         to_ascii=True,
                         lower=True,
                         no_line_breaks=True,
                         no_urls=True,
                         no_emails=True,
                         no_phone_numbers=True,
                         no_digits=True,
                         no_currency_symbols=True,
                         no_punct=True,
                         replace_with_punct=" ",
                         replace_with_url=" ",
                         replace_with_email=" ",
                         replace_with_phone_number=" ",
                         replace_with_digit=" ",
                         replace_with_currency_symbol=" ",
                         lang="en"
                         )

        # Elimina símbolos
        text = re.sub(r"[!#$%&\"'()*+,\-./:;<=>?@[\\\]^_`{|}~]", " ", text)

        # Elimina espacios extra
        text = re.sub(r'\s{2,}', " ", text)

        text = word_tokenize(text)

        if options['remove_stopwords']:
            stops = set(stopwords.words("english"))
            text = [word for word in text if word not in stops]

        if options['lemmatization']:
            wl = WordNetLemmatizer()
            text = [wl.lemmatize(word) for word in text]

        if options['stemming']:
            ps = PorterStemmer()
            text = [ps.stem(word) for word in text]

        preprocessed_text = text

    return preprocessed_text
