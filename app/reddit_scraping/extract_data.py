import json
import praw
import logging
from pathlib import Path
from psaw import PushshiftAPI
from reddit_scraping.insert_data import *


def extract_data(subreddits: list, date_after: datetime, date_before:datetime):

    """
    Extrae dos subreddits indicados as publicacións realizadas entre date_after e date_before,
    xunto coa información asociada.

    """

    # to use PRAW
    path = Path.cwd()
    api = f"{str(path)}/files/credentials/client_secrets.json"
    with open(api) as f:
        datos = json.load(f)
    reddit = praw.Reddit(**datos)

    # to use PSAW
    api = PushshiftAPI()

    ts_after = int(date_after.timestamp())
    ts_before = int(date_before.timestamp())

    # log
    path = Path.cwd()
    file = f'{str(path)}/files/log/{date_after.day}-{date_after.month}-{date_after.year}_{date_before.day}-{date_before.month}-{date_before.year}.log '

    logging.basicConfig(filename=file, filemode='w')

    for element in subreddits:

        subreddit = reddit.subreddit(element)
        insert_subreddit(subreddit)

        # use PSAW only to get id of submissions in time interval
        gen = api.search_submissions(
            after=ts_after,
            before=ts_before,
            filter=['id'],
            subreddit=element
        )

        # use PRAW to get actual info and traverse comment tree
        for submission_psaw in gen:

            try:

                # use psaw here
                submission_id = submission_psaw.d_['id']

                # use praw from now on
                submission_praw = reddit.submission(id=submission_id)

                author = submission_praw.author
                if author != None and hasattr(author, 'id'):

                    try:

                        insert_author(author)
                        insert_submission(submission_praw, author.id, subreddit.id)

                        date = datetime.utcfromtimestamp(submission_praw.created_utc).strftime('%Y-%m-%d %H:%M:%S')
                        print(date)

                    except Exception:

                        logging.exception('Submission')

                    else:

                        submission_praw.comments.replace_more(limit=None)
                        for comment in submission_praw.comments.list():

                            try:

                                author = comment.author
                                if author != None and hasattr(author, 'id'):

                                    insert_author(author)
                                    insert_comment(comment, author.id, subreddit.id)

                            except Exception:

                                logging.exception('Comment')

            except Exception:

                logging.exception('Error')
