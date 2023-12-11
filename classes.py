from datetime import date


class Funcionario():
    def __init__(self, nome, nascimento, salario):
        self._nome = nome
        self._nascimento = nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome
    
    @property
    def salario(self):
        return self._salario
    
    def idade(self):
        data_usuario = self._nascimento.split('/')
        ano_usuario = data_usuario[-1]

        ano_atual = date.today().year
        return ano_atual - int(ano_usuario)
    

    def sobrenome(self):
        sobrenome = self._nome.strip().split(' ')[-1]
        return sobrenome
    

    def calcular_bonus(self):
        valor = self._salario * 0.1
        
        if valor > 1000:
            raise Exception('Salário alto demais para ser bonificado.')
        
        return valor
    

    def decrescimo_salario(self):
        sobrenomes = ['Hoppus', 'Falcão', 'Albuquerque']

        if self.sobrenome() in sobrenomes and self._salario >= 100000:
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo

        return self._salario
    
    
    def __str__(self):
        return f'Funcionario: ({self._nome}, {self._nascimento}, {self._salario})'