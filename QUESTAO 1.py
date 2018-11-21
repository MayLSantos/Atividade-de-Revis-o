class pilha():
    def __init__(self):
        self.lista = []
    def push (self, valor):
        self.lista.append (valor)
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
