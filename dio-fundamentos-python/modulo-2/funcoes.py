def exibir_mensagem():
    print("ola mundo")
    
exibir_mensagem() #>>>ola mundo

def exibir_mensagem_2(nome):
    print(f"seja bem vindo {nome}!")
    
exibir_mensagem_2(nome="Guilherme") #>>>seja bem vindo Guilherme!

def exibir_mensagem_3(nome="Anonimo"):
    print(f"seja bem vindo {nome}")
    
exibir_mensagem_3() #>>>seja bem vindo Anonimo
exibir_mensagem_3(nome="chap") #>>>seja bem vindo chap

    #retornando valores
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero + 1
    return antecessor, sucessor

print(calcular_total([10, 20, 30])) #>>>64
print(retorna_antecessor_e_sucessor(10)) #>>>[9, 11]

    #argumentos nomeados
def salvar_carro(marca, ano, placa):
    print(f"Carro inserido com sucesso {marca}/{ano}/{placa}")  #Carro inserido com sucesso Fiat/1999/ABC-1234
    
salvar_carro("Fiat",  1999, "ABC-1234") 
#ou
salvar_carro(marca="fiat", ano=1999, placa="ABC-1234")
#ou
salvar_carro(**{"marca": "fiat", "ano": 1999, "placa": "ABC-1234"})

    #args e kwargs
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{meta_dados}"
    print(mensagem)
    
exibir_poema("Zen of Python", "Beautiful is better than ugly", autor="Tim Peters", ano=1999)
#Zen of Python
#quebra de linha
#Autor: Tim Peters
#Ano: 1999

    #parametros especiais
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro("Palio", 1999, "ABC-1234", marca="fiat", motor="1.0", combustivel="gasolina") #Palio 1999 ABC-1234 fiat 1.0 gasolina

    #keyword only
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro(modelo="palio", ano=1999, placa="ABC-1234", marca="fiat", motor="1.0", combustivel="gasolina") #palio 1999 ABC-1234 fiat 1.0 gasolina

    #keyword and positional only
def criar_receita(ingrediente, forno, hora, /, *, receita):
    print(ingrediente, forno, hora, receita)

criar_receita("Ovo", "brastemp", "22:00", receita="bolo") #Ovo brastemp 22:00 bolo

    #objeto de 1 classe
def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"o resultado da operacao {a} + {b} = {resultado}")
    
exibir_resultado(10, 10, somar) #o resultado da operacao 10 + 10 = 20

    #escopo local e escopo global
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_bonus(500)
print(salario) #>>>2500


