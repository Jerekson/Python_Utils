selection = input("select convertion \n\
char to ascii (1) \n\
ascii to char (2) \n\
")

if selection == "1" : # Char to Ascii
    result = ""
    theReturn = input("enter chars (separated by a simple ',' \n")
    chars = theReturn.split(",")
    for it in chars:
        char = int(it)
        result += chr(char)
    print(result)
elif selection == "2" : # Ascii to char
    result = ""
    asci = input("enter ascii \n")
    for i in asci:
        result += str(ord(i))+","
    print(result[:-1])
else: 
    print("nothing selected")
