# The goal is to create a program that generates a random and secure password, then saves it to a text file.

# Create a function 'password_generator' which has the parameter : 'password_long'
# use the module random and string to generate the password
# save it in a file along the previous passwords. (default file, but can be on specific file) (Use 'a')
# use argparse to take the passwords_long 
# add argparse, logging and Path modules too
## try match

import argparse, logging
from pathlib import Path

class PWD_generator:
    print('PWD generator class start')
    defaultFilePath = ''
    def __init__(self, pwdLong=12, save=False, filePath='myfile'):
        print('constructor start')
        self.pwdLong = pwdLong
        self.save = save
        self.filePath = filePath
        
    def get_new_pwd(self):
        return 'run'


def parser():
    parser = argparse.ArgumentParser(description='lvl1 secure password generator')

    parser.add_argument('--pwdLong', dest='pwdLong', help='password long', required=False)
    parser.add_argument('--save', dest='save', help='want to save it', required=False)
    parser.add_argument('--filePath', dest='filePath', help='file path', required=False)

    return parser.parse_args()


if __name__ == '__main__':
    args = parser()
    print(args)
    if args.pwdLong and args.save and args.filePath:
        print('pwd save and file')
    elif args.pwdLong and args.save:
        print('pwd and save')
    elif args.pwdLong:
        print('pwd')
    else:
        print('no')
        quit()