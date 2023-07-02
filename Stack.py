class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            print(self.stack[len(self.stack) - 1])
        else:
            print(None)

    def catch_last(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def printout(self):
        print(str(self.stack))

    def catch_all(self):
        return str(self.stack)


lista = Stack()
lista.push(1)
lista.peek()
lista.push(3)
print(lista.catch_last())
lista.printout()
lista.push(5)
print(lista.pop())
print(lista.pop())
print(lista.catch_last())
lista.printout()