import json

from sqlalchemy import (
    Column,
    Float,
    MetaData,
    Table,
    and_,
    create_engine,
    desc,
    select,
    case,
    alias
)
from sqlalchemy.ext.asyncio import create_async_engine
from asyncio import run

DATABASE_URL = 'sqlite+pysqlite:///brazil_oil_production.sqlite'

engine = create_async_engine(DATABASE_URL, echo=True)

async def main():
    async with engine.connect() as conn:

        metadata_obj = MetaData()

        production = Table(
            'production',
            metadata_obj,
            Column('Oil (m³)', Float),
            Column('Condensate oil (m³)', Float),
            autoload_with=engine,
        )

        stmt = (
            select(
                case(
                    (production.columns['Basin'] == 'Santos', 'Charlie Brown Jr.'),
                    else_=production.columns['Basin']
                ).label('Município'),
                production.columns['State'].label('Estado'),
                case(
                    (production.columns['Field'] == 'LULA', 'Ladrão'), else_=production.columns['Field']
                ).label('Campo'),
                production.columns['Installation'].label('Instalação'),
                production.columns['Oil (m³)'],
            )
            .where(
                and_(
                production.c.State.in_(['SP', 'RJ']), production.columns['Oil (m³)'].is_not(None))
            )
            .order_by(desc(production.columns['Oil (m³)']))
        ).limit(10000)


        dictlist = []
        # Com conn begin, criando a possibilidade de realizar consultas atômicas, acabanco com a necessidade de criar várias conexões para cada consulta.
        # Com o begin, é possível realizar N consultas, dentro de uma conexão. Se algo não sair como o esperado, ROLLBACK
        with conn.begin():
            for row in conn.execute(stmt).fetchall():
                dictitem = dict(row._mapping.items())
                dictlist.append(dictitem)

        with open('result.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(dictlist, ensure_ascii=False)) 

run(main())



#1788912000000
#1790467200000