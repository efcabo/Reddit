from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Award(Base):
    """
    Representa un premio.
    """

    __tablename__ = 'Award'

    award_key = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    award_id = Column(String(50), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    award_sub_type = Column(String(50))
    award_type = Column(String(50))
    coin_price = Column(Integer)
    coin_reward = Column(Integer)
    subreddit_coin_reward = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    icon_url = Column(Text)
