from sqlalchemy import Column, Integer, Table, ForeignKey
from app.database import Base

# Association table for many-to-many relationship between Challenge and Tag
# It’s a pure join table used by SQLAlchemy to link Challenge and Tag.
# Creates a table called challenge_tags in your database
# Each row links one Challenge to one Tag

challenge_tags = Table(
    'challenge_tags',
    Base.metadata,
    Column('challenge_id', ForeignKey('challenges.id'), primary_key=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True)
)