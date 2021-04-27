""" Calcular o determinante de uma matriz quadrada A de tamanho máximo n=3.
Fazer 3 funções: uma para cada tamanho da matriz. """

#Calcular o determinante de matrizes até a ordem 3
matrixA = eval(input());

def order_one(a):
    return a[0];

def order_two(a):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0];

def order_three(a):
    # [[a,b,c], [d,e,f], [g,h,i]];
    return a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1] - a[2][0]*a[1][1]*a[0][2] - a[2][1]*a[1][2]*a[0][0] - a[2][2]*a[1][0]*a[0][1]

if (len(matrixA) == 1):
    print(order_one(matrixA));

if (len(matrixA) == 2):
    print(order_two(matrixA)); 

if (len(matrixA) == 3):
    print(order_three(matrixA));