from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Post_has_Award(Base):
    """
    Representa a relación entre os premios e as publicacións ou comentarios.
    """

    __tablename__ = 'Post_has_Award'

    post_key = Column(Integer, nullable=False, primary_key=True)
    award_key = Column(Integer, nullable=False, primary_key=True)
    post_id = Column(String(50), nullable=False)
    award_id = Column(String(50), nullable=False)
