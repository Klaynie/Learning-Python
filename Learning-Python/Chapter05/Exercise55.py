def draw(t, length, n):
    if n == 0:
       return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)
    
'''
This piece of code uses the turtle world inputs draw "branches" in a recursive way, the angle of each branch is fixed by the variable "angle".
The initial length is n*length, which will go down to (n-1), (n-2), (n-3) and so on until n = 1 is reached and the final branch is drawn.
Once n = 0 the recursion is exited and the turtle will return to a previous, where it will start out to draw the next branches. 
In the special case of angle = 60 the branches form a hexagonal structure.
'''
