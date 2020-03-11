import urllib.request

def getURL(zipCode):
    return 'https://www.uszip.com/zip/' + str(zipCode)

def getContent(url):
    return urllib.request.urlopen(url)

def findValueInContent(content, startString, endString):
    for line in content:
        if str(line).find(startString) > 0:
            return findValueInLine(line, startString, endString)

def findValueInLine(line, startString, endString):
    return str(line)[str(line).find(startString)+len(startString):(str(line).find(endString))]

def getTownName(content, zipCode):
    startString = '<title>'
    endString = ','
    return findValueInContent(content, startString, endString)

def getTownPopulation(content, zipCode):
    startString = '<dt>Total population</dt><dd>'
    endString = '<span class'
    return findValueInContent(content, startString, endString)

def getZipCode():
    prompt = "This program will provide the name and population of a town for a given zip code. Please provide a zip code!\n"
    zipCode = str(input(prompt))
    try:
        content = getContent(getURL(zipCode))
        print('The town name is: ' + getTownName(content, zipCode), 'The population is: ' + getTownPopulation(content, zipCode))        
    except:
        print('Something went wrong. 1) Could not find town 2) No internet connection? 3) ???')

if __name__ == '__main__':
    getZipCode()