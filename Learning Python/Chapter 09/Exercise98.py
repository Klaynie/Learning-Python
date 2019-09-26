def is_reverse_number(number1, number2):
    number1 = str(number1)
    number2 = str(number2)
    if len(number1) != len(number2):
       return False
    i = 0
    j = len(number2) - 1
    while j >= 0:
        if number1[i] != number2[j]:
            return False
        i = i+1
        j = j-1    
    return True
    
def is_palindrome_number(number):
    return is_reverse_number(number,number)
    
def check_all_six_digit_numbers():
    i = 100000
    while i < 999999:
        if is_palindrome_number(str(i)[2:]):
            if is_palindrome_number(str(i+1)[1:]):
                if is_palindrome_number(str(i+2)[1:5]):
                    #print(i,1,str(i)[2:],2,str(i+1)[1:],3,i+2,str(i+2)[1:5],str(i+3),is_palindrome_number(str(i+3)))
                    if is_palindrome_number(str(i+3)):
                        print(i)
        i = i + 1
        
check_all_six_digit_numbers()
#198888
#199999