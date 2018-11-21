class Pilha():
    def __init__(self):
        self.lista = []
    def push (self, valor):
        self.lista.append (valor)
    def pop (self):
        if (not(self.isEmpty())):
            return self.lista.pop()
    def isEmppty(self):
        return len(lista) == 0
    def length (self):
        return len (self.lista)
    def  peek (self):
        if(not(self.isEmpty())):
            return self.lista[-1]

pilha= Pilha()

for i in range (5):
    n= int(input("-"))
    pilha.push(i)
    print("Adicionou mais um elemento, a lista ficou com  {} elementos." .format(pilha.length))
    
for i in range (2):
    pilha.pop()
    print("Retirou um elemento, a lista ficou com  {} elementos." .format(pilha.length))
        
