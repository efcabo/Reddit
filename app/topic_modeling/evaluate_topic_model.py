import numpy as np
import tqdm
from gensim import corpora
from pathlib import Path
from gensim import models
path = Path.cwd()


def compute_metrics(corpus, texts, dictionary, k, a, e):
    """
    Calcula os valorer de coherencia e perplexidade do modelo cos parámetros indicados

    Returns
    -------
    tuple
        Devolve unha tupla cos valores de coherencia e perplexidade
    """

    lda_model = models.LdaMulticore(corpus=corpus,
                                    id2word=dictionary,
                                    num_topics=k,
                                    random_state=100,
                                    chunksize=100,
                                    passes=10,
                                    alpha=a,
                                    eta=e)

    perplexity = lda_model.log_perplexity(corpus)

    coherence_model_lda = models.CoherenceModel(model=lda_model, texts=texts, dictionary=dictionary, coherence='c_v')

    return coherence_model_lda.get_coherence(), perplexity


def hyperparameter(texts: list):
    """
    Calcula o valores de coherencia e perplexidade para diferentes combinacións de valores dos parámetros co obxetivo
    de atopar os máis axeitados para os textos empregados

    Parameters
    ----------
    texts : list
        Conxunto de textos de entrada para avaliar o modelo

    Returns
    -------
    dict
        Diccionario que recolle os valores de coherencia e perplexidade para cada combinación de parámetros

    """

    texts = [text for text in texts if text != []]

    dictionary = corpora.Dictionary(texts)

    corpus = [dictionary.doc2bow(text) for text in texts]
    tfidf = models.TfidfModel(corpus)
    corpus = tfidf[corpus]

    # Topics range(min_topics, max_topics, step_size)
    topics_range = range(2, 11, 1)

    # Parámetro Alpha
    alpha = list(np.arange(0.01, 1, 0.3))
    alpha.append('symmetric')
    alpha.append('asymmetric')

    # Parámetro Eta
    eta = list(np.arange(0.01, 1, 0.3))
    eta.append('symmetric')

    model_results = {'Topics': [],
                     'Alpha': [],
                     'Eta': [],
                     'Coherence': [],
                     'Perplexity': []
                     }

    total = len(topics_range) * len(alpha) * len(eta)

    if 1 == 1:
        pbar = tqdm.tqdm(total=total)

        # Iterar sobre os parámetros
        for k in topics_range:
            for a in alpha:
                for e in eta:
                    # Calcular coherencia e perplexidade
                    cv, perplexity = compute_metrics(corpus=corpus, texts=texts, dictionary=dictionary,
                                                     k=k, a=a, e=e)
                    # Gardar resultados
                    model_results['Topics'].append(k)
                    model_results['Alpha'].append(a)
                    model_results['Eta'].append(e)
                    model_results['Coherence'].append(cv)
                    model_results['Perplexity'].append(perplexity)

                    pbar.update(1)

        pbar.close()

        return model_results



