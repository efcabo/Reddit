import os
import argparse
import pickle
from pathlib import Path
from data_preprocessing.data_preprocessing import data_preprocessing

if __name__ == '__main__':

    # global variables
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--person", type=str, help="first_person/no_first_person",
                        choices=["first_person", "no_first_person"], required=True)
    args = parser.parse_args()

    path = Path.cwd()

    # python app\preprocess_data.py -p person

    person = args.person
    data = pickle.load(open(f"{str(path)}/files/classified_posts/posts_{str(person)}.pkl", 'rb'))

    preprocessed_posts = [{'key': post['key'],
                           'body': post['body'],
                           'title': post['title'],
                           'preprocessed_body': data_preprocessing(post['body']),
                           'preprocessed_title': data_preprocessing(post['title'])}
                          for post in data]

    if os.path.isfile(f"{str(path)}/files/preprocessed_posts/preprocessed_{str(person)}.pkl"):
        pre = pickle.load(open(f"{str(path)}/files/preprocessed_posts/preprocessed_{str(person)}.pkl", 'rb'))
        preprocessed_posts = pre + preprocessed_posts

    pickle.dump(preprocessed_posts, open(f"{str(path)}/files/preprocessed_posts/preprocessed_{str(person)}.pkl", 'wb'))
