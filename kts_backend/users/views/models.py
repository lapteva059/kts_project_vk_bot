from dataclasses import dataclass

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from kts_backend.store.database.sqlalchemy_database import db


@dataclass
class Player:
    vk_id: int


class PlayerModel(db):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    vk_id = Column(Integer, unique=True, nullable=False)