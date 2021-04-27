""" Faça uma função recursiva para calcular a divisão inteira de números inteiros positivos utilizando somente soma e subtração. 

Ex: 

Input: 1

3

 Output: 0

Input:  10

3

Output: 3 """

#Única leitura
from functools import reduce;

n = int(input());

def digits(n):
    #Retorna o número de dígitos de um número inteiro não negativo
    str_numbers = str(n);
    return len(str_numbers);

def inverted_numbers(n):
    #Única preocupação é se tem zero na frente ou não
    list_number = list(str(n));

    for i in range(len(list_number)//2): #Se o número for ímpar, o número "do meio" não será alterado
        list_number[i], list_number[len(list_number)-1 -i] = list_number[len(list_number)-1 -i], list_number[i];
    

    #Retira os zeros 
    j = 0;
    aux = list_number[:];
    while (list_number[j] == '0'):
        aux = list_number[j+1:];
        j += 1;

    #Concatena todos os elementos da lista numa só string;
    return int(reduce(lambda acc, new: acc + new,aux));

def both(n):
    if (n == 0):
        return (1,0);
    else:
        return (digits(n), inverted_numbers(n))

print(both(n));