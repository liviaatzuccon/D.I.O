frutas = ("Laranja", "pera", "uva",)
#ou
#letras = tuple("python")
#ou
#numeros = tuple([1, 3, 4, 2])
#OU
#pais = ("Brasil",)

print(frutas) #>>>("laranja", "pera", "uva")

    #acesso direto
print(frutas[0]) #>>>laranja

    #indices negativos
print(frutas[1]) #>>>pera

    #tuplas aninhadas
tupla = (
    (1, 2, 3),
    ("b", 3, 4),
    (6, 5, "c")
)
print(tupla[0]) #>>>(1, 2, 3)
print(tupla[0][0]) #>>>1
print(tupla[0][-1]) #>>>3
print(tupla[-1][-1]) #>>>c

    #fatiamento
tupla = ("p", "y", "t", "h", "o", "n")
print(tupla[2:]) #>>>('t', 'h', 'o', 'n')
print(tupla[:2]) #>>>('p', 'y')
print(tupla[1:3]) #>>>('y', 't')
print(tupla[0:3:2]) #>>>('p', 't')
print(tupla[::]) #>>>('p', 'y', 't', 'h', 'o', 'n')
print(tupla[::-1]) #>>>('n', 'o', 'h', 't', 'y', 'p')

    #enumerate
carros = ("gol", "celta", "palio")
for indice, carro in enumerate(carros):
    print(f"{indice}: {carros}")
#0: ('gol', 'celta', 'palio')
#1: ('gol', 'celta', 'palio')
#2: ('gol', 'celta', 'palio')

    #interar
carros = ("gol", "celta", "palio")
for carro in carros:
    print(carro)
    
    ##Métodos da classe tuple
    
    #().count
cores = ("vermelho", "azul", "verde", "azul")
print(cores.count("vermelho")) #>>>1
print(cores.count("azul")) #>>>2
print(cores.count("verde")) #>>>1

    #().index
linguagens = ("py", "c", "java")
print(linguagens.index("java")) #>>>2
print(linguagens.index("py")) 0

    #len
linguagens = ("py", "c", "java")
print(linguagens.index("py")) 
print(len(linguagens)) #>>>3