from collections import deque
to_read_stack = deque()
read_stack = deque()

def print_stack(stack):
    for _ in range(len(stack)):
        print(stack.pop())

def push(stack, item):
    stack.append(item)

def pop(stack_in, stack_out):
    stack_out.append(stack_in.pop())

def input_handler(input_):
    global to_read_stack, read_stack
    input_ = input_.split(" ", 1)
    if input_[0] == "READ":
        pop(to_read_stack, read_stack)
    elif input_[0] == "BUY":
        push(to_read_stack, input_[1])

for _ in range(int(input())):
    input_handler(input())

print_stack(read_stack)