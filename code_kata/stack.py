class CreateStack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def is_empty(self):
        if not self.stack:
            return True
        else:
            return False

    def is_full(self):
        if len(self.stack) == self.size:
            return True
        else:
            return False
    
    def push(self, *item):
        for i in item:
            if self.is_full():
                print("stack is full unable to push")
            else:
                self.stack.append(i)
    
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            stack_top = self.stack[-1]
            self.stack.remove(stack_top)
            return stack_top
    
    def peek(self):
        print(self.stack[-1])

stack = CreateStack(10)
print(stack.is_empty())
print(stack.is_full())
stack.push(2)
stack.push(1)
stack.push(*(1,2,3,4,5,6,7,8,19))
print(stack.is_full())
stack.peek()
stack.pop()
stack.peek()