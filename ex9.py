""" Faça uma função que retorna um booleano informando se uma matriz é um quadrado mágico.

Dizemos que uma matriz quadrada inteira é um quadrado mágico se a soma dos elementos de cada linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e secundária são todas iguais.

Ex: 

Input: [[8, 3, 4], [1, 5, 9], [6, 7, 2]]

Output: True

Input: [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

Outpu: False """

#Squared Matrix
matrix = eval(input());

def general(matrix):

    #Diagonal Principal:
    main_diag_sum = 0;
    for i in range(len(matrix)):
        main_diag_sum += matrix[i][i]
    
    #Diagonal secundária:
    second_diag_sum = 0;
    for i in range(len(matrix)):
        second_diag_sum += matrix[i][len(matrix)-1]; 

    if(main_diag_sum != second_diag_sum):
        return False;

    # Cada linha e cada coluna. Se já não for igual, a função para para  
    for i in range(len(matrix)):
        each_line_sum = 0;  
        each_column_sum = 0;
        for j in range(len(matrix)):
            each_line_sum += matrix[i][j];
            each_column_sum += matrix[j][i];
        if(each_line_sum != main_diag_sum or each_column_sum != main_diag_sum):
            return False;
            
    return True;

print(general(matrix));