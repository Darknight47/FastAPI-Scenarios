# A join table for many-to-many relationship between Path and Challenge!
from sqlalchemy import Table, Column, ForeignKey
from app.database import Base

# it’s a pure join table used by SQLAlchemy to link Path and Challenge.

# Creates a table called path_challenges in your database
# Each row links one Path to one Challenge
# Both columns are foreign keys pointing to their respective tables
# primary_key=True on both makes the combination unique — no duplicate links

path_challenges = Table(
    'path_challenges',
    Base.metadata,
    Column('path_id', ForeignKey('paths.id'), primary_key=True),
    Column('challenge_id', ForeignKey('challenges.id'), primary_key=True)
)