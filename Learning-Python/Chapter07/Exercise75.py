import math

def estimate_pi():
    epsilon = 1e-15
    inverse_approx_pi_k = 0
    k=0
    while True:
        next_inverse_approx_pi_k = 2*math.sqrt(2)/9801*(math.factorial(4*k)*(1103+26390*k)/(math.factorial(k)**4*396**(4*k)))
        inverse_approx_pi_k = inverse_approx_pi_k + next_inverse_approx_pi_k
        approx_pi = 1 / inverse_approx_pi_k
        if(abs(approx_pi-math.pi)< epsilon):
            break
        k = k + 1
    print(approx_pi)
    
estimate_pi()