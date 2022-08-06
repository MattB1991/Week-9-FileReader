

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
    
    directory =input('Enter the directory for the file.'' ')
    if directory =='':
        directory ='.'
    filename = input('Enter the file name.'' ')
    time.sleep(1)
    name = input('What is your name?'' ')
    time.sleep(1)
    address = input('What is you full address?'' ')
    time.sleep(1)
    phone =input('What is you phone number?'' ')
    time.sleep(2)
    
    try:
        with open("{}/{}.txt".format(directory, filename), 'w') as file:
          file.write(",".join([name]))
          file.write(",".join([address]))
          file.write(",".join([phone]))

        with open("{}/{}.txt".format(directory, filename), 'r') as file:
          print("{}/{}.txt contents".format(directory, filename))
          for line in file:
            print(line)
            time.sleep(1)
            print('Nice! The file was created and named {}!'.format(filename))
    except:
        print('This directory does not exist')
        print("Let's try that again")
        main()
        
    uanswer = input('Was this information correct?''(Yes or No)'' ')
    answer = uanswer.title()
    if answer == 'Yes':
        print('Great!')
    else:
        print("Let's correct that! One moment while I restart the program...")
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        main()    

main()
