# Модели для ролей
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.database.db_configs import Base


# Модель для ролей
class Role(Base):
    __tablename__ = 'roles'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
