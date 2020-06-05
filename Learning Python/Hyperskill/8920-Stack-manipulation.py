from collections import deque
stack = deque()

def print_stack():
    global stack
    for _ in range(len(stack)):
        print(stack.pop())

def push(item):
    global stack
    stack.append(item)

def pop():
    global stack
    stack.pop()

def input_handler(input_):
    input_ = input_.split()
    if len(input_) == 1:
        pop()
    else:
        push(input_[1])

for _ in range(int(input())):
    input_handler(input())

print_stack()