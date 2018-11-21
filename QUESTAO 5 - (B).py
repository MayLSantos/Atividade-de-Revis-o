class Stack():
    def __init__(self):
        self.lista = []
    def push (self, valor):
        self.lista.append (valor)
    def pop (self):
        if (not(self.isEmpty())):
            return self.lista.pop()
    def isEmpty(self):
        return len(self.lista) == 0
    def length (self):
        return len (self.lista)
    def  peek (self):
        if(not(self.isEmpty())):
            return self.lista[-1]


stack = Stack ()
for i in range(16):
    if i %3 ==0:
        stack.push(i)
        print(i)
    elif i %4 ==0:
        #print("Elemento retirado: {}".format(i))
        stack.pop()       
