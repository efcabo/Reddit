import os
import argparse
import pickle
from pathlib import Path
from data_preprocessing.data_preprocessing import data_preprocessing

if __name__ == '__main__':

    # Definición dos argumentos de entrada
    parser = argparse.ArgumentParser(description="Preprocesado do conxunto de textos de entrada")

    parser.add_argument("-od", "--output_directory", type=Path,
                        help="Selecciona a ruta  ao directorio onde se almacenarán os resultados."
                             "Se non se especifica, almacenaranse no directorio actual.", default=Path.cwd())
    parser.add_argument("-if", "--input_filename", type=Path,
                        help="Selecciona a ruta ao arquivo co conxunto de textos de entrada.", required=True)
    parser.add_argument("-mw", "--min_words", type=int,
                        help="Seleccionar o número mínimo de palabras para ter en conta un texto ", default=10)
    parser.add_argument("-rht", "--remove_htlm", type=bool,
                        help="Eliminar trazas de HTML. Por defecto será True.", default=True)
    parser.add_argument("-rsub", "--remove_subreddits", type=bool,
                        help="Eliminar nomes de subreddits. Por defecto será True.", default=True)
    parser.add_argument("-rha", "--remove_hashtags", type=bool,
                        help="Eliminar hashtags. Por defecto será True.", default=True)
    parser.add_argument("-rc", "--remove_contractions", type=bool,
                        help="Desfacer contraccións. Por defecto será True.", default=True)
    parser.add_argument("-uct", "--use_clean_text", type=bool,
                        help="Empregar clean-text para a limpeza. Por defecto será True.", default=True)
    parser.add_argument("-rstop", "--remove_stopwords", type=bool,
                        help="Eliminar stopwords. Por defecto será True. ", default=True)
    parser.add_argument("-sol", "--stem_or_lem", type=str,
                        help="Empregar lematización ou stemming. Por defecto será True.",
                        choices=["lemmatization", "stemming"])

    args = parser.parse_args()

    path = Path.cwd()

    options = {'min_words': args.min_words,
               'remove_htlm': args.remove_htlm,
               'remove_subreddits': args.remove_subreddits,
               'remove_hashtags': args.remove_hashtags,
               'remove_contractions': args.remove_contractions,
               'use_clean_text': args.use_clean_text,
               'remove_stopwords': args.remove_stopwords,
               'stemming': True if args.stem_or_lem == "stemming" else False,
               'lemmatization': True if args.stem_or_lem == "lemmatization" else False,
               }

    if os.path.isfile(args.input_filename):
        data = pickle.load(open(f"{str(args.input_filename)}", 'rb'))

        if os.path.exists(args.output_directory):

            # Preprocesado das publicacións
            preprocessed_posts = [{'key': post['key'],
                                   'body': post['body'],
                                   'title': post['title'],
                                   'preprocessed_body': data_preprocessing(post['body'], options),
                                   'preprocessed_title': data_preprocessing(post['title'], options)}
                                  for post in data]

            pickle.dump(preprocessed_posts, open(f"{str(args.output_directory)}/data_preprocessed.pkl", 'wb'))
            print('Resultados almacenados no directorio ' + str(args.output_directory.absolute()))

        else:
            print('O directorio non existe.')

    else:
        print("O arquivo especificado non existe.")
