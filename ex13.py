""" mplementar uma classe de número em ponto flutuante usando número inteiro, desta forma essa classe terá precisão "infinita".

Essa classe tem que ter os métodos abaixo:

class NumeroDecimal:    

    def __init__(self, v):

    def __add__(self,other):

    def __sub__(self,other):

    def __repr__(self):

Exemplo de uso: 

a = NumeroDecimal("0.1")

b = NumeroDecimal("1000000000000000.999999999999999999")

print (a, "+", b, "=", a+b)

print (b, "-", a, "=", b-a)

Saída:

,1 + 1000000000000000,999999999999999999 = 1000000000000001,099999999999999999

1000000000000000,999999999999999999 - ,1 = 1000000000000000,899999999999999999

Ex:

Input: 0.1+1000000000000000.999999999999999999

Output: 1000000000000001,099999999999999999

Input: 0.1-1000000000000000.999999999999999999

Output: 
-1000000000000000,899999999999999999 """


class NumeroDecimal:
    def __init__(self, v):
        self.integer, self.decimal = v.split('.');
    
    def __add__(self, other):
        
        integer = int(self.integer) + int(other.integer);
        
        self_size = len(self.decimal);
        other_size = len(other.decimal);
        major = '';
        minor = '';
        
        if(self_size >= other_size):
            major = self.decimal;
            minor = other.decimal;
        else:
            major = other.decimal;
            minor = self.decimal;

        for i in range(0,len(major)-len(minor)):
            minor += '0';

        decimal = int(major) + int(minor);

        len_int_major = len(str(int(major)));
        qnt_zeros = len(major) - len_int_major;

        #Quantidade de zeros a ser adicionada
        if(len(str(decimal)) > len_int_major):
            qnt_zeros -= 1;
        
        if(qnt_zeros):
            integer += 1;
            decimal =  qnt_zeros*'0' + str(decimal)[1:]
    
        return NumeroDecimal(f"{integer}.{decimal}");

    def __sub__(self, other):

        #Tratando o caso de menos em cima de menos
        if(other.integer[0] == '-'):
            other.integer = other.integer[1:]; #Retira o menos para passagem à função de soma
            return self + other;

        integer = int(self.integer) - int(other.integer);

        self_size = len(self.decimal);
        other_size = len(other.decimal);
        major = '';
        minor = '';
        
        if(self_size >= other_size):
            major = self.decimal;
            minor = other.decimal;
        else:
            major = other.decimal;
            minor = self.decimal;

        zeros = '';
        for i in range(0,len(major)-len(minor)):
            minor += '0';
        
        print(minor);
        print(major);
        
        decimal = '';
        carry = 0;
        for i in range(len(major)-1, -1, -1):
            digit = int(major[i]) - int(minor[i]) + carry;
            print(digit);
            if(digit < 0):
                if(i == 0):
                    digit = int(str(integer)[0]) + int(major) - int(minor[i]);
                else:    
                    digit = 10 + int(major[i]) - int(minor[i]);
                carry = -1
            decimal += str(digit);
        decimal = decimal[::-1];

        return NumeroDecimal(f"{integer}.{decimal}"); 

    def __repr__(self):
        return f"{self.integer},{self.decimal}";

numbers = str(input());
if('+' in numbers):
    both = numbers.split('+');
    print(NumeroDecimal(both[0]) + NumeroDecimal(both[1]));
if('-' in numbers):
    both = numbers.split('-');
    print(NumeroDecimal(both[0]) - NumeroDecimal(both[1]));