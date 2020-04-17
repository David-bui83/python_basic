# Python has functions for creating, reading, updating, and deleting files.

#Open a file --> if file doesn't exist, it will create one
myFile = open('myfile.txt', 'w')

# Get come info
print('Name: ', myFile.name)
print('is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.text', 'a')
myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile.open('myfile.txt', 'r+')
text = myFile.read(10)
print(text)