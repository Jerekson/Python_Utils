# The goal is to create a program that generates a random and secure password, then saves it to a text file.

# Create a function 'password_generator' which has the parameter : 'password_long'
# use the module random and string to generate the password
# save it in a file along the previous passwords. (default file, but can be on specific file) (Use 'a')
# use argparse to take the passwords_long 
# add argparse, logging and Path modules too

import argparse, logging
from pathlib import Path

def start():
    #args = parser()
    
       

def parser():
    parser = argparse.ArgumentParser(description='Directories Enumerator.')

    parser.add_argument('-pwd-long', dest='wdPath', help='WordList Path', required=True)
    parser.add_argument('--save-file-path', dest='tls', help='https True or False?', default='True')

    return parser.parse_args()

start()