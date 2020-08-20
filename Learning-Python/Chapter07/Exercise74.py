import math

def eval_loop():
    print("This program will use the built-in eval() function on the last input you provide. Type done to start the evaluation!\n")
    while True:
        line = input('>')
        if line == 'done':
           break
        line_old = line
    print(eval(line_old))

eval_loop()