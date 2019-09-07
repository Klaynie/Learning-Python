def is_triangle(a,b,c):
    if a+b<c:
        print('No')
    elif a+c<b:
        print('No')
    elif b+c<a:
        print('No')
    else:
        print('Yes')

def check_triangle():
    prompt = "This program will check if you can create a triangle with 3 given lengths. Please provide an integer number!\n"
    a = int(input(prompt))
    prompt = "Please provide another integer number!\n"
    b = int(input(prompt))
    prompt = "Please provide another integer number!\n"
    c = int(input(prompt))
    is_triangle(a, b, c)
        
check_triangle()