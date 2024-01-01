import numpy as np
import sqlalchemy
from faker import Faker

# Use psycopg2 as the PostgreSQL adapter
from sqlalchemy.dialects.postgresql import psycopg2

# Change here: Use Table, Column, Integer, String, MetaData, Date, ForeignKey from sqlalchemy.dialects.postgresql
from sqlalchemy import Table, Column, Integer, String, MetaData, Date, ForeignKey

class SQLData:
    def __init__(self, server: str, db: str, uid: str, pwd: str):
        self.__fake = Faker()
        self.__server = server
        self.__db = db
        self.__uid = uid
        self.__pwd = pwd
        self.__tables = dict()

    def connect(self):
        # Change here: Use 'postgresql+psycopg2' instead of 'mysql+pymysql'
        self.__engine = sqlalchemy.create_engine(
            f"postgresql+psycopg2://{self.__uid}:{self.__pwd}@{self.__server}/{self.__db}"
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

        # for _ in range(100):
        #     jobs_ins.append({'description': self.__fake.job()})
        for _ in range(100):
            record = dict()
            record['description'] = self.__fake.job()
            jobs_ins.append(record)
        # print("Jobs data:", jobs_ins)

        for _ in range(100):
            companies_ins.append({
                'name': self.__fake.company(),
                'phrase': self.__fake.catch_phrase(),
                'address': self.__fake.street_address(),
                'country': self.__fake.country(),
                'est_date': self.__fake.date_of_birth(),
            })
        print(companies_ins)

        for _ in range(500):
            persons_ins.append({
                'job_id': np.random.randint(1, 100),
                'company_id': np.random.randint(1, 100),
                'last_name': self.__fake.last_name(),
                'first_name': self.__fake.first_name(),
                'date_of_birth': self.__fake.date_of_birth(),
                'address': self.__fake.street_address(),
                'country': self.__fake.country(),
                'zipcode': self.__fake.zipcode(),
                'salary': np.random.randint(60000, 150000),
            })

        self.__conn.execute(self.__tables['jobs'].insert().values(jobs_ins))
        self.__conn.execute(self.__tables['companies'].insert().values(companies_ins))
        self.__conn.execute(self.__tables['persons'].insert().values(persons_ins))
    
        self.__conn.commit()


if __name__ == '__main__':
    sql = SQLData('localhost', 'practice_db', 'postgres', 'globular')
    sql.connect()
    sql.create_tables()
    sql.populate_tables()

        
