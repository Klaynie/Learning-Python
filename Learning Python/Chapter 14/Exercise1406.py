import urllib.request

def getURL(zipCode):
    return 'https://www.uszip.com/zip/' + str(zipCode)

def getContent(url):
    return urllib.request.urlopen(url)

def getTownName(zipCode):
    content = getContent(getURL(zipCode))
    for line in content:
        if str(line).find('<title>') > 0:
            townName = str(line)[9:(str(line).find(','))] #Check to make 9 more dynamic
            break
    return townName

def getTownPopulation(zipCode):
    content = getContent(getURL(zipCode))
    for line in content:
        if str(line).find('<dt>Total population</dt>') > 0:
            townPopulation = str(line)[str(line).find('<dt>Total population</dt>')+29:str(line).find('<span class')] #Check to make 29 more dynamic
            break
    return townPopulation

def getZipCode():
    prompt = "This program will provide the name and population of a town for a given zip code. Please provide a zip code!\n"
    zipCode = str(input(prompt))
    try:
        print('The town name is: ' + getTownName(zipCode), 'The population is: ' + getTownPopulation(zipCode))        
    except:
        print('Could not find town or maybe no Internet Connection?')

getZipCode()
