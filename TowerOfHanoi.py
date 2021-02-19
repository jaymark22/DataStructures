
import time

count = 0
def moveDisks(disks, inPos, toPos):
    print("\nHanoi disc {} moved from {} to {}.".format(disks, inPos,toPos))

def runHanoi(disks, inPos, auxPos, toPos):
    global count
    if disks == 0:
        pass
    else:
        runHanoi(disks-1, inPos, toPos, auxPos)
        moveDisks(disks, inPos,toPos)
        #time.sleep(1)
        runHanoi(disks-1, auxPos, inPos, toPos)
        count += 1
disks = int(input("Enter Number of Hanoi Disks: "))

print("-="*18)
print("  Hanoi Disks: Smallest at disk 1 ")
print("    {} disks with columns A B C   ".format(disks))
print("-="*18)
runHanoi(disks, "A", "B", "C")
print("\n-="*18)
print("Moves Made: ", count)
print("-="*18)