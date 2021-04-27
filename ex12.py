""" Duas palavras são anagramas se possuem exatamente as mesmas letras. Por exemplo, optar, parto, porta, prato, rapto, topar, trapo, tropa. 

Escreva a função anagrama(a,b) que retorna True se e somente se a e b são anagramas. Você pode assumir que a e b estão escritas usando apenas letras minúsculas.

Input: faça duas leituras uma para a e outra para b

Output: saída da função """

a = str(input());
b = str(input()); 

def anagrama(a,b):
    a = list(a);
    b = list(b);

    for item in a:
        if (item in b):
            del b[b.index(item)]; #Exclui o item de acordo com sua posição em B. Index só pega o índice do primeiro, então letras repetidas não são problemas.
    if(len(b) == 0): #Se b estiver vazia, todos os elementos de a foram encontrados em b. Logo, são anagramas;
        return True; 
    else:
        return False;

print(anagrama(a,b))