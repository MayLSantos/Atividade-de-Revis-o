class Pilha():
    def push (self, valor):
        self.numeros.append (valor)
    def pop (self):
        if (not(self.isEmpty())):
            return self.numeros.pop()
    def isEmppty(self):
        return len(numeros) == 0
    def length (self):
        return len (self.numeros)
    def  peek (self):
        if(not(self.isEmpty())):
            return self.numeros[-1]

s=0
def Num (numeros):
    pilha= Pilha()
    s=0

    for i in range(len(numeros)):
        s= s+numeros[i]
        pilha.pop()
    

Num()
numeros= [2,5,6,9,7]
print(s)
