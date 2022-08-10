import argparse
import os
import pickle
import pyLDAvis.gensim_models
import pandas as pd

from topic_modeling import *


if __name__ == '__main__':

    # Definición dos argumentos de entrada
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--option", type=str,
                        help="Selecciona unha das opcións do script:"
                             "-Create - creación do modelo"
                             "-Evaluate - avaliación ou hiperparametrización do modelo",
                        choices=["create", "evaluate"], required=True)

    parser.add_argument("-if", "--input_filename", type=Path,
                        help="Selecciona a ruta ao arquivo co conxunto de textos de entrada.", required=True)

    parser.add_argument("-od", "--output_directory", type=Path,
                        help="Selecciona a ruta  ao directorio onde se almacenarán os resultados."
                             "Se non se especifica, almacenarase no directorio actual.", default=Path.cwd())

    parser.add_argument("-n", "--num_topics", type=int,
                        help="Valor do parámetos num_topics. Aplicable para a opción create.", default=6)

    parser.add_argument("-a", "--alpha", type=str,
                        help="Valor do parámetro alpha. Aplicable para a opción create.", default='0.01')

    parser.add_argument("-e", "--eta", type=str,
                        help="Valor do parámetro eta. Aplicable para a opción create.", default='0.01')

    args = parser.parse_args()
    path = Path.cwd()

    # Hiperparametrización ou avaliación do modelo
    if args.option == "evaluate":

        if os.path.isfile(args.input_filename):
            data = pickle.load(open(f"{str(args.input_filename)}", 'rb'))

            # Proceso de hiperparametrización
            if os.path.exists(args.output_directory):

                model_results = hyperparameter([post['preprocessed_body'] for post in data])

                pd.DataFrame(model_results).to_csv(
                    f"{str(args.output_directory)}/lda_tuning_results.csv", index=False)

                print('Resultados almacenados no directorio ' + str(args.output_directory.absolute()))
            else:
                print('O directorio non existe.')

        else:
            print("O arquivo especificado non existe.")

    # Creación do modelo
    if args.option == "create":

        if os.path.isfile(args.input_filename):
            data = pickle.load(open(f"{str(args.input_filename)}", 'rb'))

            if os.path.exists(args.output_directory):

                if args.alpha != 'symmetric' and args.alpha != 'asymmetric':
                    alpha = float(args.alpha)

                else:
                    alpha = args.alpha

                if args.eta != 'symmetric' and args.alpha != 'asymmetric':
                    eta = float(args.eta)

                else:
                    eta = args.eta

                parameters = {'num_topics': args.num_topics,
                              'alpha': alpha,
                              'eta': eta
                              }

                topics, dictionary, lda_model, corpus = topic_modeling([post['preprocessed_body'] for post in data],
                                                                       parameters)
                # Almacenamento dos resultados
                dictionary.save(f"{str(args.output_directory)}/dictionary.gensim")
                lda_model.save(f"{str(args.output_directory)}/model5.gensim")

                # Visualización dos resultados
                for topic in topics:
                    print(topic)

                lda_display = pyLDAvis.gensim_models.prepare(topic_model=lda_model, corpus=corpus,
                                                             dictionary=dictionary)
                pyLDAvis.save_html(lda_display, f"{str(args.output_directory)}/topics.html")

                print('Resultados almacenados no directorio ' + str(args.output_directory.absolute()))
            else:
                print('O directorio non existe.')

        else:
            print("O arquivo especificado non existe.")
