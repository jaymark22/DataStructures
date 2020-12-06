import time
import os 
from os import system, name 

def clear(): 

	# for windows 
	if name == 'nt': 
		_ = system('cls') 

	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear') 
	
carGarage = []
tempGarage = []

carEntered = {}
carExited = {}
carGone = []

#cars = ['ABC 1234', 'DEF 5678', 'GHI 9101', 'JKL 1213', 'MNO 1415', 'PQR 1617', 'STU 1819','VWX 2021', 'YZA 2223', 'BCD 2425']
cars = []

def userOption():
    menu = """
                [Garage Management]
    
                  :Process Menu:
    
        1)  Add Car to the Garage.
        2)  Get Car out of the Garage.
        3)  Check Garage Capacity.
        4)  View all cars in the Garage.
        5)  Check Arrival and Departure Counter.
        6)  Yeet all cars out of the Garage.
        7)  End Program. 
    """
    print(menu)

    userInput = input("What do you want to do?: ")
    if userInput.isdigit():
        optionPass = userInput
        processPass(optionPass)

    else:
        print("\n[Error] Carefully choose from the options above!")
        time.sleep(3)      
        clear()
        time.sleep(2)
        userOption()


def processPass(option):

    if option == "1":
        addCar()

    elif option == "2":
        removeCar()

    elif option == "3":
        checkGarage("a")
        print(carGarage)
        time.sleep(5)
        clear()
        userOption()

    elif option == "4":
        return

    elif option == "5":
        return

    elif option == "6":
        yeetAll()
        
    elif option == "7":
        print("\nThank you for using Garage Management.")
        time.sleep(3)
        print("Goodbye :)")
        time.sleep(2)
        clear()
        exit()

    else: 
        print("\n[Error] Unknown command. Please try again :(")
        time.sleep(3)
        clear()
        userOption()
    

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

def addCar():
    print("\n[   Adding a Car to the Garage   ]")
    print("[ Plate Number Example = ABC 123 ]")
    newCar = str(input("\nNew Car's Plate Number: "))
    if not newCar:
        print("\n[Error] Please enter a Plate Number!")
        time.sleep(3)      
        clear()
        time.sleep(2)
        addCar()
    else: 
        if len(newCar) != 7:
            print("\n[Error] Please follow the prescribed plate configuration!")
            time.sleep(3)      
            clear()
            time.sleep(2)
            addCar()

        else:
            cars.append(newCar)
            carInit()
    return

def removeCar():
    print("\n[   Please Enter the Leaving Car's Plate Number   ]")
    print("Cars List: "+carGarage)
    newCar = str(input("\nCar's Plate Number: "))
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
    print("[ Car Valet: ]")
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


def yeetAll():
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
    print("titiw :3")

while True:
    userOption()

