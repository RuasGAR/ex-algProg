""" Calcular o determinante de uma matriz quadrada A de tamanho máximo n>=4.

Obs: os coeficientes da matriz são inteiros e o formato da matriz é igual ao do exc.3 e 4 """

from copy import deepcopy;
matrix = eval(input());
#Teorema de Laplace

#Utilizar a função que calcula o determinante de matriz de ordem 3
#Fazer de forma recursiva

#(-1) ** i+j*determinante da matriz sem aquela coluna e sem aquela linha

def order_three(a):
    return a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1] - a[2][0]*a[1][1]*a[0][2] - a[2][1]*a[1][2]*a[0][0] - a[2][2]*a[1][0]*a[0][1];

#Escolho uma linha -> a primeira, por exemplo. matrix[0];

def determinant(a):

    det = 0;

    if(len(a) == 3):
        return order_three(a);
    else:
        for index, element in enumerate(a[0]): #Escolho uma linha -> a primeira, por exemplo. matrix[0];
            aux_a = deepcopy(a); #Copia a matriz e, todos os itens dentro da mesma por valor!
            del aux_a[0];
            for j in range(len(aux_a)):
                del aux_a[j][index];
            det += element*((-1)**(0 + index))*determinant(aux_a);
        
        return det;

print(determinant(matrix));