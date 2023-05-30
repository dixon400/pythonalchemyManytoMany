from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

engine = create_engine('sqlite:///freebies.db', echo=True)

Base = declarative_base()

company_dev = Table(
    'company_devs',
    Base.metadata,
    Column('company_id', ForeignKey('companies.id'), primary_key=True),
    Column('dev_id', ForeignKey('devs.id'), primary_key=True),
    extend_existing=True,
)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())
    freebies = relationship('Freebie', backref=backref('company'))
    devs = relationship('Dev', secondary='company_devs', back_populates='companies')


    def __repr__(self):
        return f'<Company id={self.id},{self.name}>' 

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())
    freebies = relationship('Freebie', backref=backref('dev'))
    companies = relationship('Company', secondary='company_devs', back_populates='devs')


    def __repr__(self):
        return f'<Dev {self.name}>'
    
class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name= Column(String())
    value = Column(Integer())
    company_id = Column(Integer(), ForeignKey('companies.id'))
    devs_id = Column(Integer(), ForeignKey('devs.id'))

    def print_details(self):
        dev_name = self.dev.name
        item_name = self.item_name
        company_name = self.company.name
        return f"{dev_name} owns a {item_name} from {company_name}."