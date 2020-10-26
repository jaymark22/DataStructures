import time

carGarage = []
tempGarage = []


carEntered = {}
carExited = {}

cars = ['ABC 1234', 'DEF 5678', 'GHI 9101', 'JKL 1213', 'MNO 1415', 'PQR 1617', 'STU 1819','VWX 2021', 'YZA 2223', 'BCD 2425']

def carEn():
    for car in carEntered.keys():
        carEntered[car] += 1
    tempGarage.clear()
def carEx():
    for car in carExited.keys():
        carExited[car] += 1
    tempGarage.pop()

def newCar():
    return

def checkGarage(string):
    chkGarage = len(carGarage)

    if string == "a":
        if chkGarage > 10:
            print("Garage capacity on maximum. [!]")
            return False
        else:
            print(" Garage has {} available space.".format(10-chkGarage))
    if string == "b":
            print(" Garage has {} available space.".format(10-chkGarage))

def checkCarHist():
    return

def carInit():
    i=0
    for c in cars: 
        while i < len(cars):
            car = cars[i]
            time.sleep(1)
            print("{} added to the garage".format(car))
            carGarage.append(car)
            checkGarage("a")
            print("")
            e = {str(car) : 0}
            carEntered.update(e)
            i+=1

    for car in carEntered.keys():
        carEntered[car] += 1

def carEnt():
    i = 0
    j = len(tempGarage)
    for c in tempGarage: 
        while i < j:
            car = tempGarage[j-(i+1)]
            time.sleep(1)
            print("{} entered the garage".format(car))
            carGarage.append(car)
            checkGarage("a")
            print("")
            i+=1
    carEn()
def carExt():
    i = 0
    j = len(carGarage)
    for c in carGarage: 
        while i < j:
            car = carGarage[j-(i+1)]
            time.sleep(1)
            print("{} exited the garage".format(car))
            e = {str(car) : 0}
            carExited.update(e)
            carGarage.pop()
            #carGarage.pop(-1)
            tempGarage.append(car)
            checkGarage("b")
            print("")
            i+=1
    carEx()

def main():
    carInit()
    time.sleep(5)
    carExt()
    print("Exit", carExited)
    print("Start of New Cycle")
    carEnt()
    print("Entered", carEntered)
    carExt()
    print("Exit", carExited)
   

main()

