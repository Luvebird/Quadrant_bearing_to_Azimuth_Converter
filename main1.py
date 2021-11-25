print("Quadrant bearing to Azimuth Converter")
number=input("Enter Quadrant bearing: ")
if number[0]=="N" and number[-1]=="E":
    print(number[1:-1])
elif number[0]=="S" and number[-1]=="E":
    a=float(number[1:-1])
    print("Azimuth: "+str(180-a))
elif number[0]=="S" and number[-1]=="W":
    a=float(number[1:-1])
    print("Azimuth: "+str(a-180))
elif number[0]=="N" and number[-1]=="W":
    a=float(number[1:-1])
    print("Azimuth: "+str(360-a))

