from collections import Counter

def parseFile(arr):
    return Counter(arr)

def writeFile(dictTop, top = 3, output = 'report.txt'):
    sumAll = sum(dictTop.values())
    dictTop = dictTop.most_common(top)
    with open(output, 'w') as new:
        new.write('Top categories:\n')
        rowNum = 0
        for row in dictTop:
            rowNum += 1
            new.write(f'{rowNum}. {row[0]} - {row[1]*100/sumAll:.2f}%\n')
