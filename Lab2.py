import pandas as pd

#Question 1
def Euclidean_distance(v1,v2):
    if len(v1)!=len(v2):
        return ("vectors are not of the same dimension")
    else:
        sq=0.0
        for i in range(0,len(v1)):
            sq+=(v1[i]-v2[i])**2
            euclidean_dist=sq**0.5
    return euclidean_dist

def Manhattan_distance(v1,v2):
    if len(v1)!=len(v2):
        return ("vectors are not of the same dimension")
    else:
        msum=0.0
        for i in range(0,len(v1)):
            msum+=(v1[i]-v2[i])
            man_dist=abs(msum)
    return man_dist

#Question 2

#Question 3 
def label_encoding(inp):
    category=set(inp) # Taking the common ones out
    label={} # creating the dictionary to save the corresponding numeric value to the data
    dt=[] # To store converted Numerical data
    for i,c in enumerate(category):
        label[c]=i
    for i in inp:
        dt.append(label[i])
    return dt

#Question 4
def onehot_encode(inp,data):
    onehot=[]
    for i in inp:
        if  data== i:
            onehot.append(1)
        else:
            onehot.append(0)   
    return onehot

#Ans 1
v1=[float(x) for x in input("Enter vector1 : ").split()]
v2=[float(x) for x in input("Enter vector2 : ").split()]
euclidean=Euclidean_distance(v1,v2)
manhattan=Manhattan_distance(v1,v2)
print("Euclidean distance is :", euclidean)
print("Manhattan distance is: ", manhattan)

#Ans 3
inp=[str(x) for x in input("Enter the input data as categorical data  : ").split()]
ans3=label_encoding(inp)
print("ANS 3: ")
print(ans3)

#Ans4
data=input("Enter the word to check:")
ans4=onehot_encode(inp,data)
print(ans4)