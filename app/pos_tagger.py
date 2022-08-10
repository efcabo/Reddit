import argparse
import os
import pickle
from pathlib import Path
from DB.connect import database_connect
from models import Post
from pos_tagging import *


if __name__ == '__main__':

    # Definición dos argumentos de entrada
    parser = argparse.ArgumentParser(description='Aplicación e visualización das técnicas de etiquetado gramatical.')

    parser.add_argument("-o", "--option", type=str,
                        help="Selecciona unha das opcións do script: "
                             "- Classification - proceso de clasificación."
                             "- Visualization - visualización dos gráficos."
                             "- Search - busca de textos.",
                        choices=["classification", "visualization", "search"], required=True)

    parser.add_argument("-od", "--output_directory", type=Path,
                        help="Selecciona a ruta  do directorio onde se almacenarán os resultados. "
                             "Se non se especifica, almacenaranse no directorio actual. "
                             "Aplicable para as opcións classification e search.", default=Path.cwd())

    parser.add_argument("-l", "--limit", type=int,
                        help="Número máximo de publicacións a extraer da base de datos."
                             "Se non se especifica, aplicarase o valor por defecto 100."
                             "Aplicable para a opción classification.", default="100")

    parser.add_argument("-if", "--input_filename", type=Path,
                        help="Selecciona a ruta ao arquivo co conxunto de datos de entrada."
                             "Aplicable para as opcións visualization e search.")

    parser.add_argument("-w", "--word", type=str,
                        help="Palabra a buscar no conxunto de textos especificado. "
                             "Aplicable para a opción search", default="")

    parser.add_argument("-t", "--tag", type=str,
                        help="Etiqueta asociada á palabra a buscar no conxunto de textos. "
                             "Aplicable para a opción search.",
                        choices=['Nouns', 'Possesives', 'Personal pronouns', 'Adverbs', 'Adjectives', 'Verbs'], default="")

    args = parser.parse_args()
    path = Path.cwd()

    # Clasificación das publicacións
    if args.option == "classification":
        limit = args.limit

        # Extracción de publicacións da base de datos. O número é especificado polo parámetro limit
        session = database_connect()
        posts = session.query(Post).filter(Post.parent_key == None).filter(Post.body != None).filter(
            Post.body != '[eliminado]').filter(Post.body != '').limit(limit).all()

        # Almacenamento da información nun diccionario
        data = [{'key': post.post_key, 'body': post.body, 'title': post.link_title} for post in posts]

        # Levar a cabo o proceso de clasificación
        first_person, no_first_person = person_classification(data)

        # Almacenar os resultados
        if os.path.exists(args.output_directory):

            pickle.dump(first_person, open(f"{str(args.output_directory)}/posts_first_person.pkl", 'wb'))
            pickle.dump(no_first_person, open(f"{str(args.output_directory)}/posts_no_first_person.pkl", 'wb'))

            print('Resultados almacenados no directorio ' + str(args.output_directory.absolute()))
        else:
            print('O directorio non existe.')

    # Visualización dos gráficos
    if args.option == "visualization":
        if os.path.isfile(args.input_filename):
            data = pickle.load(open(f"{str(args.input_filename)}", 'rb'))
            pos_visualization([f"{post['title']}\n{post['body']}" for post in data])

        else:
            print("O arquivo especificado non existe.")

    # Busca de textos que coincidan cos parámetros
    if args.option == "search":
        word = args.word
        tag = args.tag

        if os.path.isfile(args.input_filename):

            if word == "" or tag == "":
                print("Debe especifircarse unha palabra e unha etiqueta para a busca.")
            else:

                if os.path.exists(args.output_directory):
                    data = pickle.load(open(f"{str(args.input_filename)}", 'rb'))
                    results = search_texts([f"{post['title']}\n{post['body']}" for post in data], word, tag)
                    pickle.dump(results, open(f"{str(args.output_directory)}/search_results_{word}_{tag}.pkl", 'wb'))

                else:

                    print("O arquivo especificado non existe.")

        else:
            print("O arquivo especificado non existe.")


