#Desafio - Contagem de Vogais
Descrição
Neste desafio, implemente uma solução para completar a função conta_vogais que conta o número de vogais em uma string fornecida como entrada. Vogais são caracteres específicos sem acentuação, incluindo tanto letras minúsculas quanto maiúsculas (aeiouAEIOU).

Para resolver este desafio, siga os passos abaixo:

1. Defina um conjunto de vogais: Primeiramente, crie um conjunto contendo todas as vogais sem acentuação, incluindo tanto letras minúsculas quanto maiúsculas.

2. Inicialize um contador: Em seguida, crie uma variável para contar o número de vogais encontradas na string, começando com zero.

3. Itere pelos caracteres da string: Aqui percorremos cada caractere na string de entrada para verificar se é uma vogal.

4. Verifique se o caractere é uma vogal: Para cada caractere, verifique se ele está presente no conjunto de vogais definido no passo 1. Se o caractere for uma vogal, incremente o contador em 1.

5. Retorne o contador: Após percorrer todos os caracteres da string, retorne o valor do contador, que representa o número total de vogais na string.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/controlflow.html#for-statements

Entrada
A função recebe como entrada uma única string contendo letras/palavras.

Saída
A função deve retornar um número inteiro que representa o total de vogais encontradas na string de entrada.

#Código

def conta_vogais(s):
    # Define um conjunto contendo todas as vogais minúsculas e maiúsculas
    vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    # Inicializa o contador de vogais
    contador_vogais = 0
    
    # Itera pelos caracteres da string
    for caractere in s:
        # Verifica se o caractere é uma vogal
        if caractere in vogais:
            contador_vogais += 1
    
    # Retorna o número total de vogais encontradas
    return contador_vogais

# Solicitamos ao usuário que insira uma string
texto = input()

# Chamamos a função conta_vogais e exibimos o resultado no formato esperado
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")

