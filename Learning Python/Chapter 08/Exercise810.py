def is_palindrome3(word):
     return word == word[::-1]
     
print(is_palindrome3('saippuakivikauppias'))
print(is_palindrome3('lagerregal'))

print(is_palindrome3('saippuakivikauppiBs'))
print(is_palindrome3('lagerregBl'))     