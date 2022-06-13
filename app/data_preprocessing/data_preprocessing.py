import re
import html
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from cleantext import clean
import contractions

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')


#
def data_preprocessing(text: str, min_words=10, remove_htlm=True, remove_subreddits=True, remove_hashtags=True,
                       remove_contractions=True, unicode=True, to_lower=True, line_breaks=True, remove_digits=True,
                       remove_punct=True, remove_url=True, remove_email=True, remove_phone=True, remove_currency=True,
                       remove_stopwords=True, stemming=True, lematization=False):
    """
    Limpa e procesa o texto de entrada en función dos parámetros indicados.
    """

    preprocessed_text = []

    if len(text) > min_words:

        if remove_htlm:
            text = html.unescape(text)

        if remove_subreddits:
            text = re.sub(r'(?<![\w/])/?[ru]/\w+/?(?![\w/+])', " ", text)  # u/user r/subreddit

        if remove_hashtags:
            text = re.sub(r"#\S+", " ", text)

        if remove_contractions:
            text = ' '.join([contractions.fix(word) for word in text.split()])

        text = clean(text,
                     fix_unicode=unicode,  # fix various unicode errors
                     to_ascii=unicode,  # transliterate to closest ASCII representation
                     lower=to_lower,  # lowercase text
                     no_line_breaks=line_breaks,  # fully strip line breaks as opposed to only normalizing them
                     no_urls=remove_url,  # replace all URLs with a special token
                     no_emails=remove_email,  # replace all email addresses with a special token
                     no_phone_numbers=remove_phone,  # replace all phone numbers with a special token
                     no_digits=remove_digits,  # replace all numbers with a special token
                     no_currency_symbols=remove_currency,  # replace all currency symbols with a special token
                     no_punct=remove_punct,  # remove punctuations
                     replace_with_punct=" ",
                     replace_with_url=" ",
                     replace_with_email=" ",
                     replace_with_phone_number=" ",
                     replace_with_digit=" ",
                     replace_with_currency_symbol=" ",
                     lang="en"
                     )

        # Replace symbols
        text = re.sub(r"[!#$%&\"'()*+,\-./:;<=>?@[\\\]^_`{|}~]", " ", text)

        # Remove extra spaces
        text = re.sub(r'\s{2,}', " ", text)

        text = word_tokenize(text)

        if remove_stopwords:
            stops = set(stopwords.words("english"))
            text = [word for word in text if word not in stops]

        if lematization:
            wl = WordNetLemmatizer()
            text = [wl.lemmatize(word) for word in text]

        if stemming:
            ps = PorterStemmer()
            text = [ps.stem(word) for word in text]

        preprocessed_text = text

    return preprocessed_text
