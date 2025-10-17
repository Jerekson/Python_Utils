# The goal is to create a program that generates a random and secure password, then saves it to a text file.

# Create a function 'password_generator' which has the parameter : 'password_long'
# use the module random and string to generate the password
# save it in a file along the previous passwords. (default file, but can be on specific file) (Use 'a')
# use argparse to take the passwords_long 
# add argparse, logging and Path modules too
## try match

import logging, sys
from pathlib import Path

print("test import log ? ")

class PWD_generator:
    print('PWD generator class start')
    defaultFilePath = ''
    def __init__(self, pwdLong=12, save=False, filePath='myfile'):
        print('constructor start')
        self.pwdLong = pwdLong
        self.save = save
        self.filePath = filePath

        # config log?
        
    def get_new_pwd(self):
        return 'get new pwd def start'

def configLog():
    pass

if __name__ == '__main__':
    pass