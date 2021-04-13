import two_classes
import unittest 

class TestMaison(unittest.TestCase):
	maisonTest= two_classes.maison(300,10,300000)
	maisonTest.jardin(1)
	maisonTest.nbr_Etage(3)
	maisonTest.superficieParEtage()
	maisonTest.avoirJardin()
	def test_avoirJardin(self):
		self.assertTrue(self.maisonTest.avoirJardin, ' Should be True')
	
	def test_Jardin(self):
		self.assertEqual(self.maisonTest.jardin,1, 'Should be 1')

	def test_nbr_Etage(self):
		self.assertEqual(self.maisonTest.nbrEtage,3, 'Should be 3')

	def test_superficieParEtage(self):
		self.assertEqual(self.maisonTest.superficieParEtage, 100,'Should be 150')


if __name__ == '__main__':
	unittest.main()
