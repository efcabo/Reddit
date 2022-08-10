from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    Representa un usuario.
    """

    __tablename__ = 'User'

    user_key = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    user_id = Column(String(50), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    created_utc = Column(DateTime, nullable=False)
    subreddit = Column(String(50))
    accept_chats = Column(Boolean)
    accept_followers = Column(Boolean)
    accept_pms = Column(Boolean)
    awardee_karma = Column(Integer)
    awarder_karma = Column(Integer)
    comment_karma = Column(Integer)
    has_subscribed = Column(Boolean)
    has_verified_email = Column(Boolean)
    hide_from_robots = Column(Boolean)
    icon_img = Column(Text)
    is_employee = Column(Boolean)
    is_gold = Column(Boolean)
    is_mod = Column(Boolean)
    link_karma = Column(Integer)
    pref_show_snoovatar = Column(Boolean)
    snoovatar_img = Column(Text)
    total_karma = Column(Integer)
    verified = Column(Boolean)
