import logging, argparse
from .utils.logging_config import logging_package_setup

print("auto start __main__ and have to run PWD_generator")
LOG_LEVEL_FROM_ARGS = logging.DEBUG # if it call with -v for verbose -> DEBUG else INFO 

def parser():
    parser = argparse.ArgumentParser(description='lvl1 secure password generator')

    parser.add_argument('--pwdLong', dest='pwdLong', help='password long', required=False)
    parser.add_argument('--save', dest='save', help='want to save it', required=False)
    parser.add_argument('--filePath', dest='filePath', help='file path', required=False)

    return parser.parse_args()


if __name__ == "__main__":
	print("I'm main")
	# logging_package_setup()

    logging_package_setup(level=LOG_LEVEL_FROM_ARGS)
    
	
	'''
	args = parser()
	print(args)
	if len(sys.argv) == 1:
		print("0 args")
	elif args.pwdLong and args.save and args.filePath:
		print('pwd save and file')
	elif args.pwdLong and args.save:
		print('pwd and save')
	elif args.pwdLong:
		print('pwd')
	else:
		print('You have to enter at least a password longer at "-pwdLong" \n"--save" and "--filePath" are facultative but "filePath" need "save"')
		quit()
	'''