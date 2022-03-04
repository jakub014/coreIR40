import re


numberMapping = [
    (r'0', 'zero'),
    (r'1', 'one'),
    (r'2', 'two'),
    (r'3', 'three'),
    (r'4', 'four'),
    (r'5', 'five'),
    (r'6', 'six'),
    (r'7', 'seven'),
    (r'8', 'eight'),
    (r'9', 'nine'),
    (r'10', 'ten'),
]



def replaceSmallNumbersByLiterals(fileName, outputFile):

    with open(fileName, encoding='utf-8') as f:
        for i,line in enumerate(f):
            split = line.split("\t", 1)
            resultLine = split[1]
            for number, literal in numberMapping:
                reg = r"\b"+ number +r"\b"
                resultLine = re.sub(reg, literal, resultLine)
            outputFile.write(split[0] + "\t" + resultLine)

collectionoutputFile = open("D:/Informationretrieval/anserini/collections/collectionReplacedNumbers.tsv", "a", encoding='utf-8')
replaceSmallNumbersByLiterals("D:/Informationretrieval/anserini/collections/msmarco-passage/collectionTest.tsv", collectionoutputFile)

queryOutputfile = open("D:/Informationretrieval/anserini/collections/testqueriesreplacedNumbers.tsv", "a", encoding='utf-8')
replaceSmallNumbersByLiterals("D:/Informationretrieval/anserini/collections/msmarco-passage/msmarco-test2019-queries.tsv", queryOutputfile)
