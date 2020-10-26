'''
cars = [("ABC 1234",1,0),("DEF 5678",0,0),("GHI 9101",1,1),\
       ("JKL 1213",0,0),("MNO 1415",0,0),("PQR 1617",0,0),\
       ("STU 1819",0,1),("VWX 2021",1,1),("YZA 2223",0,0),\
       ("BCD 2425",1,0)]
'''
import os
# cars = [["ABC 1234",1,0],["DEF 5678",0,0],["GHI 9101",1,1],\
#        ["JKL 1213",0,0],["MNO 1415",0,0],["PQR 1617",0,0],\
#        ["STU 1819",0,1],["VWX 2021",1,1],["YZA 2223",0,0],\
#        ["BCD 2425",1,0]]

cars = {  'ABC 1234': [0,0],
          'DEF 5678': [0,0],
          'GHI 9101': [0,0],
          'JKL 1213': [0,0],
          'MNO 1415': [0,0],
          'PQR 1617': [0,0],
          'STU 1819': [0,0],
          'VWX 2021': [0,0],
          'YZA 2223': [0,0],
          'BCD 2425': [0,0]
}

carsList = list(cars)                                                                                                                      
car = carsList[0]
print(car) 
print(carsList) 


carInOut = cars.values()
carsVal = list(carInOut)

carIn = carsVal[0][1]

print(carIn)
carIn +=1
print(carIn)



# #======================================================================================================#
# # Python3 code to demonstrate working of  
# # Mapping key values to Dictionary 
# # Using dictionary comprehension 
  
# # initializing list 
# test_list = [{'name' : 'Manjeet', 'age' : 23},  
#              {'name' : 'Akshat',  'age' : 22}, 
#              {'name' : 'Nikhil', 'age' : 21}] 
  
# # printing original list 
# print("The original list is : " + str(test_list)) 
  
# # Mapping key values to Dictionary 
# # Using dictionary comprehension 
# res = {sub['name'] : sub['age'] for sub in test_list} 
  
# # printing result  
# print("The flattened dictionary is : " + str(dict(res)))  

# #======================================================================================================#

# #for search 

# dictionary = {'george': 16, 'amber': 19}
# search_age = input("Provide age")
# for name, age in dictionary.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
#     if age == search_age:
#         print(name)
'''
 from collections import defaultdict
 data = [(2010, 2), (2009, 4), (1989, 8), (2009, 7)]
 d = defaultdict(list)
print (d) # output --> defaultdict(<type 'list'>, {})
 for year, month in data:
     d[year].append(month) 
print (d) # output --> defaultdict(<type 'list'>, {2009: [4, 7], 2010: [2], 1989: [8]})
'''