import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = "../database.sqlite" # '../' retrocede una carpeta y crea la BD
# con el nombre de 'database.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__)) # Leo el directorio actual del archivo database.py

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}" # asi creo la url de la bd
# hago un join de base_dir y el sqlite_file_name

engine = create_engine(database_url, echo=True) # motor de la BD, 'echo=True' es para ver los logs
# de cuando se crea la BD

Session = sessionmaker(bind=engine) # creo una 'session' para conectarme a la BD
# 'bind' se conecta al motor de la BD

Base = declarative_base() # Instancia para manejo de tablas de la BD