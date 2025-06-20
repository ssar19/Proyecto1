import unittest
from mi_modelo import hon_presi, sui_presi, aus_presi, arg_presi, chi_presi, bul_presi

class TestMiModelo(unittest.TestCase):
    
    
    def presidencia_hon(self):
        hon_presi.nombre = "Xiomara Castro"
        self.assertEqual(hon_presi.nombre, "Xiomara Castro")
        
    def presidencia_sui(self):
        sui_presi.nombre = "Karin Kelle"
        self.assertEqual(sui_presi.nombre, "Karin Kelle")
        
    def presidencia_aus(self):
        aus_presi.nombre = "Anthony Albanese"
        self.assertEqual(aus_presi.nombre, "Anthony Albanese")
        
    def presidencia_arg(self):
        arg_presi.nombre = "Javier Milei"
        self.assertEqual(arg_presi.nombre, "Javier Milei")
        
    def presidencia_chi(self):
        chi_presi.nombre = "Níkos Christodoulídis"
        self.assertEqual(chi_presi.nombre, "Níkos Christodoulídis")
        
    def presidencia_bul(self):
        bul_presi.nombre = "Rumen Radev"
        self.assertEqual(bul_presi.nombre, "Rumen Radev")
    
# Otra forma de hacerlo?
    
    def hon_presi(self):
 # Casos donde a debería retornar True
        self.assertTrue(hon_presi("Xiomara Castro", "Honduras")) 
 # Casos donde debería retornar False
        self.assertFalse(hon_presi("Karin Kelle", "Honduras"))
        self.assertFalse(hon_presi("Anthony Albanese", "Honduras"))
        self.assertFalse(hon_presi("Javier Milei", "Honduras"))
        self.assertFalse(hon_presi("Níkos Christodoulídis", "Honduras"))
        self.assertFalse(hon_presi("Rumen Radev", "Honduras"))
    
    def sui_presi(self):
 # Casos donde a debería retornar True
        self.assertTrue(sui_presi("Karin Kelle", "Suiza")) 
 # Casos donde debería retornar False
        self.assertFalse(sui_presi("Xiomara Castro", "Suiza"))
        self.assertFalse(sui_presi("Anthony Albanese", "Suiza"))
        self.assertFalse(sui_presi("Javier Milei", "Suiza"))
        self.assertFalse(sui_presi("Níkos Christodoulídis", "Suiza"))
        self.assertFalse(sui_presi("Rumen Radev", "Suiza"))
    
    def aus_presi(self):
 # Casos donde a debería retornar True
        self.assertTrue(aus_presi("Anthony Albanese", "Australia")) 
 # Casos donde debería retornar False
        self.assertFalse(aus_presi("Xiomara Castro", "Australia"))
        self.assertFalse(aus_presi("Karin Kelle", "Australia"))
        self.assertFalse(aus_presi("Javier Milei", "Australia"))
        self.assertFalse(aus_presi("Níkos Christodoulídis", "Australia"))
        self.assertFalse(aus_presi("Rumen Radev", "Australia"))
    
    def arg_presi(self):
 # Casos donde a debería retornar True
        self.assertTrue(arg_presi("Javier Milei", "Argentina")) 
 # Casos donde debería retornar False
        self.assertFalse(arg_presi("Xiomara Castro", "Argentina"))
        self.assertFalse(arg_presi("Karin Kelle", "Argentina"))
        self.assertFalse(arg_presi("Anthony Albanese", "Argentina"))
        self.assertFalse(arg_presi("Níkos Christodoulídis", "Argentina"))
        self.assertFalse(arg_presi("Rumen Radev", "Argentina"))
    
    def chi_presi(self):
 # Casos donde a debería retornar True
        self.assertTrue(chi_presi("Níkos Christodoulídis", "Chipre")) 
 # Casos donde debería retornar False
        self.assertFalse(chi_presi("Xiomara Castro", "Chipre"))
        self.assertFalse(chi_presi("Karin Kelle", "Chipre"))
        self.assertFalse(chi_presi("Anthony Albanese", "Chipre"))
        self.assertFalse(chi_presi("Javier Milei", "Chipre"))
        self.assertFalse(chi_presi("Rumen Radev", "Chipre"))
        
    def bul_presi(self):
 # Casos donde a debería retornar True
        self.assertTrue(bul_presi("Rumen Radev", "Bulgaria")) 
 # Casos donde debería retornar False
        self.assertFalse(bul_presi("Xiomara Castro", "Bulgaria"))
        self.assertFalse(bul_presi("Karin Kelle", "Bulgaria"))
        self.assertFalse(bul_presi("Anthony Albanese", "Bulgaria"))
        self.assertFalse(bul_presi("Javier Milei", "Bulgaria"))
        self.assertFalse(bul_presi("Níkos Christodoulídis", "Bulgaria"))    




if __name__ == '__main__':
 unittest.main()
 
 
 
       