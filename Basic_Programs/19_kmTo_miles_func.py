def calcMiles(km):
    f=0.62137

    miles=km * f

    print("The value of {0} km in miles: {1}".format(km,miles))


km=float(input("Enter the value of vehicles in kilometers: "))

calcMiles(km)