import unittest
from empregado import Empregado

class testempregado(unittest.TestCase):

    def testValidarCargoPresidente(self):
        empregado = Empregado(primeiro_nome="lucas", sobrenome="silva", cargo="presidente", salario=1)
        entrada = empregado.validar_cargo()
        esperado = True

        return self.assertEqual(
            entrada, 
            esperado
            )

    def testValidarCargoDiretor(self):
        empregado = Empregado(primeiro_nome="vinicius", sobrenome="augusto", cargo="diretor", salario=2)
        entrada = empregado.validar_cargo()
        esperado = True

        return self.assertEqual(
            entrada, 
            esperado
            )

    def testValidarCargoGerente(self):
        empregado = Empregado(primeiro_nome="lucas", sobrenome="barbi", cargo="gerente", salario=3)
        entrada = empregado.validar_cargo()
        esperado = True

        return self.assertEqual(
            entrada, 
            esperado
            )

    def testValidarCargoAnalista(self):
        empregado = Empregado(primeiro_nome="joao", sobrenome="mathias", cargo="analista", salario=1000)
        entrada = empregado.validar_cargo()
        esperado = True

        return self.assertEqual(
            entrada, 
            esperado
            )

    def testValidarCargoAuxiliar(self):
        empregado = Empregado(primeiro_nome="bini", sobrenome="vin", cargo="auxiliar", salario=10)
        entrada = empregado.validar_cargo()
        esperado = True

        return self.assertEqual(
            entrada, 
            esperado
            )


    def testNomeCompleto1(self):
        empregado = Empregado(primeiro_nome="lucas", sobrenome="silva", cargo="presidente", salario=1)
        entrada = empregado.gerar_nome_completo()
        esperado = "lucassilva"

        return self.assertEqual(
            entrada, 
            esperado
            )

    def testNomeCompleto2(self):
        empregado = Empregado(primeiro_nome="lucas", sobrenome="barbi", cargo="gerente", salario=3)
        entrada = empregado.gerar_nome_completo()
        esperado = "lucasbarbi"

        return self.assertEqual(
            entrada, 
            esperado
            )

    def testNomeCompleto3(self):
        empregado = Empregado(primeiro_nome="joao", sobrenome="mathias", cargo="analista", salario=1000)
        entrada = empregado.gerar_nome_completo()
        esperado = "joaomathias"

        return self.assertEqual(
            entrada, 
            esperado
            )

    def testeReajusteSalarial1(self):
        empregado = Empregado(primeiro_nome="lucas", sobrenome="silva", cargo="presidente", salario=100)
        entrada = empregado.calcular_reajuste()
        esperado = 105

        return self.assertEqual(
            entrada, 
            esperado
            )

    def testeReajusteSalarial2(self):
        empregado = Empregado(primeiro_nome="matheus", sobrenome="araujo", cargo="gerente", salario=200)
        entrada = empregado.calcular_reajuste()
        esperado = 210

        return self.assertEqual(
            entrada, 
            esperado
            )
    
    def testeReajusteSalarial3(self):
        empregado = Empregado(primeiro_nome="bini", sobrenome="luis", cargo="auxiliar", salario=10)
        entrada = empregado.calcular_reajuste()
        esperado = 10.5

        return self.assertEqual(
            entrada, 
            esperado
            )
