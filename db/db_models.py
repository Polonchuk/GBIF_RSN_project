from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from db import Base, engine

class Info_source(Base):
    __tablename__ = 'info_sources'
    id = Column(Integer, primary_key=True)
    alias = Column(String)
    full_name = Column(String)

    def __repr__(self):
        return f'<Info source id: {self.id}, name: {self.full_name}>'

class Herb_species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    scientific_name = Column(String)
    Full_name = Column(String)
    genus = Column(String)
    status = Column(String)

    def __repr__(self):
        return f'<Species id: {self.id}, species name: {self.scientific_name}>'

class Herb_occurrence(Base):
    __tablename__ = 'herb_occurrences'
    id = Column(Integer, primary_key=True)
    scientific_name = Column(String, ForeignKey(Herb_species.scientific_name), index=True, nullable=False)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    region = Column(String, index=True)
    year = Column(String)
    source = Column(String, ForeignKey(Info_source.alias), index=True, nullable=False)

    def __repr__(self):
        return f'<Occurrence id: {self.id}, species: {self.scientific_name}, region: {self.region}, info from {self.source_alias}>'

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)