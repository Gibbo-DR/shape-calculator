from math import atan, sqrt, degrees
def getMeasurement(): # Handles standard measurement inputs and constraints
    measurement = input("Enter an integer measurement between 10mm-10000mm (inclusive): ")
    try:
        measurement = int(measurement)
    except ValueError:
        measurement = 0 # if a string it justs sets as out of range

    if measurement > 9 and measurement < 10001:
        return measurement
    else:
        return False # any falses back in main throw the error
    
def Pyramid(H,W,L):
    volume = (1/3)*H*W*L
    baseArea = W*L
    if W > L:
        longerSide = W
        shorterSide = L
    elif W < L:
        longerSide = L
        shorterSide = W
    else: # if they are the same it only calculates one value cause they will be the same
        TriA = (1/2) * sqrt(((L/2)**2) + ((H)**2)) * W
        ApexAng = degrees(atan(((1/2)*W)/(sqrt((((1/2)*L)**2)+(H**2)))))
        BaseAng = (180 - ApexAng)/2 #
        Sum = ApexAng + BaseAng*2

        return f"Volume = {volume}mm^3,\
            \nBase Area = {baseArea}mm^2,\
            \nSide Triangle areas = {TriA}mm^2,\
            \nApex angles for both triangles = {ApexAng} degrees,\
            \nBase angles for both triangles = {BaseAng} degrees,\
            \nSum of short base angles for both = {Sum} degrees"
    
    shorterTriA = (1/2) * sqrt(((longerSide/2)**2) + ((H)**2)) * shorterSide
    shorterApexAng = degrees(atan(((1/2)*shorterSide)/(sqrt((((1/2)*longerSide)**2)+(H**2)))))
    shorterBaseAng = (180 - shorterApexAng)/2
    shortSum = shorterApexAng + shorterBaseAng*2

    longerTriA = (1/2) * sqrt(((shorterSide/2)**2) + ((H)**2)) * longerSide
    longerApexAng = degrees(atan(((1/2)*longerSide)/(sqrt((((1/2)*shorterSide)**2)+(H**2)))))
    longerBaseAng = (180 - longerApexAng)/2
    longSum = longerApexAng + longerBaseAng*2
    
    return f"Volume = {volume}mm^3,\
        \nBase Area = {baseArea}mm^2,\
        \nShorter Base Triangle Area = {shorterTriA}mm^2,\
        \nShorter Base Triangle apex angle = {shorterApexAng} degrees,\
        \nShorter Base Triangle Base angles = {shorterBaseAng},\
        \nLonger Base Triangle Area = {longerTriA},\
        \nLonger Base Triangle Apex Angle = {longerApexAng},\
        \nLonger Base Triangle Base angles = {longerBaseAng},\
        \nSum of short base angles = {shortSum},\
        \nSum of long base angles = {longSum}"

active = True
while active:
    print("\n")
    shapeChoice = input("""choose the shape you would like to calculate:
                        1. Rectangle
                        2. Pyramid
                        choice: """)
    if shapeChoice == "1":
        print("feature still in development...")
        pass

    elif shapeChoice == "2":
        print("please enter a value for height") # getting measurements (could -> __init__)
        height = getMeasurement()
        print("please enter a value for width")
        width = getMeasurement()
        print("please enter a value for length")
        length = getMeasurement()
        if height == False or width == False or length == False:
            print("user input must be an integer within the range 10mm-10000mm inclusive")
        else:
            print(Pyramid(height, width, length))

    else:
        print("user input must be a number displayed next to a shape name")

