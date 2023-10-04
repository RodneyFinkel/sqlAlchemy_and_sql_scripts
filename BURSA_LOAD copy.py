import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Numeric, Integer, NVARCHAR, VARCHAR
import pyodbc
import pandas as pd

# server = 'ILTLVPOALIMSQL'
# database = 'Bursa_2022'
server ='USTLVRFINKEL1\DA'
database = 'DA4OPS_Temp'
driver = 'ODBC Driver 17 for SQL Server'
Database_Con = f'mssql+pyodbc://@{server}/{database}?driver={driver}'
engine = create_engine(Database_Con, echo=True)
meta = MetaData()

BURSA_2022_ALCHEMY999 = Table('BURSA_2022_ALCHEMY_1983', meta, 
    Column('מס גיליון', NVARCHAR,),
    Column('ת.סליקה', NVARCHAR),
    Column('סוג פעולה', NVARCHAR),
    Column('שם סוג פעולה', NVARCHAR),
    Column('קבוצה', NVARCHAR),
    Column('שם קבוצה', NVARCHAR),
    Column('מס נייר', NVARCHAR),
    Column('שם נייר', NVARCHAR),
    Column('סוג נייר', NVARCHAR),
    Column('תת סוג נייר', NVARCHAR),
    Column('כמות', NVARCHAR),
    Column('שער', NVARCHAR),
    Column('תמורה כספית', NVARCHAR),
    Column('חשבון', NVARCHAR),
    Column('אסמכתה', NVARCHAR),
    Column('עמלה', VARCHAR(53)),
)

meta.create_all(engine)
data = pd.read_csv(r'C:\Users\rfinkel\Desktop\BURSA FILES\mechaser_slika_again\4_combined.csv', 
        skiprows=1, sep=',', encoding = "iso8859-8", low_memory=False)
df = pd.DataFrame(data)

engine = create_engine(Database_Con, encoding='iso8859-8', echo=False)
con = engine.connect()

df.to_sql('BURSA_2022_ALCHEMY_4combined', con=engine, if_exists='append', chunksize=8000)   