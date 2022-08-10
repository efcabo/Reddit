import argparse
import datetime as dt
from reddit_scraping import extract_data

if __name__ == '__main__':

    # Definición dos argumentos de entrada
    parser = argparse.ArgumentParser(description='Extracción de datos de un ou varios subreddits entre as datas '
                                                 'especificadas.')

    parser.add_argument("-s", "--subreddits", nargs='+', type=str,
                        help="Lista de subrredits para realizar a extracción. Debe especificarse como mínimo un.",
                        required=True)

    parser.add_argument("-a", "--after", type=str,
                        help="Data de inicio da extracción en formato DD/MM/YYYY.", required=True)

    parser.add_argument("-b", "--before", type=str,
                        help="Data de fin da extracción en formato DD/MM/YYYY. Debe ser posterior á data de inicio.",
                        required=True)

    args = parser.parse_args()

    # Aplicar formato ás datas
    try:
        format_str = '%d/%m/%Y'
        date_after = dt.datetime.strptime(args.after, format_str)
        date_before = dt.datetime.strptime(args.before, format_str)

    except ValueError:
        print("Formato de data incorrecto. O formato debe ser: DD/MM/YYYY")

    else:

        if date_after < date_before:
            # Proceso de extracción
            subreddits = args.subreddits
            extract_data(subreddits, date_after, date_before)
        else:
            print('A data de inicio da extracción debe ser anterior á de fin.')
