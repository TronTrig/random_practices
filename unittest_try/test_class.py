import unittest
from .main_class import Abuelito

class TestAbuelito(unittest.TestCase):

    def setUp(self):
        self.Abuelito = Abuelito()

    def test_come(self):
        self.Abuelito.come('atún')
        self.assertEqual(self.Abuelito.esta_digiriendo(), 'Silencio')

    def test_esta_digiriendo(self):
        self.assertEqual(self.Abuelito.esta_digiriendo(), 'Gruñe')

    def test_vomita(self):
        self.Abuelito.come('Fruta')
        self.Abuelito.vomita()
        self.assertEqual(self.Abuelito.esta_digiriendo(), 'Gruñe')

    def test_vomita_sin_comer(self):
        with self.assertRaises(IndexError):
            self.Abuelito.vomita()

    def test_disculparse_con_abuelito(self):
        self.assertEqual('Perdón abuelito', 'Perdón abuelito')

if __name__ == '__main__':
    unittest.main()
