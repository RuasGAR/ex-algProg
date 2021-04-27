""" Um número palíndromo é um número natural cuja sequência de dígitos (base 10) é a mesma quando lidos da esquerda para a direita ou da direita para a esquerda. Assim, 12321 é um número palíndromo. Embora a maior parte dos números naturais não seja palíndromo, muitos deles podem gerar palíndromos pelo processo de soma com o número formado pelos seus dígitos lidos da direita para a esquerda. Por exemplo, 47 somado com seu reverso 74 dá 121, que é palíndromo. Mesmo que um palíndromo não seja gerado na primeira tentativa, pode-se repetir o processo várias vezes até resultar num palíndromo. Por exemplo:

349 + 943 = 1292,

1292 + 2921 = 4213

4213 + 3124 = 7337

Um número que nunca resulta num palíndromo usando este processo é chamado de número de Lychrel. Por exemplo, acredita-se que o número 196 seja um número de Lychrel. Escreva a função fatorLychrel que retorna o número de iterações do processo descrito acima que é necessário aplicar a n para resultar num palíndromo. Você pode assumir que 50 iterações são suficientes para resultar num palíndromo, caso contrário n pode ser considerado um número de Lychrel, e a função retorna -1. Por exemplo, fatorLychrel(47) retorna 1,  fatorLychrel(349) retorna 3, e  fatorLychrel(196) retorna -1.

Input: Leia um único inteiro positivo

Output: resultado da função """

n = int(input());


def fatorLychrel(n,counter):

    n = str(n);
    
    if(counter == 50):
        return -1;
    
    if(n == n[::-1]):
        return counter;
    else:
        return fatorLychrel(int(n) + int(n[::-1]), counter+1);

print(fatorLychrel(n,0));