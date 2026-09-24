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

DATABASE_URL = 'sqlite+pysqlite:///brazil_oil_production.sqlite'

engine = create_engine(DATABASE_URL, echo=True)
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

with engine.connect() as conn:
    dictlist = []
    for row in conn.execute(stmt).fetchall():
        dictitem = dict(row._mapping.items())
        dictlist.append(dictitem)

    with open('result.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(dictlist, ensure_ascii=False))
