def check_fermat():
    prompt = "This program will check if Fermat's Last Theorem Holds True. Please provide an integer number!\n"
    a = int(input(prompt))
    prompt = "Please provide another integer number!\n"
    b = int(input(prompt))
    prompt = "Please provide another integer number!\n"
    c = int(input(prompt))
    prompt = "Please provide an integer number greater than 2!\n"
    n = int(input(prompt))
    print('Now we will check if ' + str(a) + '^' + str(n) + ' + '+ str(b) + '^' + str(n) +' = '+ str(c) + '^' + str(n))
    if a**n+b**n == c**n:
        print(str(a**n+b**n)+' = '+str(c**n)+ ' Holy smokes, Fermat was wrong!')
    else:
        print(str(a**n+b**n)+' = '+str(c**n)+ " No, that doesn't work.")
    
check_fermat()