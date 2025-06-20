from classes.pais import Pais
from classes.presidente import Presidente

presi_Honduras = Presidente("Xiomara Castro", 65, "Cafe")
presi_Suiza = Presidente("Karin Keller", 61, "Naranja")
presi_Australia = Presidente("Anthony Albanese", 62, "Azul")
presi_Argentina = Presidente("Javier Milei", 54, "Morado")
presi_Chipre = Presidente("Níkos Christodoulídis", 51, "Rojo")
presi_Bulgaria = Presidente("Rumen Radev", 62, "Verde")


hon = Pais("Honduras", "HND", "Tegucigalpa", "Español")
sui = Pais("Suiza", "CHE", "Berna", "Alemán")
aus = Pais("Australia", "AUS", "Canberra", "Inglés")
arg = Pais("Argentina", "ARG", "Buenos Aires", "Español")
chi = Pais("Chipre", "CYP", "Nicosia", "Griego")
bul = Pais("Bulgaria", "BGR", "Sofía", "Búlgaro")




def hon_presi(presi_Honduras, hon):
    """
    Retorna True si 'presi_Honduras' y 'hon' se igualan, de lo contrario False.
    """
    return presi_Honduras == hon

def sui_presi(presi_Suiza, sui):
    """
    Retorna True si 'presi_Suiza' y 'sui' se igualan, de lo contrario False.
    """
    return presi_Suiza == sui

def aus_presi(presi_Australia, aus):
    """"
    Retorna True si 'presi_Australia' y 'aus' se igualan, de lo contrario False.
    """
    return presi_Australia == aus

def arg_presi(presi_Argentina, arg):
    """
    Retorna True si 'presi_Argentina' y 'arg' se igualan, de lo contrario False.
   """
    return presi_Argentina == arg

def chi_presi(presi_Chipre, chi):
    """
    Retorna True si 'presi_Chipre' y 'chi' se igualan, de lo contrario False.
    """
    return presi_Chipre == chi

def bul_presi(presi_Bulgaria, bul):
    """
    Retorna True si 'presi_Bulgaria' y 'bul' se igualan, de lo contrario False.
    """
    return presi_Bulgaria == bul
    
