import datetime
import json
import praw
import logging
from pathlib import Path
from psaw import PushshiftAPI
from reddit_scraping.insert_data import *


def extract_data(subreddits: list, date_after: datetime, date_before: datetime):
    """
    Extrae, dos subreddits indicados, as publicacións realizadas entre date_after e date_before,
    xunto coa información asociada.

    Parameters
    ----------
    subreddits : list
        Lista dos subrredits dos que se extraerá a información
    date_after : datetime
        Data de inicio para a busca.
    date_before : datetime
        Data de fin para a busca.

    """

    # Obter as credenciais para usar PRAW
    path = Path.cwd()
    api = f"{str(path)}/files/credentials/client_secrets.json"
    with open(api) as f:
        datos = json.load(f)
    reddit = praw.Reddit(**datos)

    # Para usar PSAW
    api = PushshiftAPI()

    ts_after = int(date_after.timestamp())
    ts_before = int(date_before.timestamp())

    # Recoller os posibles erros nun arquivo log
    path = Path.cwd()
    file = f'{str(path)}/files/log/{date_after.day}-{date_after.month}-{date_after.year}_' \
           f'{date_before.day}-{date_before.month}-{date_before.year}.log '

    logging.basicConfig(filename=file, filemode='w')

    for element in subreddits:

        subreddit = reddit.subreddit(element)
        insert_subreddit(subreddit)

        print("Extraendo publicacións do subrredit " + element + "...")

        # Usar PSAW para obter os id das publicacións entre as datas indicadas
        gen = api.search_submissions(
            after=ts_after,
            before=ts_before,
            filter=['id'],
            subreddit=element
        )

        # Usar PRAW para obter a información completa da publicación
        for submission_psaw in gen:

            try:

                submission_id = submission_psaw.d_['id']
                submission_praw = reddit.submission(id=submission_id)

                # Nalgúns casos pódese producir un erro por non existir o autor, polo que se comproba antes
                # Ao contar con gran cantidade de información estes casos serán descartados
                author = submission_praw.author
                if author != None and hasattr(author, 'id'):

                    try:

                        insert_author(author)
                        insert_submission(submission_praw, author.id, subreddit.id)

                        date = datetime.utcfromtimestamp(submission_praw.created_utc).strftime('%Y-%m-%d %H:%M:%S')
                        print("     Extraendo datos das publicacións realizadas a " + date + "...")

                    except Exception:

                        logging.exception('Submission')

                    else:

                        # Obter a árbore de comentarios completa
                        submission_praw.comments.replace_more(limit=None)
                        for comment in submission_praw.comments.list():

                            try:

                                # Mesma comprobación que para as publicacións
                                author = comment.author
                                if author != None and hasattr(author, 'id'):
                                    insert_author(author)
                                    insert_comment(comment, author.id, subreddit.id)

                            except Exception:

                                logging.exception('Comment')

            except Exception:

                logging.exception('Error')
