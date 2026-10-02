import json

from sqlalchemy import (
    MetaData,
    Table,
    and_,
    create_engine,
    desc,
    select,
    case,
    func
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Production(Base):
    __tablename__ = 'production'
    row_id: Mapped[str] = mapped_column('ROWID', primary_key=True)
    year: Mapped[int] = mapped_column('Year')
    month: Mapped[int] = mapped_column('Month')
    state: Mapped[str] = mapped_column('State')
    basin: Mapped[str] = mapped_column('Basin')
    field: Mapped[str] = mapped_column('Field')
    well: Mapped[str] = mapped_column('Well')
    environment: Mapped[str] = mapped_column('Environment')
    installation: Mapped[str] = mapped_column('Installation')
    oil: Mapped[float] = mapped_column('Oil (m³)')
    condensate_oil: Mapped[float] = mapped_column('Condensate oil (m³)')
    associated_petroleum_gas: Mapped[float] = mapped_column('Associated petroleum gas (Mm³)')
    non_associated_petroleum_gas: Mapped[float] = mapped_column('Non-associated petroleum gas (Mm³)')
    water: Mapped[float] = mapped_column('Water (m³)')
    gas_injection: Mapped[float] = mapped_column('Gas injection (Mm³)')
    secondary_recovery_water_injection: Mapped[float] = mapped_column('Secondary recovery water injection (m³)')
    wastewater_injection: Mapped[float] = mapped_column('Wastewater injection (m³)')
    co_injection: Mapped[float] = mapped_column('CO2 injection (Mm³)')
    nitrogen_injection: Mapped[float] = mapped_column('Nitrogen injection (Mm³)')
    steam_injection: Mapped[float] = mapped_column('Steam injection (t)')
    polymer_injection: Mapped[float] = mapped_column('Polymer injection (m³)')
    others_fluids_injection: Mapped[float] = mapped_column('Others fluids injection (m³)')
     
DATABASE_URL = 'sqlite+pysqlite:///brazil_oil_production.sqlite'

engine = create_engine(DATABASE_URL, echo=True)

with engine.connect() as conn:

    # production = Table(
    #     'production',
    #     MetaData(),
    #     autoload_with=engine,
    # )

    # stmt = (
    #     select(
    #         # case(
    #         #     (production.columns['Basin'] == 'Santos', 'Charlie Brown Jr.'),
    #         #     else_=production.columns['Basin']
    #         # ).label('Município'),
    #         #production.columns['State'].label('Estado'),
    #         case(
    #             (production.columns['Field'] == 'LULA', 'Ladrão'), else_=production.columns['Field']
    #         ).label('Campo'),
    #         #production.columns['Installation'].label('Instalação'),
    #         func.sum(production.columns['Oil (m³)']).label("Soma total"),
    #     )
    #     .where(
    #         and_(
    #         production.c.State.in_(['SP', 'RJ']), production.columns['Oil (m³)'].is_not(None))
    #     ).group_by(production.columns['Field'])
    #     .order_by(desc(production.columns['Oil (m³)']))
    # ).limit(10000)

    stmt = (
        select(
            #case(
            #    (Production.basin == 'Santos', 'Charlie Brown Jr.'),
            #    else_=Production.basin
            #).label('Municipio'),
            #Production.state.label('Estado'),
            case(
                (Production.field == 'Lula', 'Ladrão'), else_=Production.field
            ).label('Campo'),
            #Production.installation.label('Instalação'),
            func.sum(Production.oil.label('Soma Total').label('Soma total'))
        )
        .where(
            and_(
                Production.state.in_(['SP', 'RJ']), Production.oil.is_not(None)
            )
        ).group_by(Production.field)
        .order_by(desc(Production.oil))
    ).limit(1000)


    dictlist = []
    # Com conn begin, criando a possibilidade de realizar consultas atômicas, acabanco com a necessidade de criar várias conexões para cada consulta.
    # Com o begin, é possível realizar N consultas, dentro de uma conexão. Se algo não sair como o esperado, ROLLBACK
    with conn.begin():
        for row in conn.execute(stmt).fetchall():
            dictitem = dict(row._mapping.items())
            dictlist.append(dictitem)

    with open('result.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(dictlist, ensure_ascii=False)) 
