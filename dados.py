'''

class Carro(object):
    estado = 'novo'
    
fusca = Carro()
fusca.estado ='novo'

ferrari = Carro()
ferrari.estado = 'usado'

print(fusca.estado)
print(ferrari.estado)
print(type(fusca))
print(ferrari)

class ControleRemoto:
    def __init__(self,cor,marca,volume): #metodo
        self.cor = cor
        self.marca = marca
        self.volume = volume
        
controle_remoto = ControleRemoto("preto","LG",10)
print(controle_remoto.cor)

questão 1

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        
p1 = Pessoa ("bryan")
p2 = Pessoa("elisa")
print(p1.nome)
print(p2.nome)

questão 2
 
class animal:
    def __init__(self, tipo):
        self.tipo = tipo
    
a1 = animal("cachorro")
a2 = animal("gato")
print(a1.tipo)
print(a2.tipo)

questão 3

class carro:
     def __init__(self, nome ,estado= "novo"):
         self.nome = nome
         self.estado = estado
         
fusca = carro("fusca")
ferrari = carro ("ferrari")
ferrari.estado = "usado"

print(f"{fusca.nome}: {fusca.estado}")
print(f"{ferrari.nome}: {ferrari.estado}")

questão 4

class carro:
     def __init__(self, nome ,cor):
         self.nome = nome
         self.cor = cor
         
fusca = carro ("fusca","azul")
ferrari = carro ("ferrari","vermelha")

print(f"{fusca.nome} - {fusca.cor}")
print(f"{ferrari.nome} - {ferrari.cor}")

questão 5

class aluno:
     def __init__(self, nome ,nota):
         self.nome = nome
         self.nota = nota
         
nome = input("digite o nome do aluno:")
nota = float(input("digite a nota do aluno:"))

aluno = aluno(nome, nota)
print(f"aluno: {aluno.nome},nota: {aluno.nota}")

questão 6

class ContaBancaria:
    def __init__ (self, saldo):
     self.saldo = saldo
     
c1 = ContaBancaria(1000)
c2 = ContaBancaria(500)

print(c1.saldo)
print(c2.saldo)

questão 7

class ContaBancaria:
    def __init__ (self, saldo):
     self.saldo = saldo
     
     def mostra_saldo(self):
         print(f"saldo: R${self.saldo}")
     
c1 = ContaBancaria(1000)
c2 = ContaBancaria(500)

c1.mostrar_saldo()
c2.mostrar_saldo()

questão 8'''

class Produto:
    def __init__(self, preço, nome):
        self.preço = preço
        self.nome = nome
        
c1 = Produto("garrafinha",20,00)
c2 = Produto("computador",1.000)
c3 = Produto("celular",800,00)
