
from fileinput import filename
from typing import Set

# Reads lines specified in argument (asc sorted list) from the specified file
def readLinesfromFile(lineNs, fileName):
    result = []
    with open(fileName, encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i == lineNs[0][0]:
                result.append((line, lineNs[0][1]))
                lineNs.pop(0)
            if len(lineNs) == 0:
                return result
    return result

# Returns a list of tuples (passageID, rating)
def retrieveRelevantPassageIds(queryid, filename, ratingIndex):
    passages = []
    with open(filename, 'r',encoding='utf-8') as f:
        for line in f:
            if line.split()[0] == queryid and line.split()[ratingIndex] != '0':
                passages.append((int(line.split()[2]), float(line.split()[ratingIndex])))
    passages.sort(key=lambda x: x[0])
    return passages

# Counts the amount of unique query ids in a file where the query id is the first column
def countUniqueQueryIds(filename):
    SetOfQueryIds = set()
    with open(filename, 'r',encoding='utf-8') as f:
        for line in f:
            SetOfQueryIds.add(line.split()[0])
    return len(SetOfQueryIds)

# Returns the query given the query id
def getQueryFromId(queryid, filename):
    with open(filename, 'r',encoding='utf-8') as f:
        for line in f:
            if line.split()[0] == queryid:
                return line

def printRelevantPassages(queryid, filename, ratingIndex):
    passageIDs = retrieveRelevantPassageIds(queryid, filename, ratingIndex)
    
    result = readLinesfromFile(passageIDs, "msmarco-passage/collection.tsv")
    result.sort(key=lambda x: -x[1])

    # Prints the retrieved passages
    for line in result[:20]:
        try:
            print(line[1])

            print("\n")
            print(line[0])

        except UnicodeEncodeError:
            print("UnicodeEncodeError \n")

def findAmountOccurences(term, filename):
    i = 0
    with open(filename, 'r',encoding='utf-8') as f:
        for line in f:
            if term.lower() in line.split()[1].lower():
                i = 1 + i
    return i

# --------------------------------------------------


# Replace arguments with your path

queryid = "1121709"

print(getQueryFromId(queryid, "msmarco-passage/msmarco-test2019-queries.tsv"))

print("\n ---------------------------OPTIMAL------------------------")
printRelevantPassages(queryid, "msmarco-passage/2019qrels-pass.tsv", 3)
print("\n --------------------------WHAT WE GOT---------------------------------------")
printRelevantPassages(queryid, "msmarco-passage/run-2.txt", 4)
# passageIDs = retrieveRelevantPassageIds(queryid, "msmarco-passage/run-2.txt", 4)




#print(countUniqueQueryIds("msmarco-passage/run-2.txt"))