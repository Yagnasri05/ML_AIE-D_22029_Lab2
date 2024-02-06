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
def KNN(dt, k, test):
    prediction = []
    distances = []

    for j in range(len(dt)):
        vec = [dt[j][0], dt[j][1]]
        d = Euclidean_distance(vec, test)
        distances.append((d, dt[j][2]))

    distances.sort(key=lambda x: x[0])
    nearest_neighbors = distances[:k]
    return nearest_neighbors

#Question 3 
def label_encoding(inp):
    category=set(inp) # Taking the common ones out
    label={} # creating the dictionary to save the corresponding numeric value to the data
    dt=[] # To store converted Numerical data
    for i,c in enumerate(category):
        label[c]=i #assigning the numerical value to the data
    for i in inp:
        dt.append(label[i])
    return dt

#Question 4
def onehot_encode(inp,data):
    onehot=[] #empty dict for one hot encoding 
    for i in inp:
        if  data== i:
            onehot.append(1) #if entered data by user is equal to the data present, then it is given as 1 else, it is given as 0
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

#Ans 2
d1=[110,150,175,195,95]
d2=[1000,2500,3500,2750,1100]
d3=[1,1,0,1,0]
dt=[d1,d2,d3] #dataset to find the nearest neighbours
k=int(input("Enter number of neighbour: "))
vector_data=input("Enter the vectors with space : ")
test = list(map(int, vector_data.split()))
KNN_classifier=KNN(dt,k,test)
print(KNN_classifier)