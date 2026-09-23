from sqlalchemy import create_engine, MetaData, Table, select, Column, Float
import json

DATABASE_URL = 'sqlite+pysqlite:///brazil_oil_production.sqlite'

engine = create_engine(DATABASE_URL, echo=True)
metadata_obj = MetaData()

production = Table("production", metadata_obj, Column('Oil (m³)', Float),
                    Column('Condensate oil (m³)', Float), 
                    autoload_with=engine)

stmt = select(production.columns["Field"],
              production.columns["Basin"],
              production.columns["Installation"],
              production.columns["Oil (m³)"],
              production.columns["Condensate oil (m³)"],
              production.columns["Associated petroleum gas (Mm³)"],
              production.columns["Non-associated petroleum gas (Mm³)"],
              production.columns["Water (m³)"],
              production.columns["Gas injection (Mm³)"],
              production.columns["Secondary recovery water injection (m³)"],
              production.columns["Wastewater injection (m³)"],
              production.columns["CO2 injection (Mm³)"],
              production.columns["Nitrogen injection (Mm³)"],
              production.columns["Steam injection (t)"],
              production.columns["Polymer injection (m³)"],
              production.columns["Others fluids injection (m³)"]).where(production.c.State == "PB")

with engine.connect() as conn:
    dict_list = []
    for row in conn.execute(stmt).all():
        dict = row._mapping
        dict_list.append(dict)

    print(dict_list)