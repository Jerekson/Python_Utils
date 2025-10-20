# The goal is to create a program that generates a random and secure password, then saves it to a text file.

# Create a function 'password_generator' which has the parameter : 'password_long'
# use the module random and string to generate the password
# save it in a file along the previous passwords. (default file, but can be on specific file) (Use 'a')
# use argparse to take the passwords_long 
# add argparse, logging and Path modules too
## try match

import logging, sys, secrets, string
from pathlib import Path
from .bdd import SQL_config

log = logging.getLogger(__name__)

class PWD_generator:
    def __init__(self, pwdLong=12):
        log.debug("PWD_generator instance created")
        self.pwdLong = pwdLong
        
    def get_new_pwd(self):
        log.debug("get_new_pwd methode start")
        # Define the character sets
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password_length = self.pwdLong # Set the desired password length

        # Generate a strong password
        password = ''.join(secrets.choice(alphabet) for _ in range(password_length))
        return password