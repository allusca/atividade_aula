'''questão 1

for i in range(1, 11):
    print(i)
    
questão 2

for i in range(2,21,2):
    print(i)
    
questão 3

for i in range(1,11):
    print(f"5 x {i} = {5 * i}")
    
questão 4

num = int(input("digite um numero: "))
for i in range(1,11):
    print(f"{num} x {i} ={num * i}")
    
questão 5

soma = 0
for i in range(1, 101):
    soma += i 
print("soma de 1 a 100 =", soma)

questão 6

palavra = input("digite uma palavra: ")
for letra in palavra:
    print(letra)

questão 7

palavra = input("digite uma palavra:")
vogais = "aeiouAEIOU"
cont = 0

for letra in palavra:
    if letra in vogais:
        cont += 1
print("quantidade de vogais:" , cont)

questão 8

soma = 0
for i in range(10):
    num = float(input(f"digite o {i+1} numero: "))
    soma += num
media = soma / 10
print("media =", media)
    
questão 9

num = int(input("digite um numero: "))
fatorial = 1
for i in range(1, num + 1):
    fatorial += i
print(f"o fatorial de {num} é {fatorial}")

questão 10

frase = input("digite uma frase:")
cont = 0
for caractere in frase:
    if caractere == " ":
      cont += 1
print("quantidade de espaços:", cont)

questão 11

nomes = []

for i in range(5):
    nome = input(f"digite o (i+1) nome: ")
    nomes.append(nome)
    
print("nomes em ordem inversa:")
for i in range(4,-1,-1):
    print(nomes[i])
    
questão 12

notas = []
for i in range(5):
    nota = float(input(f"digite a {i+1} nota:"))
    notas.append(nota)
print("maior nota",max(notas))
print("menor nota =",min(notas))

questão 13

for i in range(1,31,2):
    print(i)
    
questão 14

for i in range(1,11):
    print(f"{i} = {i**2}")
    
questão 15

positivos = 0
for i in range(5):
    num = float(input(f"digite o {i+1} numero: "))
    if num > 0:
        positivos += 1
print("quantidade de numeros positivos:", positivos)

questão 16

palavra = input("digite uma palavra:")
invertida = ""
for letra in palavra:
    invertida = letra +invertida
print("palavra invertida:", invertida)

questão 17

for i in range(10):
    num = int(input(f"digite o {i+1} numero:"))
    if num % 2 == 0:
        print(num)
        
questão 18

lista = []

for i in range(10):
    num = int(input(f"digite o {i+1} numero: "))
    lista.append(num)
print("elementos e seus indices: ")
for i in range(len(lista)):
    print(f"indice {i} -> {lista[i]}")
    
questão 19

for i in range(10,0,-1):
    print(i)
    
questão 20

maior = ""
for i in range(5):
    nome = input("nome: ")
    if len(nome) > len(maior): maior = nome
    print("maior nome: ", maior)
    

questão 21'''

print(sum(range(2, 51, 2)))