from gensim import corpora, models
import numpy as np
import tqdm
from pathlib import Path

path = Path.cwd()


def compute_coherence_values(corpus, texts, dictionary, k, a, b):
    """
    Calcula o valor de coherencia do modelo cos parámetros indicados
    """
    lda_model = models.LdaMulticore(corpus=corpus,
                                    id2word=dictionary,
                                    num_topics=k,
                                    random_state=100,
                                    chunksize=100,
                                    passes=10,
                                    alpha=a,
                                    eta=b)

    coherence_model_lda = models.CoherenceModel(model=lda_model, texts=texts, dictionary=dictionary, coherence='c_v')

    return coherence_model_lda.get_coherence()


def hyperparameter(texts):
    """
    Calcula o valor de coherencia para diferentes combinacións de valores dos parámetros co obxetivo
    de atopar os máis axeitados para os textos empregados
    """

    print(len(texts))

    texts = [text for text in texts if text != []]

    dictionary = corpora.Dictionary(texts)

    corpus = [dictionary.doc2bow(text) for text in texts]
    tfidf = models.TfidfModel(corpus)
    corpus = tfidf[corpus]

    # Topics range(min_topics, max_topics, step_size)
    topics_range = range(2, 11, 1)

    # Alpha parameter
    alpha = list(np.arange(0.01, 1, 0.3))
    alpha.append('symmetric')
    alpha.append('asymmetric')

    # Beta parameter
    beta = list(np.arange(0.01, 1, 0.3))
    beta.append('symmetric')

    model_results = {'Topics': [],
                     'Alpha': [],
                     'Beta': [],
                     'Coherence': []
                     }

    total = len(topics_range) * len(alpha) * len(beta)

    if 1 == 1:
        pbar = tqdm.tqdm(total=total)

        # iterate through parameters
        for k in topics_range:
            for a in alpha:
                for b in beta:
                    # get the coherence score
                    cv = compute_coherence_values(corpus=corpus, texts=texts, dictionary=dictionary,
                                                  k=k, a=a, b=b)
                    # Save results
                    model_results['Topics'].append(k)
                    model_results['Alpha'].append(a)
                    model_results['Beta'].append(b)
                    model_results['Coherence'].append(cv)

                    pbar.update(1)

        pbar.close()

        return model_results

