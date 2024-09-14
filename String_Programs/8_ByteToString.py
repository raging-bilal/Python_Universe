# Convert Bytes to String in Python?


# Using the decode() Method
# The most common way to convert bytes to a string is by using the decode() method, which interprets the bytes as a specific encoding and returns a string:

# Convert bytes to string using decode()  
bytes_data = b'Hello, World!'  
string_data = bytes_data.decode('utf-8')  
print(string_data)  