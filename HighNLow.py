#Sorting without built in functions

n = 10
lowList = []
highList = []

def numHigh(numList):
    n = 10
    for i in range(n):
        for j in range(i+1, n):
            if(numList[i] < numList[j]):
                temp = numList[i]
                numList[i] = numList[j]
                numList[j] = temp
    print("first to the highest: ", numList[0]) 
    print("second to the highest: ", numList[1])

def numLow(numList):
    n = 10
    for i in range(n):
        for j in range(i+1, n):
            if(numList[i] > numList[j]):
                temp = numList[i]
                numList[i] = numList[j]
                numList[j] = temp
    print("first to the lowest: ", numList[0]) 
    print("second to the lowest: ", numList[1])

def main():
    numList = list(map(int,input("Enter 10 numbers : \n").strip().split()))[:n]
    numHigh(numList)
    numLow(numList)

main()
