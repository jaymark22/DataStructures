import time

carGarage = []
tempGarage = []

carEntered = {}
carExited = {}
carGone = []

cars = ['ABC 1234', 'DEF 5678', 'GHI 9101', 'JKL 1213', 'MNO 1415', 'PQR 1617', 'STU 1819','VWX 2021', 'YZA 2223', 'BCD 2425']

def carEn():
    for car in carEntered.keys():
        if (car not in carGone): 
            carEntered[car] += 1
    tempGarage.clear()

def carEx():
    for car in carExited.keys():
        if (car not in carGone): 
            carExited[car] += 1
    yeet = len(tempGarage)
    print("\n Car {} left the garage for good :( \n".format(tempGarage[yeet-1]))
    carGone.append(tempGarage[yeet-1])
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
    print("Sum of all car entries: ", sum(carEntered.values()))
    print(carEntered)
    print("\nSum of all car exits: ", sum(carExited.values()))
    print(carExited)

def carInit():
    print("[ Start of Program ]\n")
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
            carExited.update(e)
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
            print("{} transferred to the temporary garage.".format(car))
            tempGarage.append(car)
            carGarage.pop()
            checkGarage("b")
            print("")
            i+=1
    carEx()

def main():
    carInit()
    while (len(tempGarage) or len(carGarage)) != 0: 
        time.sleep(1)
        print("\n[A car decided to get out of the garage.]\n")
        carExt()
        #print("Car Transferred: ", carExited)
        time.sleep(1)
        carEnt()
        #print("\nCar Entered: \n", carEntered)
        print("")
        time.sleep(1)
    checkCarHist()
    time.sleep(5)
    print("\n End of Program.")
    print("titiw :3")

main()

