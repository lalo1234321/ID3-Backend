'''from node import Node
class Tree:
    def __init__(self, data):
        self.root = Node("",data, [])

    def addNode(self, node):
        self.nodes = self.root.nodes.append(node)'''
import random
 
r1 = random.randint(5, 1000000000000000000000)
from datetime import datetime

print("This is my random number ",r1)

 
import json
from node import Node
file = open('processedPseudoTree.txt', 'r')

# Read the first line of the file
first_line = file.readline()

# Process the first line (e.g., print it)
print("First line:", first_line)
text_splitted = first_line.split("->")
text_splitted.remove('')
print(text_splitted)
# Close the file
file.close()


def findRootOfTheTree(leave):
    if leave.depth != 1:
        return findRootOfTheTree(leave.parent)
    else:
        return leave


dictionary = {'data':text_splitted[0],'children':[1,2]}
root = Node("",text_splitted[0],[])
#print(root)
#print(len(text_splitted))
def treeCreation(i, parent):
    currentNode = parent
    if i == len(text_splitted)-1:
        currentNode = Node(text_splitted[i-1], text_splitted[i],[],parent, parent.depth+1,r1)
        parent.nodes.append(currentNode)
        #print("caso final?")
        return currentNode


    else:
        if i % 2 == 0:
            currentNode = Node(text_splitted[i-1], text_splitted[i],[], parent, parent.depth+1, r1)
            parent.nodes.append(currentNode)
            
            
        return treeCreation(i+1, currentNode)


treeReference = treeCreation(2,root)
#print(treeReference.data)

newRef = treeReference
#print(newRef.parent.parent.data)



# Open the file for reading
'''
file = open('demoFile2.txt', 'r')
content = file.readlines()
processedLine = content[1]
file.close()
#print(processedLine )
text_splitted2 = processedLine.split("->")
text_splitted2.remove('')
print("-------------------------------------------------")
print(text_splitted2)'''
'''
def treeCreationSecondIteration(i, parent):
    currentNode = parent
    if i == len(text_splitted)-1:
        currentNode = Node(text_splitted2[i-1], text_splitted2[i],[],parent, parent.depth+1)
        parent.nodes.append(currentNode)
        #print("caso final?")
        return currentNode


    else:
        if i % 2 == 0:
            if len(parent.nodes) != 0 :
                print("elemento ya existente")
                childrens = parent.nodes
                #print(childrens[0].data)
                for w in childrens:
                   
                    if w.data == text_splitted2[i]:
                        currentNode = w
                
            else:
                currentNode = Node(text_splitted2[i-1], text_splitted2[i],[], parent, parent.depth+1)
                parent.nodes.append(currentNode)
            
            
            
        return treeCreationSecondIteration(i+1, currentNode)
    
print(treeCreationSecondIteration(2, findRootOfTheTree(newRef)).parent.parent.nodes[0].nodes[0].data)





#parameter of the function needs to be the leave    
print('the root is: ',findRootOfTheTree(newRef).data)
'''



print("-------------------------This is the good one---------------------------------------")


def treeCreationRecursively(i, parent, currentList):
    #print("inside?")

    currentNode = parent
    enterToValidateChildsButNeverFindAMatch = False
    twinNodes = False
    #print(parent.data)
    #print("CurrentList data: ",currentList[i])
    if i == len(currentList)-1:

            


        #if not working erase above and erase cooment from below lines
        currentNode = Node(currentList[i-1], currentList[i],[],parent, parent.depth+1,r1)
        parent.nodes.append(currentNode)
        #print("caso final?")
        return currentNode


    else:
        if i % 2 == 0:
            print(len(parent.nodes))
            if len(parent.nodes) != 0 :
                print("hay almenos un hijo")
                childrens = parent.nodes
                #print(parent.nodes)
                #print(childrens[0].data)
                q = 0
                
                
                for w in childrens:
                    print("The children array lenght: ",len(childrens))
                    print("Current inner iteration: ", q)
                    
                    #if w.parent.data == parent.data and w.path == currentList[i-1]:
                     #   currentNode = w
                     #and w.depth == parent.depth+1 and w.path == currentList[i-1] at the end of the below condition
                    #if w.data == currentList[i] and w.path == currentList[i-1] :
                    if w.path == currentList[i-1] and w.data == currentList[i]:
                        print("condition is true")
                        #print(currentList[i])
                        currentNode = w
                        twinNodes = True
                        #return treeCreationRecursively(i+1, currentNode, currentList)
                        break

                    q +=1
                    if q == len(childrens):
                        enterToValidateChildsButNeverFindAMatch = True
                        #uncommnment this lines if problems
                    '''else:
                        print("Condition is false")
                        currentNode = Node(currentList[i-1], currentList[i],[], parent, parent.depth+1)
                        parent.nodes.append(currentNode)
                        break'''
                        #return treeCreationRecursively(i+1, currentNode, currentList)
                        #print("Buscando mi nodo, ", currentList[i])

            if enterToValidateChildsButNeverFindAMatch == True:
                print("Condition is false")
                currentNode = Node(currentList[i-1], currentList[i],[], parent, parent.depth+1, r1)
                parent.nodes.append(currentNode)

            if len(parent.nodes) == 0:
                print("avoiding this one")
                currentNode = Node(currentList[i-1], currentList[i],[], parent, parent.depth+1, r1)
                parent.nodes.append(currentNode)
                
                #print("Buscando mi nodo, ", currentList[i])
            
            
            
        return treeCreationRecursively(i+1, currentNode, currentList)

#textSplitted is the current list over the matrix
def createMatrix():
    matrix = []
    file = open('processedPseudoTree.txt', 'r')
    content = file.readlines()
    for i in content:
        text_splittedv1 = i.split("->")
        text_splittedv1.remove('')
        matrix.append(text_splittedv1)
    file.close()
    return matrix
#print(createMatrix())

def treeOverMatrix(matrixv1):
    rootv1 = Node("",matrixv1[0][0],[])
    currentLeave = None
    for z in matrixv1:
        print(z)
        currentLeave = treeCreationRecursively(2, rootv1, z)
        rootv1 = findRootOfTheTree(currentLeave)
        
        #print("current root: ", rootv1.nodes[len(rootv1.nodes)-1].data)
    return currentLeave





decisionTree = findRootOfTheTree(treeOverMatrix(createMatrix()))
print(decisionTree.nodes)



print("----------------------Generating dictionary---------------------------------")
r1 = random.randint(5, 1000000000000000000000)
mainDictionary = {"Hello": "View", "children":[]}
responseDictionary = {
    'data': decisionTree.data,
    'path': decisionTree.path,
    'depth': decisionTree.depth,
    'children': [],
    'uniqueKey': r1
}


def iterateTree(root, currentDictionary):
    
    for child in root.nodes:
        r1 = random.randint(5, 1000000000000000000000)
        print("Children depth: ",child.depth)
        print("Data: ", child.data , " Path: " ,child.path)
        newDictionary = {
            'data': str(child.data),
            'path': str(child.path),
            'depth': str(child.depth),
            'children': [],
            'uniqueKey': r1
            
        }
        
        currentDictionary["children"].append(newDictionary)
        if len(child.nodes) != 0:
            
            iterateTree(child, newDictionary)
       



iterateTree(decisionTree, responseDictionary)
print(responseDictionary)

with open("treeJsonFormat.json", "w") as outfile:
    json.dump(responseDictionary, outfile)


'''

dummyTree = {
    "data": "Presion Arterial",
    "path": "",
    "depth": 1,
    "children": [{
        "data": "Gota",
        "path": "Alta",
        "depth": 2,
        "children": [{
            "data": "No",
            "path": "Si",
            "depth": 3,
            "children": []
        },{
            "data": "Si",
            "path": "No",
            "depth": 3,
            "children": []
        }]
        
    },{
        "data": "Si",
        "path": "Normal",
        "depth": 2,
        "children":[]
    }]
}


def lookForTheCorrectPath(parentNode, path, nameOfParent, dictionaryR = None):
    for childs in parentNode["children"]:
        if parentNode["data"] == nameOfParent and childs["path"] == path:
            parentNode["children"].append({"okas":"new"})
            return childs
        if len(childs["children"]) != 0:
            lookForTheCorrectPath(childs,path,nameOfParent)


lookForTheCorrectPath(dummyTree, "Normal", "Presion Arterial")
print(dummyTree)'''