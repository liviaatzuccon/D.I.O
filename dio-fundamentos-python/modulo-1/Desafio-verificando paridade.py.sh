#Desafio - verificando paridade
Descrição
Neste desafio, você deve escreva uma solução que receba um número inteiro como entrada e determine se ele é par ou ímpar. Dessa forma, a solução deve retornar uma string indicando Par se o número for par e Ímpar se o número for ímpar.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/controlflow.html

Entrada
A entrada do programa é um único número inteiro.

Saída
A saída do programa é uma string que será Par se o número for par e Ímpar se o número for ímpar.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

##Código
# Função para verificar se o número é par ou ímpar
def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# Solicita ao usuário que digite um número e remove qualquer espaço extra
numero = int(input().strip())

# Imprime o resultado, que é "Par" ou "Ímpar"
print(verificar_par_ou_impar(numero))