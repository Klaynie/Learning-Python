from collections import deque
ticket_stack = deque()

def print_stack(stack):
    for _ in range(len(stack)):
        print(stack.pop())

def enqueue(item):
    global ticket_stack
    ticket_stack.appendleft(item)

def dequeue():
    global ticket_stack
    ticket_stack.pop()

def input_handler(input_):
    input_ = input_.split(" ")
    if input_[0] == "SOLVED":
        dequeue()
    elif input_[0] == "ISSUE":
        enqueue(input_[1])

for _ in range(int(input())):
    input_handler(input())

print_stack(ticket_stack)