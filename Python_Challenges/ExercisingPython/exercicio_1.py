Question = """ 

Exercício de Python - POO - Programação Orientada a Objetos - 
Uma classe para representar uma pessoa, com os atributos privados de nome, data de nascimento e altura

Missão:
Crie uma classe para representar uma pessoa, com os atributos privados de nome, data de nascimento e altura. 
Crie os métodos públicos necessários para sets e gets e também um método para imprimir todos dados de uma pessoa. 
Crie um método para calcular a idade da pessoa.

A data de nascimento pode ser informada como uma String (no formato 05/10/1982, por exemplo) e, no cálculo da idade, 
considere apenas o ano da data de nascimento informada.

Sua saída deverá ser parecida com:
Nome: Amanda Rodrigues
Data de Nascimento: 12/03/1972
Altura: 1.65
A pessoa tem 49 anos

"""


### Codigo

from datetime import date
class Pessoa:
    
    def __init__(self, nome, nascimento, altura):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__altura = altura
    
    #get_name
    @property
    def nome(self):
        return self.__nome
    #get_nascimento    
    @property
    def nascimento(self):
        return self.__nascimento
        
    #get_altura    
    @property
    def altura(self):
        return self.__altura
    
    #set_nome    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    #set_nascimento    
    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento
        
    #set_altura
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
        
    #Metodo para calcular a idade da pessoa
    def idade(self):
        dataNascimento = self.nascimento
        anoNascimento = int(dataNascimento[6:10])
        return anoNascimento
        
    
    #Metodo para imprimir todas as informacoes da pessoa
    def exibeDados(self):
        anoNascimento = self.idade()
        current_year = date.today().year
        idade = current_year - anoNascimento
        print(f"Nome: {self.__nome}")
        print(f"Data de Nascimento: {self.__nascimento}")
        print(f"Altura: {self.__altura}")
        print(f"Idade: Essa pessoa tem {idade} anos")
    

pessoa = Pessoa("Carlos", "23/12/1970", 1.70)

pessoa.exibeDados()

