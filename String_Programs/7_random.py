# Create a program to generate a random string using the random.choices() function.---------------------------

# Random_str.py

import string    
import random # define the random module  
S = 10  # number of characters in the string.  
# call random.choices() string module to find the string in Uppercase + numeric data.  
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
print("The randomly generated string is : " + str(ran)) # print the random data  









# Generate a random string of upper case and lower-case letters-------------------------------

# UprLwr.py

# write a program to generate the random string in upper and lower case letters.  
import random  
import string  
def Upper_Lower_string(length): # define the function and pass the length as argument  
    # Print the string in Lowercase  
    result = ''.join((random.choice(string.ascii_lowercase) for x in range(length))) # run loop until the define length  
    print(" Random string generated in Lowercase: ", result)  
  
    # Print the string in Uppercase  
    result1 = ''.join((random.choice(string.ascii_uppercase) for x in range(length))) # run the loop until the define length  
    print(" Random string generated in Uppercase: ", result1)  
  
Upper_Lower_string(10) # define the length 













# Random String of Specified Characters-------------------------------------------------------
# Specific.py

# create a program to generate the random string of given letters.  
import random  
import string  
def specific_string(length):  
    sample_string = 'pqrstuvwxy' # define the specific string  
    # define the condition for random string  
    result = ''.join((random.choice(sample_string)) for x in range(length))  
    print(" Randomly generated string is: ", result)  
  
specific_string(8) # define the length  
specific_string(10)  