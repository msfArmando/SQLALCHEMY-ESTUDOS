from sqlalchemy import create_engine, ForeignKey, delete
from sqlalchemy.orm import Session, registry, Mapped, mapped_column
from dotenv import load_dotenv
import os

rg = registry()
load_dotenv()
DB_URL = os.getenv('DB_URL')

@rg.mapped_as_dataclass
class Alembic_Versions:
    __tablename__ = 'alembic_version'
    version_num: Mapped[str] = mapped_column('version_num', primary_key=True)

engine = create_engine(str(DB_URL))

with Session(engine) as conn:

    delete_column = delete(Alembic_Versions)
    
    with conn.begin():
        conn.execute(delete_column)
        conn.commit()
        pass
