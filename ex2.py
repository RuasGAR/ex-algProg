""" Implementar o produto interno de dois vetores.

Ler dois vetores.  (dimensão máxima =4 e coordenadas são inteiras)

Imprimir o resultado do produto interno. (inteiro)

Exemplos:

Input: [2] [3] Output: 6

Input: [2,3] [2,3] Output: 13
Input: [1,1,1,1] [2,2,2,2] Output: 8

Obs: Faça duas leituras, uma para cada vetor """

array1 = eval(input());
array2 = eval(input());

def times(a, b):
    return a * b

def inner_product(l1,l2):
    if (len(l1) <= 4 and len(l1) == len(l2)): 
        accumulator = 0;
        for i in range (0, len(l1)):
            accumulator += times(l1[i],l2[i]);
        return int(accumulator);
    else:
        pass    

print(inner_product(array1, array2));