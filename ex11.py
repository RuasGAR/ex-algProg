""" A série descoberta por Leibniz para computar o arco tangente é 

Se usarmos x=1
, podemos computar uma aproximação para π/4

.

Faça uma função que receba x e n, onde n é o numero de termos da serie e retorna o valor da serie.

Input: são dois inputs. O primeiro recebe um float e o segundo recebe um inteiro positivo

Output: saída da função """

x = float(input());
n = int(input());


def serie(x, n):
    arctan = x;

    if (n == 2):
        arctan += ((-x)**3)/3;
    else:
        for i in range(1, n, 2):
            arctan += ((-x)**i)/i;
    return arctan;


print(serie(x, n));