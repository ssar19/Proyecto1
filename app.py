import os
from dataclasses import dataclass, asdict
from pymongo.mongo_client import MongoClient 
from pymongo.server_api import ServerApi
from dotenv import load_dotenv


load_dotenv()

URI = os.getenv("URI")


@dataclass
class Person:
    capital: str
    name: str
    codigo: str
    
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
    
    p = Person( "Ankara", "Turquia", "TUR" )
    
    id = p.save(coll) 
    
    print(id)
    
if __name__ == "__main__":
        main()
        
