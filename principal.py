

import unittest

from clase import Ropa

class TestRopa(unittest.TestCase):

    def setUp(self):
        self.ropa = Ropa()

    def test_ropa(self):
        self.assertEqual(self.ropa.descuento(7,'fueraDeTemporada'),'hola')

if __name__ == "__main__":
    
    unittest.main()