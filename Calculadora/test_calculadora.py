import unittest
from calculadora import Calculadora

class testCalculadora(unittest.TestCase):

    def testSoma1(self):
        entrada = Calculadora().somar(x=1, y=2)
        esperado = 3

        return self.assertEqual(
            entrada, 
            esperado
            )

    def testSoma2(self):
        entrada = Calculadora().somar(x=5, y=6)
        esperado = 11

        return self.assertEqual(
            entrada, 
            esperado
            )

    def testSoma3(self):
        entrada = Calculadora().somar(x=10, y=6)
        esperado = 16

        return self.assertEqual(
            entrada, 
            esperado
            )
    
    def testSub1(self):
        entrada = Calculadora().subtrair(x=10, y=5)
        esperado = 5

        return self.assertEqual(
            entrada, 
            esperado
            )

    def testSub2(self):
        entrada = Calculadora().subtrair(x=15, y=5)
        esperado = 10

        return self.assertEqual(
            entrada, 
            esperado
            )

    def testSub3(self):
        entrada = Calculadora().subtrair(x=20, y=5)
        esperado = 15

        return self.assertEqual(
            entrada, 
            esperado
            )

    def testMult1(self):
        entrada = Calculadora().multiplicar(x=5, y=5)
        esperado = 25

        return self.assertEqual(
            entrada, 
            esperado
            )

    def testMult2(self):
        entrada = Calculadora().multiplicar(x=20, y=5)
        esperado = 100

        return self.assertEqual(
            entrada, 
            esperado
            )    

    def testMult3(self):
        entrada = Calculadora().multiplicar(x=12, y=5)
        esperado = 60

        return self.assertEqual(
            entrada, 
            esperado
            )        

    def testDiv1(self):
        entrada = Calculadora().divisao(x=10, y=5)
        esperado = 2

        return self.assertEqual(
            entrada, 
            esperado
            )  

    def testDiv2(self):
        entrada = Calculadora().divisao(x=20, y=5)
        esperado = 4

        return self.assertEqual(
            entrada, 
            esperado
            )  
    
    def testDiv3(self):
        entrada = Calculadora().divisao(x=20, y=0)
        esperado = False

        return self.assertEqual(
            entrada, 
            esperado
            )  