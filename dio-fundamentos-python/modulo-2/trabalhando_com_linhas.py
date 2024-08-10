#####Criando uma lista
frutas = ["laranja", "maca", "uva"]
print(frutas)

#Acesso direto
print(frutas[0])
print(frutas[2]) 

#Exemplos de criando uma lista
frutas = []
print(frutas)

letras = list("Python")
print(letras)

numero = list(range(10))
print(numero)

carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]
print(carro)

#Linhas aninhadas
matriz = [
    [1, "a", 2],
    ["B", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])

#índices negativos
print(matriz[-1][-1])

#Fatiamento
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print( lista[::-1])

#Acessar listas
carros =  ["gol", "celta", "palio"]

for carro in carros:
    print(carro)
    
#Função enumerate
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#Comprensao de lista
    #filtro versao 1
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []
   
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print("Pares:", pares)
        
    #filtro versao 2 - mais facil
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print("Pares:", pares)

    #modificando valores - versao 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
print("Quadrados:", quadrado)

    #modificando valores - versao 2
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print("Quadrados:", quadrado)

#####Métodos  da classe list

    # {}.append 
    
lista = ["Python"]
lista.append([1]) 
print(lista) #>>>1

    #[].clear
lista = [1, "pYTHON"]
lista.clear()
print(lista) #>>>[]

    #[].copy
lista = [1, 2, 3]
l2 = lista.copy()
print(id(l2), id(lista)) #>>>1894758673472 1894762115520

    #[].count
cores = ["vermelho", "verde", "amarelo"]
print(cores.count("vermelho")) #>>>1

    #[].extend
linguagens = ["py", "js", "c"]
linguagens.extend(["JAVA", "CS"])
print(linguagens) #>>>['py', 'js', 'c', 'JAVA', 'CS']

    #[].index
linguagens = ["py", "js", "c", "js"]
print(linguagens.index("js")) #>>>1

    #[].pop
linguagens = ["py", "js", "c", "js"]
print(linguagens.pop()) #>>>js
print(linguagens.pop()) #>>>c
print(linguagens.pop()) #>>>js

    #[].reverse
linguagens = ["py", "js", "c", "js"]
print(linguagens.reverse)

    #[].remove
linguagens = ["py", "js", "c", "js"]
linguagens.remove("c")
print(linguagens) #>>>['py', 'js', 'js']

    #[].sort
linguagens = ["py", "js", "c", "js"]
linguagens.sort()
print(linguagens) #>>>['c', 'js', 'js', 'py']

linguagens.sort(reverse=True)
print(linguagens) #>>>['py', 'js', 'js', 'c']

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens) #>>>['py', 'js', 'js', 'c']

linguagens.sort(key=lambda x: len(x))
print(linguagens) #>>>['c', 'py', 'js', 'js']

    #len
linguagens = ["py", "js", "c", "js"]
print(len(linguagens)) #>>>4