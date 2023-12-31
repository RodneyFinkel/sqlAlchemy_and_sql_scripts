import os 
from dotenv import load_dotenv
import numpy as np 
import sqlalchemy 
from faker import Faker 


load_dotenv()

# mysqlconnector instead of pymysql line 21/make sure both are pip installed

from sqlalchemy import Table, Column, Integer, String, MetaData, Date, ForeignKey
# Encapsulation suggested through name mangling with use of double underscores __server
# This makes the attributes class level private
class SQLData:
    def __init__(self, server:str, db:str, uid:str, pwd:str):
        self.__fake = Faker()
        self.__server = server
        self.__db = db
        self.__uid = uid
        self.__pwd = pwd
        self.__tables = dict()
        
    def connect(self):
        password = os.environ.get('DB_PASSWORD', self.__pwd)
        self.__engine = sqlalchemy.create_engine(
            f"mysql+pymysql://{self.__uid}:{self.__pwd}@{self.__server}/{self.__db}"
        )
        self.__conn = self.__engine.connect()
        self.__meta = MetaData()
        self.__meta.reflect(bind=self.__engine)
    
    
    def drop_all_tables(self):
        pass
    
    def create_tables(self):
        self.__tables['jobs'] = Table (
            'jobs', self.__meta,
            Column('job_id', Integer, primary_key=True, autoincrement=True, nullable=False),
            Column('description', String(255))
        )

        self.__tables['companies'] = Table(
            'companies', self.__meta, 
            Column('company_id', Integer, primary_key=True, autoincrement=True, nullable=False),
            Column('name', String(255), nullable=False),
            Column('phrase', String(255)),
            Column('address', String(255)),
            Column('country', String(255)),
            Column('est_date', Date)
        )

        self.__tables['persons'] = Table(
            'persons', self.__meta,
            Column('person_id', Integer, primary_key=True, autoincrement=True, nullable=False),
            Column('job_id', Integer, ForeignKey('jobs.job_id'), nullable=False),
            Column('company_id', Integer, ForeignKey('companies.company_id'), nullable=False),
            Column('last_name', String(255), nullable=False),
            Column('first_name', String(255)),
            Column('date_of_birth', Date),
            Column('address', String(255)),
            Column('country', String(255)),
            Column('zipcode', String(10)),
            Column('salary', Integer)
        )

        self.__meta.create_all(bind=self.__engine)
    
    def populate_tables(self):
        jobs_ins = list()
        companies_ins = list()
        persons_ins = list()

        for _ in range(100):
            record = dict()
            record['description'] = self.__fake.job()
            jobs_ins.append(record)
        
        for _ in range(100):
            record = dict()
            record['name'] = self.__fake.company()
            record['phrase'] = self.__fake.catch_phrase()
            record['address'] = self.__fake.street_address()
            record['country'] = self.__fake.country()
            record['est_date'] = self.__fake.date_of_birth()
            companies_ins.append(record)

        for _ in range(500):
            record = dict()
            record['job_id'] = np.random.randint(1, 100)
            record['company_id'] = np.random.randint(1, 100)
            record['last_name'] = self.__fake.last_name()
            record['first_name'] = self.__fake.first_name()
            record['date_of_birth'] = self.__fake.date_of_birth()
            record['address'] = self.__fake.street_address()
            record['country'] = self.__fake.country()
            record['zipcode'] = self.__fake.zipcode()
            record['salary'] = np.random.randint(60000, 150000)
            persons_ins.append(record)
            
        self.__conn.execute(self.__tables['jobs'].insert(), jobs_ins)
        self.__conn.execute(self.__tables['companies'].insert(), companies_ins)
        self.__conn.execute(self.__tables['persons'].insert(), persons_ins)
    
        self.__conn.commit()

    
if __name__ == '__main__':
    sql = SQLData('localhost','practice_db','root','DB_PASSWORD')
    sql.connect()
    sql.create_tables()
    sql.populate_tables()