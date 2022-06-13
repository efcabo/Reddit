from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def database_connect(target: str = "reddit"):
    """
    Permite establecer conexión coa BD
    """
    if target == "reddit":
        engine = create_engine(
            "mysql+pymysql://redditUser:Efcabo18@localhost:3306/reddit?charset=utf8mb4"
        )
    Session = sessionmaker(bind=engine)

    return Session()
