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
import json
import time

def main():
    name = input('What is your name?'' ')
    address = input('What is your Address?'' ')
    phone = input('What is your phone number?'' ')
    filePath = input('What directory do you want to search?'' ')
    fileName = input('What file am I looking for?'' ')
    completePath = filePath+fileName

    try:
        with open('filename') as file_object:
            for line in file_object:
                print(line)
        
    except FileNotFoundError:
        unewfile = input('That file does not seem to exist! Would you like to create it?')
        newfile = unewfile.upper()
        if newfile == 'YES':
            with open(fileName, 'w') as f:
                json.dump(name, f)
                json.dump(address, f)
                json.dump(phone, f)
                print('Your file was created!')
                
        else:
            print('Have a great day! Program will close.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            exit()
    
    restart = input('Would you like to do another?')
    if restart == 'Yes':
        main()
    else:
        print('Have a great day!')
        time.sleep(2)
        exit()
main()
