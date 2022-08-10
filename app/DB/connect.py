import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pathlib import Path


def database_connect(target: str = "reddit"):
    """
    Permite establecer a conexión coa base de datos.

    Parameters
    ----------
    target : str
        Indica a base de datos a empregar. Por defecto será 'reddit'.

    Returns
    -------
    Session
        Obxecto Session para a conexión coa base de datos mediante SQLAlchemy.
    """

    # Carga, do arquivo correspondente, os parámetros para crear a conexión.
    path = Path.cwd()
    api = f"{str(path)}/files/credentials/reddit_connection.json"

    with open(api) as f:
        datos = json.load(f)

    if target == "reddit":
        engine = create_engine(
            'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(datos['db_user'], datos['db_pass'],
                                                                    datos['db_host'],
                                                                    datos['db_port'], datos['database'])
        )
    Session = sessionmaker(bind=engine)

    return Session()
