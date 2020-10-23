''' #[Working]
#Using built-in decimal to binary conversion function 
def decimalToBinary(n):  
    return bin(n).replace("0b", "")  
  
if __name__ == '__main__':  
    num = int(input("Enter a decimal number: "))
    print( "Binary equivalent: ",decimalToBinary(num))  
'''
'''
#Using Recursive Algorithm
def DecToBin(num):
    if num > 1:
        DecToBin(num // 2)
        num = num % 2
    print([num])
    

numVal = int(input("Enter a decimal number: "))
DecToBin(numVal)
'''
#Using Recursive Algorithm
listNum = []

class DerivedList(list):
    def insertAtLastLocation(self,obj):
        self.__iadd__([obj])    
 
lst=DerivedList(listNum)

def DecToBin(num):
    while num > 1:
        DecToBin(num // 2)
        num = num % 2
    lst.insertAtLastLocation(num)
    
def numVal():
    numVal = int(input("Enter a decimal number: "))
    DecToBin(numVal)

numVal()
print(lst)





