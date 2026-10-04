import json

from sqlalchemy import ForeignKey, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# Criando classe base declarativa
class Base(DeclarativeBase):
    pass


# Criando classes mapeadas das tabelas
class Artist(Base):
    __tablename__ = 'artists'
    artist_id: Mapped[int] = mapped_column('artist_id', primary_key=True)
    name: Mapped[str] = mapped_column('name')


class Albums(Base):
    __tablename__ = 'albums'
    album_id: Mapped[int] = mapped_column('album_id', primary_key=True)
    artist_id: Mapped[str] = mapped_column(ForeignKey('artists.artist_id'))
    title: Mapped[str] = mapped_column('title')


class Genre(Base):
    __tablename__ = 'genres'
    genre_id: Mapped[int] = mapped_column('genre_id', primary_key=True)
    name: Mapped[str] = mapped_column('name')


class Tracks(Base):
    __tablename__ = 'tracks'
    track_id: Mapped[int] = mapped_column('track_id', primary_key=True)
    name: Mapped[str] = mapped_column('name')
    album_id: Mapped[int] = mapped_column(ForeignKey('albums.album_id'))
    genre_id: Mapped[int] = mapped_column(ForeignKey('genres.genre_id'))
    milliseconds: Mapped[int] = mapped_column('milliseconds')
    unit_price: Mapped[float] = mapped_column('unit_price')


# Criando engine de conexão
DATABASE_URL = 'sqlite+pysqlite:///chinook_sample.sqlite'

engine = create_engine(DATABASE_URL, echo=True)

# Iniciando conexão
with engine.connect() as conn:
    stmt = (
        select(Tracks.name, Genre.name, Artist.name, Albums.title)
        .join(Albums, Artist.artist_id == Albums.artist_id)
        .join(Tracks, Albums.album_id == Tracks.album_id)
        .join(Genre, Tracks.genre_id == Genre.genre_id)
        .where(Albums.title == 'Machine Head')
    )

    dictlist: list[dict] = []

    # Criando lista de dicionários com o resultado da consulta
    with conn.begin():
        for row in conn.execute(stmt).fetchall():
            dictitem = dict(row._mapping.items())
            dictlist.append(dictitem)

    with open('result.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(dictlist, ensure_ascii=False))
