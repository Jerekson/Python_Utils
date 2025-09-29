from pathlib import Path

p = Path(".")
for x in p.iterdir():
	#print(x)
	if x.is_dir(): #if x it's a directory
		#print(x)
		continue

# list all .py file in the tree structure
allpy = list(p.glob("**/*.py"))

# get dir and a files then check if they exists
mydir = Path("./Learning")
inmydir = mydir / 'advanced_python' / 'classherit.py'
inmydir2 = mydir / 'blabla'
'''
print(mydir, '\n', mydir.exists())
print(inmydir, '\n', inmydir.exists())
print(inmydir2, '\n', inmydir2.exists())
'''

# open and read a file
with Path("./tmp.py").open(encoding="utf-8") as f:
	#print(f, "\n", f.readline(), "\n",f.read())
	pass

# get absolute path
absolutePath = Path("tmp.py").resolve()
#print(absolutePath)

# write in file but it will erase the actual file content
tmpfile = Path("./tmp.py")
# tmpfile.write_text("Hello world from pathlib")