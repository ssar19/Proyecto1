import os
from dataclasses import asdict
from pymongo.mongo_client import MongoClient 
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

URI = os.getenv("URI")


class Presidente:
    def __init__(self, nombre:str, edad: int, partido:str):
        self.nombre = nombre
        self.edad = edad
        self.partido = partido
        self.pais_gobierno = None
        
    def __str__( self ):
            return(f"Presidente: {self.nombre}, {self.edad}, {self.partido}") 
    
    def pais_mandato(self, pais_name):
        self.pais_gobierno =  pais_name
        print(f"{self.nombre} es presidente(a) de {pais_name.nombre}.")
        
   #     print(f"{self.nombre} de {self.edad} años de edad, es presidente(a) de {pais_name.nombre} y forma parte del partido político {self.partido}. ")
   
    def save(self, coll):
             return str( coll.insert_one( asdict(self) ).inserted_id ) 
    
    def get_collection( uri, db="demo_db", col="presis" ):
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
    
            p = Presidente( "Xiomara Castro", 65, "Cafe")
            
            id = p.save(coll) 
    
    print(id)