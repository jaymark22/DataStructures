import time

carGarage = []
tempGarageA = []
tempGarageB = []

cars = [["ABC 1234",0,0],["DEF 5678",0,0],["GHI 9101",0,0],\
       ["JKL 1213",0,0],["MNO 1415",0,0],["PQR 1617",0,0],\
       ["STU 1819",0,0],["VWX 2021",0,0],["YZA 2223",0,0],\
       ["BCD 2425",0,0]]

num = 0
n = 1
for i in range(len(cars)):
    carGarage.append(cars[num])
    time.sleep(1)
    print("New Car {} added to the garage. {} car space left.".format(cars[num], 10-n))
    cars.pop(num)
    n+=1
print(cars)   

carGarage[0][1]=1

print(carGarage[0])

'''
num = 0
numCar = 0
for car in cars:
        carGarage.append(car)
        time.sleep(1)
        print("{} added to the garage".format(cars[numCar]))
        numCar += 1
        cars.pop(cars[num])
        num +=1
'''


