class Empregado:

    def __init__(self, primeiro_nome, sobrenome, cargo, salario, taxa_reajuste=1.05):
        self.nome = primeiro_nome
        self.sobrenome = sobrenome
        self.cargo = cargo
        self.salario = salario
        self.taxa_reajuste = taxa_reajuste

    def calcular_reajuste(self):
        return self.salario * self.taxa_reajuste
        
    def gerar_nome_completo(self):
        return self.nome + self.sobrenome
    
    def validar_cargo(self):
        if self.cargo == "presidente":
            return True
        if self.cargo == "diretor":
            return True
        if self.cargo == "auxiliar":
            return True
        if self.cargo == "gerente":
            return True
        if self.cargo == "analista":
            return True
        