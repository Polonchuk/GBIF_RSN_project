from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from db import Base, engine

class Info_source(Base):
    __tablename__ = 'info_sources'
    id = Column(Integer, primary_key=True)
    alias = Column(String)
    full_name = Column(String)
    occurrences = relationship('Herb_occurrence', back_populates='source')

    def __repr__(self):
        return f'<Info source id: {self.id}, name: {self.full_name}>'

class Herb_species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    scientific_name = Column(String)
    Full_name = Column(String)
    genus = Column(String)
    status = Column(String)
    occurrences = relationship('Herb_occurrence', back_populates='species')

    def __repr__(self):
        return f'<Species id: {self.id}, species name: {self.scientific_name}>'

class Herb_occurrence(Base):
    __tablename__ = 'herb_occurrences'
    id = Column(Integer, primary_key=True)
    scientific_name_id = Column(Integer, ForeignKey(Herb_species.id), index=True, nullable=False)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    region = Column(String, index=True)
    year = Column(Integer)
    source_id = Column(Integer, ForeignKey(Info_source.id), index=True, nullable=False)
    source = relationship('Info_source', back_populates='occurrences', lazy='joined')
    species = relationship('Herb_species', back_populates='occurrences', lazy='joined')


    def __repr__(self):
        return f'<Occurrence id: {self.id}, species: {Herb_species.query.get(self.scientific_name_id).scientific_name}, region: {self.region}, info from {Info_source.query.get(self.source_id).alias}>'

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)