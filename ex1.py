# Leia um número inteiro positivo n.

# Crie uma lista (list) com todos os números primos de 1 a n.
# Transforme essa lista em uma string e imprima a string.

# Ex:

# Input: 1 Output: '[]'

# Input: 5 Output: '[2,3,5]'

n = int(input());
array = [];

def printPrimes(n):
    array = [];
    for i in range(1, n+1):
        # Para cada número gerado, há a necessidade de verificar se ele é divisível por algum outro número ATÉ ele além do próprio.
        # Se chegarmos ao ponto em que o número de referência(i) for igual ao de comparação(j) e ele não tiver parada ainda,
        # teremos um número primo.
        for j in range(2,i+1):
            if(i == j):
                array.append(i);
            if((i%j) == 0):
                break
    return array


print(str(printPrimes(n)));