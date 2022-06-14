from gensim import corpora, models
import pyLDAvis.gensim_models
from pathlib import Path

path = Path.cwd()


def topic_modeling(texts: list, k, a, b, tfidf=True):
    """
    Crea o modelo cos parámetros indicados
    """

    texts = [text for text in texts if text != []]

    dictionary = corpora.Dictionary(texts)

    corpus = [dictionary.doc2bow(text) for text in texts]

    if tfidf:
        tfidf = models.TfidfModel(corpus)
        corpus = tfidf[corpus]

    dictionary.save(f"{str(path)}/files/topic_model/dictionary.gensim")

    lda_model = models.LdaMulticore(corpus=corpus,
                                    id2word=dictionary,
                                    num_topics=k,
                                    random_state=100,
                                    chunksize=100,
                                    passes=10,
                                    alpha=a,
                                    eta=b)
    lda_model.save(f"{str(path)}/files/topic_model/model5.gensim")

    topics = lda_model.print_topics()

    for topic in topics:
        print(topic)

    lda_display = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
    pyLDAvis.save_html(lda_display, f"{str(path)}/files/topic_model/topics.html")
