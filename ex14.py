""" Deve implementar a classe Polinômio, que será usada para representar polinômios envolvendo uma variável,

Sua classe deverá implementar soma, subtração e multiplicação de polinômios, entre outros métodos, conforme o código parcial dado abaixo. As reticências (...) indicam onde você deve escrever a implementação de cada método.

class Polinomio:

    "Representa um polinomio de uma variavel"

    def __init__(self, coeficientes=[]):

        "Construtor, onde a lista coeficientes contem os coeficientes para os termos de grau 0, grau 1, etc."

        ...

    def __setitem__(self, grau, coeficiente):

        "Altera o coeficiente para o termo do grau dado"

        ...

    def __getitem__(self,grau):

        "Retorna o coeficiente para o grau dado"

        ...

    def grau (self):

        "Retorna o grau do polinomio"

        ...

    def __mul__(self,p):

        "Retorna o polinomio dado pela multiplicacao deste polinomio por p (tambem um polinomio)"

        ...

    def __add__(self,p):

        "Retorna o polinomio dado pela soma deste polinomio com p (tambem um polinomio)"

        ...

    def __sub__(self,p):

        "retorna o polinomio dado pela diferenca entre este polinomio e p (tambem um polinomio)"

        ...    

    def avalia (self,x):

        "Retorna a avaliacao do polinomio avaliado em x."

        ...

Como exemplo de caso de uso, o código abaixo

p = Polinomio ([1,2])

p[3] = 0.5

q = Polinomio ([0,-1,2])

print(p[0],p[1],p[2])

print(p.avalia(0))

print(p.avalia(3),q.avalia(3),(p+q).avalia(3),(p-q).avalia(3),(p*q).avalia(3))

print(((p+q)*(p-q)).avalia(0.5))

Imprime

1 2 0

1.0

20.5 15 35.5 5.5 307.5

4.25390625

O programa deve ler 3 entradas separadas onde (1) é a lista com os coeficiente do polinômio p; (2)  é a lista com os coeficiente do polinômio q; (3) um número x

O programa deve imprimir print(p.avalia(x),q.avalia(x),(p+q).avalia(x),(p-q).avalia(x),(p*q).avalia(x))

Ex:

Input: [1,2,0,0.5]

[0,-1,2]

3

Output:

20.5 15 35.5 5.5 307.5 """

#Polinômios de uma variável

class Polinomio:
    def __init__(self, coeficientes=[]):
        self.coeficientes = coeficientes;
    
    def __setitem__(self, grau, coeficiente):
        #Se a inserção se der num número imediatamente posterior ao último da lista
        if(grau == len(self.coeficientes)):
            self.coeficientes += [coeficiente];
        
        #Se a inserção ocorrer em algum grau que não seja consecutivo.
        #Exemplo: polinômio de grau 4 recebe um coeficiente para o grau 7
        elif(grau > len(self.coeficientes)):
            for i in range(len(self.coeficientes), grau):
                self.coeficientes.append(0);
            self.coeficientes += [coeficiente];
        
        #Caso somente de subistituição de coeficientes
        else:
            self.coeficientes = self.coeficientes[0:grau] + [coeficiente] + self.coeficientes[grau+1:] 


    def __getitem__(self,grau):
        return self.coeficientes[grau];
    
    def grau(self):
        return (len(self.coeficientes) - 1);
    
    def __make_same_length(self,l,other):
        major, minor = [],[];
    
        if(len(l) >= len(other)):
            major = l[:];
            minor = other[:];
        else:
            major = other[:];
            minor = l[:];

        #Preenche os coeficiente vazios com 0
        for i in range(len(major) - len(minor)):
            minor.append(0);
        
        return (major, minor)


    def __mul__(self, p):
        sized_lists = self.__make_same_length(self.coeficientes, p.coeficientes);
        major = sized_lists[0];
        minor = sized_lists[1];
        result = [];

        for i in range(len(major)*2-1):
            result.append(0);

        for i in range(len(major)):
            for j in range(len(minor)):
                result[i+j] += major[i]*minor[j];
            
        
        return Polinomio(result);
        
        #Verificar se têm mesmo tamanho. Se não, um deles deverá ser aumentado até dar certo;
    
        #p também é polinômio
    
    def __add__(self,p):
        sized_lists = self.__make_same_length(self.coeficientes, p.coeficientes);
        sized_self_coef = sized_lists[0];
        sized_p_coef = sized_lists[1];
        result = [];

        for i in range(len(sized_self_coef)):
            result += [sized_self_coef[i] + sized_p_coef[i]];
        
        return Polinomio(result);

    def __sub__(self,p):
    
        #Não utilizo o método criado para isso pois não é possível saber se o major ou minor estão, de fato, na ordem.
        #Cópias para completar o tamanho
        self_coef = self.coeficientes[:];
        p_coef = p.coeficientes[:];  
        result = [];
        if(len(self.coeficientes) >= len(p.coeficientes)):
            for i in range(len(self_coef)-len(p_coef)):
                p_coef.append(0);
        else:
            for i in range(len(p_coef) - len(self_coef)):
                self_coef.append(0);

        for i in range(len(self.coeficientes)):
            result += [self_coef[i] - p_coef[i]];
        
        return Polinomio(result);

    
    def avalia(self,x):
        result = 0;
        for i in range(len(self.coeficientes)):
            result += self.coeficientes[i]*(x**i);
        return result;

    def __repr__(self):
        return str(self.coeficientes);
    
#Inputs

p_coef = eval(input());
q_coef = eval(input());
x = input();
if ('.') in x:
    x = float(x);
else:
    x = int(x);

p = Polinomio(p_coef);
q = Polinomio(q_coef);


print(p.avalia(x), q.avalia(x), (p+q).avalia(x), (p-q).avalia(x),(p*q).avalia(x));