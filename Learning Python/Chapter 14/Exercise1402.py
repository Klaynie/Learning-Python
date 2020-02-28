import string

def modifyFile(filename, outputFile, patternString, replacementString):
    for line in open(filename):
        process_line(line, outputFile, patternString, replacementString)

def process_line(line, outputFile, patternString, replacementString):
    outputFile.write(line.replace(patternString, replacementString))
        
def sed(patternString, replacementString, fileNameInput, fileNameOutput):
    try:
        modifyFile(fileNameInput, open(fileNameOutput, 'w'), patternString, replacementString)
    except:
        print('Something went wrong')
        
sed('am','PM', 'emma.txt', 'ebba.txt')