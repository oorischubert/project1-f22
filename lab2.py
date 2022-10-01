
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    def __str__(self):
        return str(self.stack[::-1])

class StackCalc(Stack):
    def __init__(self):
        super().__init__()
    def add(self):
        self.push(self.pop() + self.pop())
    def sub(self):
        self.push(self.pop() - self.pop())
    def mult(self):
        self.push(self.pop() * self.pop())
    def div(self):
        self.push(self.pop() / self.pop())

#[2pts] Complete the function below that is checking "delimiter matching"
# of a given expression using a stack
# Requirement: delimiters are () [] {} <>  
# Hint:"index" method for string could be useful (but not necessary)
# Example with multiple outputs:
"""
Enter your expression:(a<b[c]+r*{5}>)
looks good!

Enter your expression:(a+[b)*c)
matching problem!

Enter your expression:(a+b[c<r>]
matching problem!
"""

def check_delimiter(expr):
    s = Stack()
    for i in expr:
        if i in "([{<":
            s.push(i)
        elif i in ")]}>":
            if s.isEmpty():
                print("matching problem!")
                return
            elif i == ")" and s.peek() != "(":
                print("matching problem!")
                return
            elif i == "]" and s.peek() != "[":
                print("matching problem!")
                return
            elif i == "}" and s.peek() != "{":
                print("matching problem!")
                return
            elif i == ">" and s.peek() != "<":
                print("matching problem!")
                return
            else:
                s.pop()
    if s.isEmpty():
        print("looks good!")
    else:
        print("matching problem!")