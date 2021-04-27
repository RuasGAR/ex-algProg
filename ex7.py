""" Decidir se um vetor A[1 .. k] é uma subsequência de um vetor B[1 .. n]. (Por exemplo, (5, 6, 4) é subsequência de (9, 5, 6, 3, 9, 6, 4, 7).) Escreva um algoritmo RECURSIVO para resolver o problema.

obs: fazer duas leituras, uma para cada vetor e retornar um booleano (True ou False).

Ex:

Input: [33, 9, 0] 

[1, 3, 5, 7, 'a', 'aba']

 Output: False """

#Temos que procurar um vetor dentro do outro.
#Primeiro, procuramos pelo primeiro elemento do vetor.
#A partir do momento que o encontrarmos, temos de passar um recorte daquela lista a partir do índice daquele número encontrado em diante.
#Assim, garantiremos que se trata de uma subsequência.
#No entanto, é preciso ter cuidado já que podemos ter valores repetidos em sequencia, então sempre iniciariamos uma nova contagem! --> DESMENTIDO EM TESTE
#Isso poderia ter sido previsto: se estamos fatiando a sub-sequência, significa que já encontramos aquele valor antes. 
#Assim, não importa se ele se repetir. Afinal, não queremos uma sub-sequência com todos os elementos diretamente seguido uns dos outros.


sub = eval(input());
sequence = eval(input());

def sub_sequence(sub, sequence):
    print(sub,sequence);

    if (len(sub) == 0 or len(sequence) == 0):
        return False;
    if (len(sub) == 1):
        if(sub[0] == sequence[0]):
            return True;
        else:
            if(len(sequence) != 1): #Se ainda houver lista a ser percorrida, perpetuamos a sub-sequência com o restante da lista, sempre tirando 1 elemnento.
                return sub_sequence(sub,sequence[1:]);
            else: 
                return False;    

    search = sub[0];
    for i in range(len(sequence)):
        if (sequence[i] == search):
            return sub_sequence(sub[1:], sequence[i+1:]);
    return False; #Se não houver compatibilidade após os casos base, já podemos excluir a possibilidade de sub-sequência.
    
print(sub_sequence(sub,sequence));