import json

from sqlalchemy import (
    ForeignKey,
    create_engine,
    delete,
    insert,
    select,
    update,
)
from sqlalchemy.orm import (
    Mapped,
    Session,
    mapped_column,
    registry,
)

rg = registry()


@rg.mapped_as_dataclass
class Artist:
    __tablename__ = 'artists'

    artist_id: Mapped[int] = mapped_column('artist_id', primary_key=True)
    name: Mapped[str] = mapped_column('name')


@rg.mapped_as_dataclass
class Albums:
    __tablename__ = 'albums'
    album_id: Mapped[int] = mapped_column('album_id', primary_key=True)
    artist_id: Mapped[str] = mapped_column(ForeignKey('artists.artist_id'))
    title: Mapped[str] = mapped_column('title')


@rg.mapped_as_dataclass
class Genre:
    __tablename__ = 'genres'
    genre_id: Mapped[int] = mapped_column('genre_id', primary_key=True)
    name: Mapped[str] = mapped_column('name')


@rg.mapped_as_dataclass
class Tracks:
    __tablename__ = 'tracks'
    track_id: Mapped[int] = mapped_column('track_id', primary_key=True)
    name: Mapped[str] = mapped_column('name')
    album_id: Mapped[int] = mapped_column(ForeignKey('albums.album_id'))
    genre_id: Mapped[int] = mapped_column(ForeignKey('genres.genre_id'))
    milliseconds: Mapped[int] = mapped_column('milliseconds')
    unit_price: Mapped[float] = mapped_column('unit_price')


@rg.mapped_as_dataclass
class Test:
    __tablename__ = 'testtable'
    test_id: Mapped[int] = mapped_column('test_id', primary_key=True)
    test_name: Mapped[str] = mapped_column('test_name')
    test_desc: Mapped[str] = mapped_column('test_description', init=False)


# Criando engine de conexão
DATABASE_URL = 'sqlite+pysqlite:///chinook_sample.sqlite'

engine = create_engine(DATABASE_URL, echo=True)

# Iniciando conexão
# with engine.connect() as conn:
with Session(engine) as conn:
    # rg.metadata.create_all(engine)

    stmt = (
        select(Tracks.name, Genre.name, Artist.name, Albums.title)
        .join(Albums, Artist.artist_id == Albums.artist_id)
        .join(Tracks, Albums.album_id == Tracks.album_id)
        .join(Genre, Tracks.genre_id == Genre.genre_id)
        .where(Albums.title == 'Master Of Puppets')
    )

    q_insert = (
        # insert(Artist).values(name='Limp Bizkit')
        insert(Albums).values(
            title='Chocolate Starfish And The Hot Dog Flavored Water',
            artist_id=6,
        )
    )

    q_delete = delete(Genre).where(Genre.genre_id == 1)

    q_insert = insert(Genre).values(genre_id=1, name='Rock')

    q_update = (
        update(Genre)
        .where(Genre.genre_id == 1)
        .values(name='Traditional rock')
    )

    dictlist: list[dict] = []

    # Criando lista de dicionários com o resultado da consulta
    with conn.begin():
        for row in conn.execute(stmt).fetchall():
            dictitem = dict(row._mapping.items())
            dictlist.append(dictitem)

        # conn.execute(q_insert)
        # conn.execute(q_delete)
        conn.execute(q_update)

        # conn.rollback()
        conn.commit()

    with open('result.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(dictlist, ensure_ascii=False))
