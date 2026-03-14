path = "/home/documents/../dd"
pathList= path.split('/')

resultList = []
for i in range(0, len(pathList)):
    if pathList[i] == '':
        continue
    elif pathList[i] == '.':
        continue
    elif pathList[i] == '..':
        if resultList:
            resultList.pop()
    else:
        resultList.append(pathList[i])

result = ""
for i in range(0, len(resultList)):
    result = result + "/" + resultList[i]

print(result)