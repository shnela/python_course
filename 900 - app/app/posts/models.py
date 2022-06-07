from datetime import datetime, timezone

from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey

from app.database import Base


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    content = Column(Text(), nullable=False)
    creation_date = Column(DateTime(timezone=True), nullable=False,
                           default=lambda: datetime.now(tz=timezone.utc))
    # user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
