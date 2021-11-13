import enum

from sqlalchemy import Column
from sqlalchemy import Enum
from sqlalchemy import Integer
from sqlalchemy import String

from ..database import Base


class Region(enum.Enum):
    APACN = "Asia-Pacific North"
    APACS = "Asia-Pacific South"
    EMEA = "Europe, Middle East, and Africa"
    NA = "North America"
    SA = "South America"


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    region = Column(Enum(Region))
