import argparse
import pickle

import pandas as pd

from topic_modeling import *

if __name__ == '__main__':

    # global variables
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--option", type=str, help="create/evaluate",
                        choices=["create", "evaluate"], required=True)
    parser.add_argument("-p", "--person", type=str, help="first_person/no_first_person",
                        choices=["first_person", "no_first_person"], required=True)
    args = parser.parse_args()
    path = Path.cwd()

    # python app\topic_model.py -o evaluate -p person
    if args.option == "evaluate":
        person = args.person
        data = pickle.load(open(f"{str(path)}/files/preprocessed_posts/preprocessed_{str(person)}.pkl", 'rb'))

        model_results = hyperparameter([post['preprocessed_body'] for post in data])

        pd.DataFrame(model_results).to_csv(f"{str(path)}/files/topic_model/{str(person)}/lda_tuning_results.csv",
                                           index=False)

    # python app\topic_model.py -o create -p person
    if args.option == "create":
        person = args.person

        data = pickle.load(open(f"{str(path)}/files/preprocessed_posts/preprocessed_{str(person)}.pkl", 'rb'))

        topic_modeling([post['preprocessed_body'] for post in data], 6, 'asymmetric', 'symmetric')
