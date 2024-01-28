import pandas as pd
import math
import json
#from tree import Tree
from node import Node

"C:/Users/LaloDominguez/Documents/Patients.csv"
#df = pd.read_csv(r"C:/Users/LaloDominguez/Documents/Patients.csv")
df = pd.read_csv(r".\uploads\myDataSet.csv")
#df = pd.read_csv(r".\weather.csv")
#df = pd.read_csv(r".\contact_lenses.csv")
#df = pd.read_csv(r".\iris.data", names=["sepal length", "sepal width", "petal length", "petal width", "class"])
#df = pd.read_csv(r".\breast_cancer_wisconsin.data", names=["Sample Code", "Clump Thickness", "Cell Uniformity size", "Cell Uniformity shape", "Marginal adhesion", "Single eplithial cell", "Bare nuclei", "Bland Chromatin", "Normal nucleoli", "Mitoses", "Class"])
#print(df)

dbSize = df.shape
#print(dbSize)

instances = df.shape[0]
columns = df.shape[1]
#print(instances)
#print(columns)
#print("Only dataframe: \n",df.columns[columns -1])
allMyDecisions = []
#Show values of the class

lastColumnName = df.columns[columns -1]
#print(df[lastColumnName].value_counts())
print(df[df.columns[0]].tolist())
print(list(set(df[df.columns[0]].tolist())))
frontEndOptions = []
#Create list of options
for i in range(0, columns-1):
    currentColumnDataSet = df.columns[i]
    if i == 0:
        columnNamesV1 = df.columns.tolist()
        columnNamesV1.pop()
        frontEndOptions.append(columnNamesV1)
    frontEndOptions.append(list(set(df[df.columns[i]].tolist())))
#print(frontEndOptions)
with open("frontOptions.json", "w") as outfile:
    json.dump(frontEndOptions, outfile)

#first obtain the entropy of each label of classes
def calculateEntropy(df, instances):
    entropy = 0
    classes = df[lastColumnName].value_counts().keys().tolist()
    #print("keys: ", df["Nota"].value_counts().keys())
    #print("toList:", classes)
    for i in range(0, len(classes)):
        #iloc to refer to the last column
        #obtaining probability
        class_probability = df.iloc[:,-1].value_counts().tolist()[i]/instances
        #print(class_probability)
        entropy = entropy - class_probability*math.log(class_probability,2)
        #print("Entropy of class ", entropy)
    return entropy
    
    


entropy = calculateEntropy(df, instances)
#print("The class entropy is: ",entropy)

#in order to obtain the gain of information its necesary to obtain the entropy of each attributes
#columns -1 because we don´t need the classes but the attributes
def attribute_entropy(df):
    information_gain = [] 
    #If not working erase
    #TO DO 

    columns = df.shape[1]



    for i in range(0, columns -1):
        #print("i value: ", i)
        attribute_name = df.columns[i]
        attribute_classes = df[attribute_name].value_counts()
        #print("Attribute clases variable value: ", columns)
        #entropy from line 36
        gain = entropy   
        #print("Attribute name ",attribute_name)
        #print("Atrtibute class ", attribute_classes )
        #obtaining subsets of attributes where the classes are repeated, iterating over all the attributes
        for j in range(0, len(attribute_classes)):
            actual_class = attribute_classes.keys().tolist()[j]
            #print("\n\nActual class:", actual_class)
            subdata = df[df[attribute_name] == actual_class]
            #print("\n",subdata)
            #subdata.shape[0] because we need to divide with the instances of the datas 3/4 or 2/3
            subdata_entropy = calculateEntropy(subdata, subdata.shape[0])
            
            #print("subdata entropy: ", subdata_entropy)
            subdata_instances = subdata.shape[0]
            class_probability = subdata_instances/instances
            gain = gain - class_probability * subdata_entropy 
        information_gain.append(gain)
    #print("Those are my information gains ", information_gain)
    #print("After droping columns ", df.columns)
    greater_gain = information_gain.index(max(information_gain))
    name_greater_gain = df.columns[greater_gain]
    #print("Greater gain ", name_greater_gain)
    #print("all my gains", information_gain)
    #print("the best gain", name_greater_gain)
    return name_greater_gain

first_decision = attribute_entropy(df)
    #print("My decision is: ",decision)
first_attributes_decision = df[first_decision].value_counts().keys().tolist()
#print("My first desicion is: ", first_decision)
#print("myAttributes are: ", first_attributes_decision)
root = Node("", first_decision, [])
#print("The root is :", root.data)

#attribute_entropy(df)


def tree(df, precondition, dataStructure, node=None, mainRoot=None, latestPath = ""):
    currentNode = None
    #print(df)
    decision = attribute_entropy(df)
    #print("Decision? ", decision)
    #print("My decision is: ",decision)
    attributes_decision = df[decision].value_counts().keys().tolist()
    #print(attributes_decision)
    #print(attributes_decision)
    #branches  #Attribute == decision
    for i in range(0, len(attributes_decision)):
        #print(i)
        actual_attribute = attributes_decision[i]
        subdata = df[df[decision] == actual_attribute]
        subdata = subdata.drop(columns = decision)
        #print("-----------------START OF SUBDATA SECTION------------------------")
        #print(subdata)
        #print("-----------------END OF SUBDATA SECTION------------------------")
        #Definitive decision
        #print("What is this value? ", subdata.iloc[:,-1])

        #IMPORTANT erase and condition
        #print("Length of the data with condition: ",len(subdata.iloc[:,-1].value_counts().tolist()))
        #print("The values are: ", subdata)
        if len(subdata.iloc[:,-1].value_counts().tolist()) == 1:
            final_decision = subdata.iloc[:,-1].value_counts().keys().tolist()[0]
            allMyDecisions.append(decision)
            #print("Base case: ",decision)
            #print(precondition , "->" , decision , "->", actual_attribute , "->", final_decision)
            mainRoot = node.nodes.append(currentNode)
            #myLeave = Node(latestPath, decision,[], node)
            leave = str(precondition) + "->" + str(decision) + "->"+ str(actual_attribute) + "->"+ str(final_decision)+"\n"
            f = open("pseudoTree.txt", "a", encoding="utf-8")
            f.write(leave)
            f.close()
            
        else:
            precondition = str(precondition) + "->" + str(decision) + "->" + str(actual_attribute) + ""
            allMyDecisions.append(decision)
            #print(decision)
            '''if node.parent != None:
                currentNode = Node(latestPath, decision,[], node)
                mainRoot = node.nodes.append(currentNode)
                tree(subdata, precondition, allMyDecisions, currentNode, mainRoot, actual_attribute)'''
            tree(subdata, precondition, allMyDecisions, node, mainRoot, actual_attribute)
            precondition = ""
    #return precondition
    #return dataStructure
    return mainRoot


tree(df, "", allMyDecisions, root, root)

print("END")