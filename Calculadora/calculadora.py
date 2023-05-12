class Calculadora:

    @staticmethod
    def somar(x, y):
        return x + y  
        
    @staticmethod
    def subtrair(x, y):
        return x - y

    @staticmethod
    def multiplicar(x, y):
        return x * y

    @staticmethod
    def divisao(x, y):
        if y == 0:
            return False
        else:
            return x/y
