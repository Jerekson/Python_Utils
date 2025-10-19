import logging, argparse, sys
from .utils.logging_config import logging_package_setup
from .bdd import SQL_config

def parser():
    parser = argparse.ArgumentParser(description="""Password Generator""")

    parser.add_argument("--pwdLong", dest="pwdLong", help="password long", required=False)
    parser.add_argument("--save", dest="save", action="store_true", help="if you want to save it in the default DB", required=False)

    # mode verbose
    parser.add_argument("-v", "--verbose", action="store_true", help="mode verbose for logs level DEBUG")

    return parser.parse_args()

def main():
	args = parser()

	if args.verbose:
		log_level = logging.DEBUG
	else:
		log_level = logging.INFO

	logging_package_setup(level=log_level)
	log = logging.getLogger("little_projects.pwd_store")
	log.debug("main firsts config done with theses args -> %s", args)

	# Generate a password

	# Save it or print it
	if args.save:
		log.debug("save was selected, need DB instantiation")
		SQL_config()
	else:
		pass # pprint the password here

if __name__ == "__main__":
	main()
	