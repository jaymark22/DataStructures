#Using Recursive Algorithm
def DecToBin(num):
    list = []
    if num > 1: 
        DecToBin(num // 2) 
        list.append(num % 2)
        print(list)
     
if __name__ == '__main__': 
      
    numVal=int(input("Enter a decimal number: "))
    DecToBin(numVal) 
   
-