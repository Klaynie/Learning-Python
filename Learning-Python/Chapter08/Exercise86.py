from Exercise84 import *
    
def countLettersInString(stringIn,letterToCheck):
    count = 0
    index = 0
    while index < len(stringIn):
          index = find(stringIn, letterToCheck, index)
          if index > 0:
             count = count + 1
          else:
             break
    print(count)
     
countLettersInString('banana','a')