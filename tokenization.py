#find the string
def findQuote(first, second, wordString):
     quoteFound = ""
     for i in range(first, second+1):
          quoteFound += wordString[i]
     return quoteFound

#funciton to find keywords operators and delimiters
def findPossible(possibleType,type,str):
     for x in possibleType:
          if x in str:
               type.add(x)

#holds the tokens
keywords = set()
identifiers = set()
operators = set()
delimiters = set()
literals = set()

possibleKeywords = {
     "def",
     "return",
     "print",
     "if" 
}
possibleOperators = {
     "=",
     "==",
     "+",
     "-"
}
possibleDelimiters = {
     "(",
     ")",
     ":",
     ","
}

#open the file and read what is in it
with open('testToken.py') as file:
    lineList =list()

    line = file.readline()
    lineList.append(line)
    while line:
        line = file.readline()
        lineList.append(line)
file.close()

#now remove the comments
noCommnetsList =[]
for x in lineList:
       j = x.split("#",1)
       noCommnetsList.append(j[0])
lineList=noCommnetsList

#remove \n from string
noNewlineList =[]
for x in lineList:
       j = x.split("\n",1)
       noNewlineList.append(j[0])
lineList=noNewlineList

#get rid of '' in list
shortenedList =[]
for x in lineList:
      x=x.strip()
      if x != '':
        shortenedList.append(x)
lineList=shortenedList


#all lines into one string
lineStr = ""
for line in lineList:
    for i in range(len(line)):
        lineStr+=line[i]
    lineStr += " "

#find literals (quotes)
firstQuoteIndex = 0
secondQuoteIndex = 0
quoteFound = False

for i in range(len(lineStr)):
     if lineStr[i]=='"' and quoteFound == False:
          firstQuoteIndex = i
          quoteFound = True
     elif lineStr[i] == '"' and quoteFound == True:
          secondQuoteIndex = i
          quoteFound = False
          literals.add(findQuote(firstQuoteIndex,secondQuoteIndex, lineStr))
for z in literals:
     lineStr = lineStr.replace(z, " ")

#find keywords operators and delimiters
findPossible(possibleKeywords,keywords,lineStr)
findPossible(possibleOperators,operators,lineStr)
findPossible(possibleDelimiters,delimiters,lineStr)

#find identifyers here
newLineStr = lineStr
for x in keywords:
     newLineStr = newLineStr.replace(x, ' ')
for x in operators:
     newLineStr = newLineStr.replace(x, ' ')
for x in delimiters:
     newLineStr = newLineStr.replace(x, ' ')
for x in literals:
     newLineStr = newLineStr.replace(x, ' ')
possibleStr = newLineStr.split(" ")

for y in possibleStr:
     if y != '':
          if y.isdigit():
               literals.add(y)
          else:
               identifiers.add(y)
          
#output 1
print("--------Output 1--------")
for line in lineList:
     print(line)
print("\n")

print("--------Output 2--------")
print("Keywords    | ",', '.join(keywords))
print("Identifiers | ",', '.join(identifiers))
print("Operators   | ",', '.join(operators))
print("Delimiters  | ",', '.join(delimiters))
print("Literals    | ",', '.join(literals))