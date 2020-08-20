import plotly.graph_objects as go
import plotly.express as px
import string
import datetime
import math

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    word = ''
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))
    t.sort(reverse=True)
    return t

def total_words(hist):
    return sum(hist.values())

def fileName():
    timestamp = datetime.datetime.utcnow()
    timestampString = str(timestamp.strftime("%Y")) + '-' + str(timestamp.strftime("%m")) + '-' + str(timestamp.strftime("%d")) + '_' + str(timestamp.strftime("%H")) + str(timestamp.strftime("%M")) + str(timestamp.strftime("%S"))
    outputFilename = 'Exercise1309-Word-Freq' + '_' + timestampString
    return outputFilename 

def zipfAnalysisFile(t):
    entryCounter = 1    
    outputFilename = fileName()
    outputFilename += '.csv'
    file = open(outputFilename ,'w') 
    file.write('word;log(rank);log(freq)'+'\n')
    for freq, word in t:
        file.write(word + ';' + str(math.log10(entryCounter)) + ';' + str(math.log10(freq)) + '\n')
        entryCounter += 1
    print('File ' + outputFilename + ' created')

def zipfAnalysisGraph(t, n):
    freqLogList = []
    rankLogList = []
    outputFilename = fileName()
    entryCounter = 1
    for freq, word in t[:n]:
        freqLogList.append(math.log10(freq))
        rankLogList.append(math.log10(entryCounter))
        entryCounter += 1
    fig = px.scatter(x=rankLogList, y=freqLogList, trendline='ols')
    fig.update_layout(title='Zipf Analysis', xaxis_title='log(Rank)', yaxis_title='log(Frequency)')
    fig.write_html(outputFilename + '_' + str(n) + '.html', auto_open=False)
    print('File ' + outputFilename + ' created')

hist = process_file('emma.txt')
t = most_common(hist)
n = total_words(hist)
fig = zipfAnalysisGraph(t,n)