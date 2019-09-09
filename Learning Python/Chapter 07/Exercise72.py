def square_root(x,a):
    epsilon = 0.000000000000001
    while True:
        #print(x)
        y = (x + a/x) / 2
        if  abs(y-x) < epsilon:
            break
        x = y
    return x
#square_root(3, 8)