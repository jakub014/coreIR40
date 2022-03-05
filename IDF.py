import numpy as np

def findAmountOccurences(term, filename):
    i = 0
    with open(filename, 'r',encoding='utf-8') as f:
        for line in f:
            if term.lower() in line.lower():
                i = 1 + i
    return i


# IDF used in Lucene: https://www.elastic.co/blog/practical-bm25-part-2-the-bm25-algorithm-and-its-variables
def luceneIDF(termAmount, totalDocs):
    return np.log(1 + (totalDocs - termAmount + 0.5) / (termAmount + 0.5))


termAmount = findAmountOccurences("three", "../anserini/collections/msmarco-passage/collection.tsv")

print(luceneIDF(termAmount, 8841822))