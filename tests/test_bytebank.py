from classes import Funcionario

class TestClass:
    def test_calculo_super_especifico(self):
        entrada = '27/02/2000'        
        
        esperado = 23
        #esperado = 28

        my_test = Funcionario('Claudinho', entrada, 777)
        result = my_test.idade()

        assert result == esperado


    def test_retornar_sobrenome_do_bagre(self):
        entrada = 'Yuri Alberto'
        esperado = 'Alberto'

        my_test = Funcionario(entrada, '27/02/2003', 777)
        result = my_test.sobrenome()

        assert result == esperado


    def test_do_descrecimo_salarial(self):
        entrada_nome = 'Mark Hoppus'
        #entrada_salario = 100000
        entrada_salario = 99999
        esperado = 90000

        my_test = Funcionario(entrada_nome, '11/11/2011', entrada_salario)
        result = my_test.decrescimo_salario()

        assert result == esperado