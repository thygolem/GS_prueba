from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.dbConfig import meta, engine

fridges = Table("fridges", meta, Column("id", Integer, primary_key=True),
                                Column("timestamp", String(10)),
                                Column("chillerStatus", Integer), 
                                Column("temperature", Float(5)), 
                                Column("humidity", Float(5)),
                                Column("power", Float(5)))

meta.create_all(engine)
