import os
from dataclasses import asdict
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

URI = os.getenv("URI")


class Pais:
    def __init__(self, nombre:str, codigo:str, capital:str, idioma:str):
        self.nombre = nombre
        self.codigo = codigo
        self.capital = capital
        self.idioma = idioma
        self.presidente_al_mando = None
        
        
        def __str__( self ):
            return(f"Pais: {self.nombre}, {self.codigo}, {self.capital}, {self.idioma}") 
        
        def save(self, coll):
             return str( coll.insert_one( asdict(self) ).inserted_id ) 
    
        def get_collection( uri, db="demo_db", col="paises" ):
            client = MongoClient(
                uri
                , server_api = ServerApi("1")
                , tls = True
                , tlsAllowInvalidCertificates = True
            )
    
            client.admin.command("ping")
            
            return client[db][col]

        def main():
    
            coll = get_collection(URI)
    
            p = Pais( "Honduras", "HND", "Tegucigalpa", "Español" )
            
            id = p.save(coll) 
    
    print(id)
  