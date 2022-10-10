

import unittest

from clase import Ropa

class TestRopa(unittest.TestCase):

    def setUp(self):
        self.ropa = Ropa()

    #PARA CADA PRUEBA SE LLAMA EL MEOTODO DESCUENTO Y SE LE DA DE ENTRADA 2 VALORES, EL COSTO Y SI ES DE TEMPORADA O NO, 
    # SE REVISA QUE EL RESULTADO CORRESPONDA AL DESCUENTO QUE RETORNA LA FUNCION

    def test_ropaFueraTemporada_menor500(self):
        self.assertEqual(self.ropa.descuento(499,'fueraDeTemporada'),10)


    def test_ropaFueraTemporada_mayor500_menor5000(self):
        self.assertEqual(self.ropa.descuento(500,'fueraDeTemporada'),20)


    def test_ropaTemporada_menor1000(self):
        self.assertEqual(self.ropa.descuento(999,'temporada'),5)


    def test_ropaTemporada_mayor1000_menor6000(self):
        self.assertEqual(self.ropa.descuento(1000,'temporada'),10)

if __name__ == "__main__":
    
    unittest.main()