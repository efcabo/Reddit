import argparse
import datetime as dt
from reddit_scraping import extract_data

if __name__ == '__main__':
    # global variables
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--subreddits", nargs='+', type=str, help="subreddits", required=True)
    parser.add_argument("-a", "--after", type=str, help="%d/%m/%Y", required=True)
    parser.add_argument("-b", "--before", type=str, help="'%d/%m/%Y", required=True)
    args = parser.parse_args()

    # python app\reddit_scraper.py -s subreddit1, subreddit2 -a date_after -b date_before

    subreddits = args.subreddits

    try:
        format_str = '%d/%m/%Y'
        date_after = dt.datetime.strptime(args.after, format_str)
        date_before = dt.datetime.strptime(args.before, format_str)
    except ValueError:
        print("Format: %d/%m/%Y")

    else:
        extract_data(subreddits, date_after, date_before)

    # date_after = dt.datetime(2021, 7, 31)
    # date_before = dt.datetime(2021, 8, 30)
    # date_after = dt.datetime(2021, 9, 30)
    # date_before = dt.datetime(2021, 12, 9)
