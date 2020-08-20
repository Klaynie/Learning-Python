from collections import deque
input_stack = deque()
output_stack = deque()

def print_stack(stack):
    for _ in range(len(stack)):
        print(stack.pop())

def enqueue(stack, item):
    stack.appendleft(item)

def dequeue(stack):
    return stack.pop()

def input_handler(input_):
    input_ = input_.split(" ")
    if input_[0] == "PASSED":
        enqueue(output_stack, dequeue(input_stack))
    elif input_[0] == "READY":
        enqueue(input_stack, input_[1])
    elif input_[0] == "EXTRA":
        enqueue(input_stack, dequeue(input_stack))

for _ in range(int(input())):
    input_handler(input())

print_stack(output_stack)