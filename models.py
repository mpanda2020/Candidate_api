from database import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String



class Candidate(Base):

    __tablename__ = "candidate"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(55)
    )

   