""" Faça um algoritmo RECURSIVO que receba dois vetores A[1 .. n] e B[1 .. n] e decida se existe um índice i tal que A[i] = B[i].
obs: fazer duas leituras, uma para cada vetor e retornar um booleano (True ou False).

Ex:

Input: [1, 3, 5, 7, 'a', 'aba']

[33, 9, 0] """

v1 = eval(input())
v2 = eval(input())

#Vetores não necessariamente terão igual tamanho.
#Como comparamos elemento por elemento, se uma lista acabar, o programa deve comparar se já ou não compatibilidade entre os dois elementos.
def compare_vectors(v1,v2): 

    if(len(v1) == 1 or len(v2) == 1): #"Or" aqui é importante pois não sabemos qual será o maior vetor. Uma vez que um deles se encerra, o programa para.
        if(v1[0] == v2[0]):
            return True;
        else:
            return False;

    if(v1[0] == v2[0]): #Comparação normal assumindo que nenhum dos dois tem somente um elemento.
        return True    
    else:
        return compare_vectors(v1[1:],v2[1:]); #Fatiamos a lista sempre removendo o primeiro item, que está envolvido na comparação em cada "iteração" #A função retorna False para todos os casos que não se enquadram nas validações.
        
print(compare_vectors(v1,v2));