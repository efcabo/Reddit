import argparse
import os
import pickle
from pathlib import Path
from DB.connect import database_connect
from models import Post
from pos_tagging import *

if __name__ == '__main__':

    # global variables
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--option", type=str, help="classification/visualization/search",
                        choices=["classification", "visualization", "search"], required=True)
    parser.add_argument("-l", "--limit", type=int, help="post limit", default="100")
    parser.add_argument("-w", "--word", type=str, help="search: word", default="")
    parser.add_argument("-t", "--tag", type=str, help="search: tag",default="",
                        choices=['Nouns', 'Possesives', 'Personal pronouns', 'Adverbs', 'Adjectives', 'Verbs'])
    parser.add_argument("-p", "--person", type=str, help="first_person/no_first_person",
                        choices=["first_person", "no_first_person"], default="first_person")

    args = parser.parse_args()
    path = Path.cwd()

    # python app\pos_tagger.py -o classification -l limit
    if args.option == "classification":

        limit = args.limit

        session = database_connect()
        posts = session.query(Post).filter(Post.parent_key == None).filter(Post.body != None).filter(
            Post.body != '[eliminado]').filter(Post.body != '').limit(limit).all()

        data = [{'key': post.post_key, 'body': post.body, 'title': post.link_title} for post in posts]

        first_person, no_first_person = person_classification(data)

        if os.path.isfile(f"{str(path)}/files/classified_posts/posts_first_person.pkl"):
            pre_first_person = pickle.load(open(f"{str(path)}/files/classified_posts/posts_first_person.pkl", 'rb'))
            first_person = pre_first_person + first_person

        if os.path.isfile(f"{str(path)}/files/classified_posts/posts_no_first_person.pkl"):
            pre_no_first_person = pickle.load(open(f"{str(path)}/files/classified_posts/posts_no_first_person.pkl", 'rb'))
            no_first_person = pre_no_first_person + no_first_person

        pickle.dump(first_person, open(f"{str(path)}/files/classified_posts/posts_first_person.pkl", 'wb'))
        pickle.dump(no_first_person, open(f"{str(path)}/files/classified_posts/posts_no_first_person.pkl", 'wb'))

        # python app\pos_tagger.py -o visualization -p person
    if args.option == "visualization":
        person = args.person

        data = pickle.load(open(f"{str(path)}/files/classified_posts/posts_{str(person)}.pkl", 'rb'))
        pos_visualization([f"{post['title']}\n{post['body']}" for post in data])

        # python app\pos_tagger.py -o search -p person -w word -t tag
    if args.option == "search":
        word = args.word
        tag = args.tag
        person = args.person

        data = pickle.load(open(f"{str(path)}/files/classified_posts/posts_{str(person)}.pkl", 'rb'))
        search_texts([f"{post['title']}\n{post['body']}" for post in data], word, tag)
