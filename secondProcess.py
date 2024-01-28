#obtain the root node
file = open('pseudoTree.txt', 'r')
first_line = file.readline()
text_splitted = first_line.split("->")
text_splitted.remove('') 

mainRoot = text_splitted[0]
print(mainRoot)
file.close

lineArray = []
file = open('pseudoTree.txt', 'r')
content = file.readlines()
for i in content:
    lineArray.append(i)
    print(i)
file.close()

j = 0
for i in lineArray:
    line_splitted = i.split('->')
    line_splitted.remove('') 
    if line_splitted[0] != mainRoot:
        lineArray[j-1] = lineArray[j-1][:-1]
        file = open("processedPseudoTree.txt", "a", encoding="utf-8")
        index = lineArray[j-1].index(line_splitted[0])
        print(line_splitted[0])
        print(lineArray[j-1])
        lostData = lineArray[j-1][:index-2]
        print("lost data", lostData)
        lineArray[j] = lostData+i
        print('---------------------')
        print(lineArray[j-1])
        print('---------------------')
        print(index)
        file.write(lostData+i)
        file.close()

    else:
        file = open("processedPseudoTree.txt", "a", encoding="utf-8")
        file.write(i)
        file.close()
    j += 1
    print(j)
