from math import atan, sqrt, degrees, pi
##########################
def getMeasurement(lowerBound=10, upperBound=10000): # Handles standard measurement inputs and constraints
    measurement = input(f"Enter an integer measurement between {lowerBound}mm-{upperBound}mm (inclusive): ")
    try:
        measurement = int(measurement)
    except ValueError:
        measurement = 0 # if a string it justs sets as out of range

    if measurement > lowerBound-1 and measurement < upperBound+1:
        return measurement
    else:
        return False # any falses back in main throw the error

def Cuboid(H,W,L):
    surfArea = 2 * (L*W + L*H + W*H)
    volume = round(H*W*L,3)
    HtoW = round(H/W, 3)
    WtoL = round(W/L,3)
    LtoH = round(L/H,3)
    return f"Volume = {volume}mm^3,\
        \nsurface area = {surfArea}mm^2,\
        \nH:W = {HtoW},\
        \nW:L = {WtoL},\
        \nL:H = {LtoH}"


def Pyramid(H,W,L):
    volume = round((1/3)*H*W*L,3)
    baseArea = round(W*L, 3)
    if W > L:
        longerSide = W
        shorterSide = L
    elif W < L:
        longerSide = L
        shorterSide = W
    else: # if they are the same it only calculates one value cause they will be the same
        TriA = round((1/2) * sqrt(((W/2)**2) + ((H)**2)) * L, 3)
        ApexAng = round(degrees(atan(((1/2)*W) / (sqrt(((1/2)*L)**2+(H)**2)))*2), 3)
        BaseAng = round((180 - ApexAng)/2, 3)
        Sum = round(ApexAng + BaseAng*2, 3)

        return f"Volume = {volume}mm^3,\
            \nBase Area = {baseArea}mm^2,\
            \nSide Triangle areas = {TriA}mm^2,\
            \nApex angles for both triangles = {ApexAng} degrees,\
            \nBase angles for both triangles = {BaseAng} degrees,\
            \nSum of short base angles for both = {Sum} degrees"
    
    shorterTriA = round((1/2) * sqrt(((longerSide/2)**2) + ((H)**2)) * shorterSide, 3)
    shorterApexAng = round(degrees(atan(((1/2)*shorterSide) / (sqrt(((1/2)*longerSide)**2+(H)**2)))*2), 3)
    shorterBaseAng = round((180 - shorterApexAng)/2, 3)
    shortSum = round(shorterApexAng + shorterBaseAng*2, 3)

    longerTriA = round((1/2) * sqrt(((shorterSide/2)**2) + ((H)**2)) * longerSide, 3)
    longerApexAng = round(degrees(atan(((1/2)*longerSide) / (sqrt(((1/2)*shorterSide)**2+(H)**2)))*2), 3)
    longerBaseAng = round((180 - longerApexAng)/2, 3)
    longSum = round(longerApexAng + longerBaseAng*2, 3)
    
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

def Sphere(R):
    volume = round((4/3)*pi*(R**3),3)
    surfArea = round(4*pi*(R**2),3)

    return [f"Volume = {volume}mm^3,\
            \nsurface area = {surfArea}mm^2",[volume,R*2]] #[output message, [volume, height]]


def Cone(H,R):
    surfArea = round(pi*R*(R+sqrt((R**2) + H**2)), 3)
    volume = round((1/3)*pi*(R**2)*H, 3)
    angle = round(degrees(atan(H/R)), 3)
    return [f"Volume = {volume}mm^3,\
            \nSurface Area = {surfArea}mm^2,\
            \nAngle from base to conical surface = {angle} degrees", [volume, H]]

def Disk(R,H):
    #surfArea = (2*pi*IR*H+2*pi*(IR+OR))*H+2*(pi*(IR+OR)**2 - pi*IR**2)
    surfArea = round((2*pi*R*H) + 2*(pi*(R**2)), 3)
    #volume = pi*(IR+OR)**2 * H - pi*(IR**2)*H
    volume = round(pi*(R**2) * H, 3)
    return [f"Volume = {volume}mm^3,\
            \nSurface Area = {surfArea}mm^2", [volume, H]]

#MAIN
def main():
    active = True
    while active:
        print("\n")
        shapeChoice = input("""choose the shape you would like to calculate:
                            1. Rectangle
                            2. Pyramid
                            3. Sphere
                            4. Cone (unstable, untested)
                            5. Disk (unstable, untested)
                            6. Snowman (unstable, untested)
                            e. Exit
                            choice: """)
        if shapeChoice == "1":
            print("please enter a value for height") # getting measurements (could -> __init__ if oop approach)
            height = getMeasurement()
            print("please enter a value for width")
            width = getMeasurement()
            print("please enter a value for length")
            length = getMeasurement()
            if height == False or width == False or length == False:
                print("user input must be an integer within the given range (inclusive)")
            else:
                print(Cuboid(height,width,length))

        elif shapeChoice == "2":
            print("please enter a value for height") # getting measurements (could -> __init__)
            height = getMeasurement()
            print("please enter a value for width")
            width = getMeasurement()
            print("please enter a value for length")
            length = getMeasurement()
            if height == False or width == False or length == False:
                print("user input must be an integer within the given range (inclusive)")
            else:
                print(Pyramid(height, width, length))

        elif shapeChoice == "3":
            print("please enter a valid input for radius")
            radius = getMeasurement()
            if radius == False:
                print("user input must be an integer within the given range (inclusive)")
            else:
                print(Sphere(radius)[0])

        elif shapeChoice == "4":
            print("Base R")
            cone_rad = getMeasurement()
            print("height")
            cone_height = getMeasurement()
            if cone_rad == False or cone_height == False:
                print("user input must be an integer within the given range (inclusive)")
            else:
                print(Cone(cone_height,cone_rad)[0])

        elif shapeChoice == "5":
            print("Disk radius")
            disk_rad = getMeasurement()
            print("Disk thik")
            disk_thick = getMeasurement()
            if disk_rad == False or disk_thick == False:
                print("user input must be an integer within the given range (inclusive)")
            else:
                print(Disk(disk_rad,disk_thick)[0])

        elif shapeChoice == "6": #Snowman but its not constrainted properly just yet
            print("base R")
            base_radius = getMeasurement()
            print("body R")
            body_radius = getMeasurement(upperBound=int(round((2/3)*base_radius, 0)), lowerBound=int(round((1/3)*base_radius, 0)))
            print("head R")
            head_radius = getMeasurement(upperBound=int(round((2/3)*body_radius, 0)), lowerBound=int(round((1/3)*body_radius, 0)))
            print("nose R")
            nose_radius = getMeasurement(upperBound=int(round((1/10)*head_radius, 0)))
            print("nose H")
            nose_height = getMeasurement(upperBound=20*nose_radius)
            print("top hat rim R")
            hat_rim_radius = getMeasurement(upperBound=head_radius)
            print("top hat rim thickness")
            hat_thick = getMeasurement(upperBound=2*nose_radius)
            print("top hat base R")
            hat_base_radius = getMeasurement(upperBound=int(round((2/3)*hat_rim_radius,0)))
            print("top hat height")
            hat_height = getMeasurement(upperBound=hat_rim_radius*2, lowerBound=int(round((1/5)*hat_rim_radius,0)))
            if base_radius == False or body_radius == False or head_radius == False or nose_radius == False or nose_height == False or hat_rim_radius == False or hat_thick == False or hat_base_radius == False or hat_height == False:
                print("user input must be in the given range")
            else:
                Volume = round(Sphere(base_radius)[1][0] + Sphere(body_radius)[1][0] + Sphere(head_radius)[1][0] + Cone(nose_height, nose_radius)[1][0] + Disk(hat_rim_radius,hat_thick)[1][0] + Cone(hat_base_radius,hat_height)[1][0], 3)
                Height = round(Sphere(base_radius)[1][1] + Sphere(body_radius)[1][1] + Sphere(head_radius)[1][1]  + Disk(hat_rim_radius,hat_thick)[1][1] + Cone(hat_base_radius,hat_height)[1][1], 3)
                print(f"snowman volume = {Volume}, height = {Height}")
        
        elif shapeChoice == "e":
            active = False

        else:
            print("user input must be a number displayed next to a shape name")

    return "Thanks for using the shape calculator"

if __name__ == "__main__":
    print(main())