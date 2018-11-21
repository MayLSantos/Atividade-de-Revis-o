lista = []
class Pilha():
    lista= []
    def push (self, valor):
        self.lista.append(valor)
    def pop (self):
        if (not(self.isEmpty())):
            return self.lista.pop()
    def isEmppty(self):
        return len(lista.lista) == 0
    def length (self):
        return len (self.lista)
    def  peek (self):
        if(not(self.isEmpty())):
            return self.lista[-1]


pilha= Pilha()
print("Lista de 5 elementos")
for i in range(5):
    valor= int(input("-"))
    if valor not in lista:
        pilha.push(valor)

print(lista)
