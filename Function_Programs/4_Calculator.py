def calc(a,o,b):
    if o=="+":
        r=a+b
        print("The sum of {0} and {1} is {2}.".format(a,b,r))
    
    elif o=="-":
        r=a-b
        print("The sub of {0} and {1} is {2}.".format(a,b,r))

    elif o=="*":
        r=a*b
        print("The mul of {0} and {1} is {2}.".format(a,b,r))

    elif o=="/":
        r=a/b
        print("The div of {0} and {1} is {2}.".format(a,b,r))

    elif o=="%":
        r=a%b
        print("The rem of {0} and {1} is {2}.".format(a,b,r))

    else:
        print("ERROR: Invalid Operator Input!")
        print("Please ENTER only (+ , - , * , / , %) Operators!")


a=int(input("Enter the first number: "))

o=input("Enter the Operator to be performed: ")

b=int(input("Enter the second number: "))

calc(a,o,b)


