import unittest
import two_classes


class TestAppartement(unittest.TestCase):
	appartTest=two_classes.appartement(100,4,150000)
	appartTest.garage(1)
	appartTest.numero_Etage(5)

	appartTest.avoirGarage()
	appartTest.superficieParPiece()


	def test_garage(self):
		self.assertTrue(self.appartTest.avoirGarage,"Cet appartement devrait avoir un garage")

	def test_supParPiece(self):
		self.assertEqual(self.appartTest.superficieParPiece(),25, "should be 20")

	def test_etage(self):
		self.assertEqual(self.appartTest.numeroEtage,5, "should be 5")

	def test_valgarage(self):
		self.assertEqual(self.appartTest.garage,1,"should be 1")

if __name__ == '__main__':
	unittest.main()
