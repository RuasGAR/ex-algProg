""" Ler duas matrizes (todos os elementos são inteiros)

Retornar a multiplicação dessas duas matrizes.

obs: número de colunas e/ou número de linhas pode ser 1. Não precisa verificar se o número de colunas da primeira matriz é igual ao número de linhas da segunda matriz.

Exemplo

input: [[2,1],[3, 2]] [[1,2],[1,1]] Output:[[3,5],[5,8]]

input:[1] [2] Output: [2]

input: [1,2] [[1],[2]] Output: [5]

input:[[1],[2]] [1,2] Output: [[1,2],[2,4]]

obs: Faça duas leituras, uma para cada matriz """

matrixA = eval(input());
matrixB = eval(input());

def generate_general_matrix(matrixA, matrixB):
    #criar, primeiro, a matriz resultante, com seus devidos espaços.
    #uma matriz A(mXn) multiplicada por uma matriz B(nXp), tera como resultante C(mXp)
    new_matrix = [];
    for i in range(len(matrixA)):
        line = []
        if(isinstance(matrixB[0],list)):
            for j in range(len(matrixB[0])):
                line.append(0);#Gera um vetor de p 0's para inlcuir na linha m    
            new_matrix.append(line);
        if(isinstance(matrixB[0],int)):
            for j in range(len(matrixB)):
                line.append(0)
            new_matrix.append(line);    
    return new_matrix

def general_matrix_product(matrixA,matrixB):

    result = generate_general_matrix(matrixA, matrixB)
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            element = 0;
            for k in range(len(matrixB)):
                """ print(f"Matrix A -- {matrixA[i][k]} --- {i,k} ======= Matrix B -- {matrixB[k][j]} --- {k,j} ") """
                element += matrixA[i][k] * matrixB[k][j];
            result[i][j] = element;

    return result    

def one_by_one(a,b): 
    product = [a[0]*b[0]];
    return product;

def one_column_by_one_line(a,b):
    #Esse caso é chamado quando temos uma multiplicação A(m X 1) X B(1 X n), resultando num vetor V(1 X 1);
    #Com isso, precisamos de uma variável de iteração, apenas. Como A só tem uma coluna, o primeiro índice permanecerá constante.
    #Já B, por ser um vetor, só possui um índice iterável, que acompanha o segundo índice de A, e por isso, só precisamos de uma iteração.
    new_matrix = [];
    element = 0;
    for i in range(len(b)):
        element += a[i][0]*b[i]
    new_matrix.append(element);    
    return new_matrix;   


def program(matrixA, matrixB):

    #A(1x1) B(1x1)
    if(len(matrixA) == 1 and len(matrixB) == 1):
        return one_by_one(matrixA, matrixB);

    #A(1 x m) B(m x 1):
    if(isinstance(matrixB[0], list) and len(matrixB[0]) == 1):
        return one_column_by_one_line(matrixB, matrixA)   

    #A(m X 1) B(1 x m):
    if(isinstance(matrixA[0],list) and len(matrixA[0]) == 1):
        new_matrix = generate_general_matrix(matrixA, matrixB);
        for i in range(len(matrixA)):
            for j in range(len(matrixA)): #len(matrixA) pois B é somente um vetor, então o len(matrixB) não retornaria a quantidade de colunas
                new_matrix[i][j] = matrixA[i][0] * matrixB[j]
        return new_matrix
    
    return general_matrix_product(matrixA,matrixB);
        

print(program(matrixA,matrixB));