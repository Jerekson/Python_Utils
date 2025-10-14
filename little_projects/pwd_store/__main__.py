import logging, argparse
from .utils.logging_config import logging_setup

print("auto start __main__ and have to run PWD_generator")



def parser():
    parser = argparse.ArgumentParser(description='lvl1 secure password generator')

    parser.add_argument('--pwdLong', dest='pwdLong', help='password long', required=False)
    parser.add_argument('--save', dest='save', help='want to save it', required=False)
    parser.add_argument('--filePath', dest='filePath', help='file path', required=False)

    return parser.parse_args()


if __name__ == "__main__":
	print("I'm main")
	print(logging_setup())
	
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