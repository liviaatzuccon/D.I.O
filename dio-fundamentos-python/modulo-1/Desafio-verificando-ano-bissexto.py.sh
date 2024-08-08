#Desafio - Verificador de Ano Bissexto
Descrição
Escreva uma solução que informe se um determinado ano é bissexto. Um ano é considerado bissexto se ele for divisível por 4. No entanto, anos que são divisíveis por 100 não são bissextos, a menos que também sejam divisíveis por 400. Esta regra é usada para corrigir o calendário, de modo que ele fique em conformidade com o ano solar.

REGRA:

Um ano é bissexto se:
1. Ele é divisível por 4 e não é divisível por 100.
2. Ou ele é divisível por 400.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/controlflow.html

Entrada
O programa deve receber um número inteiro que representa o ano a ser verificado.

Saída
O programa deve imprimir SIM se o ano for bissexto, ou NÃO se não for bissexto.


##CODIGO
def verificar_ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return "SIM"
    else:
        return "NÃO"

ano = int(input().strip())

print(verificar_ano_bissexto(ano))


