'''
FileReader.py

Matthew Bell
08/02/2022
CIS245
Assignment 9.1
Requirements:
This week we will create a program that performs file processing activities.
Your program this week will use the OS library in order to validate that
a directory exists before creating a file in that directory. Your program
will prompt the user for the directory they would like to save the file in as
well as the name of the file. The program should then prompt the user for their
name, address, and phone number. Your program will write this data to a comma
separated line in a file and store the file in the directory specified by the
user. 
Once the data has been written, your program should read the file you just
wrote to the file system and display the file contents to the user for
validation purposes. 
Submit a link to your Github repository.
'''
import os

filePath = input('What directory do you want to search?')
fileName = input('What file am I looking for')
completePath = filePath+fileName

try:
    if os.path.isfile(fileName):
        print('File Exists')
    if os.path.isdir(filePath): 
        print('Directory Exists')
    if os.path.exists(completePath): 
        print('Complete path exists')
        print('Complete Path',completePath)
    with open(completePath, 'w') as fileHandle: 
        fileHandle.write(input('What is your name?')
        fileHandle.write(input('What is your address?')
        fileHandle.write(input(' What is your phone number?')
    with open(completePath, 'r') as fileHandle: 
        data = fileHandle.read() 
        print(data)
except FileNotFoundError:
    
