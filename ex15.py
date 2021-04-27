""" class Dominos:
	"Simula um jogo de dominó"
  def __init__(self, l):
  	"Inicializa um novo jogo com o estoque l"
    ...
  def compra(self):
  	Retira uma peça ainda não sorteada do estoque e a retorna. Levanta a exceção ValueError caso não existam mais peças
    ...
    def coloca(self,peca,extremidade):
    	Dada uma peça (tupla da forma a,b), e uma extremidade (0 ou 1),adiciona a peça ao jogo estendendo a extremidade dada. Retorna True se a peça foi colocada com sucesso ou False caso contrário
      ...
    def imprime(self):
    	Imprime o jogo até o momento. A impressão tem que ser na forma de uma 'escadinha', isto é, as peças colocadas na mesa se alternam na orientação horizontal e vertical. O leiaute entre uma jogada e a próxima não pode mudar!

Exemplo de uso:

l=[(5,6),(1,5),(2,2),(3,4),(0,4),(1,3)]
d = Dominos(l)
for i in range(6):
  p = d.compra()
  print("Compra:", p)
  if d.coloca(p,0) or d.coloca(p,1): d.imprime()

Que imprime:

Compra: (5, 6)
56
Compra: (1, 5)
1
5
56
Compra: (2, 2)
Compra: (3, 4)
Compra: (0, 4)
Compra: (1, 3)
31
 1
 5
 56

Você tem que ler uma lista de tuplas com todas as peças. 

As compras vão seguir a ordem desta lista.

 Só no final deve imprimir o domino.

A ordem da tentativa de colocar deve ser a mesma do caso de uso acima.

 Input: [(5,6),(1,5),(2,2),(3,4),(0,4),(1,3)]

Output: 31

 1

 5

 56 """

class Dominos:

    def __init__(self, l):
        self.pecas = l;
        self.tabuleiro = [];
        self.rodadas = len(l);

    def compra(self):
        if(len(self.pecas) == 0): raise ValueError;
        else:
            peca = self.pecas[0];
            self.pecas = self.pecas[1:];
            return peca;

    def coloca(self, peca, extremidade):
        #retorna true se for possível, retorna false se não
        if(len(self.tabuleiro) == self.rodadas):
            return False;

        elif(self.tabuleiro == []):
            self.tabuleiro.append(peca);
            return True;

        else:
            if(extremidade == 0):
                if(peca[0] == self.tabuleiro[len(self.tabuleiro)-1][0]):
                    self.tabuleiro.append((peca[1],peca[0]));
                    return True;
                elif(peca[1] == self.tabuleiro[len(self.tabuleiro)-1][0]):
                    self.tabuleiro.append(peca);
                    return True;

            elif(extremidade == 1):
                if(peca[0] == self.tabuleiro[len(self.tabuleiro)-1][1]):
                    self.tabuleiro.append(peca);
                    return True;
                elif(peca[1] == self.tabuleiro[len(self.tabuleiro)-1][1]):
                    self.tabuleiro.append((peca[1],peca[0])); #Insere uma tupla com a peça invertida;
                    return True;
        return False;


    def imprime(self):
        for i in range(len(self.tabuleiro)-1,-1, -1):
            if(i % 2 == 0):
                print(str(self.tabuleiro[i][0]) + str(self.tabuleiro[i][1]));
            else:
                print(i*" " + str(self.tabuleiro[i][0]) + "\n" + i*" " + str(self.tabuleiro[i][1]));

inp = eval(input());

d = Dominos(inp);
