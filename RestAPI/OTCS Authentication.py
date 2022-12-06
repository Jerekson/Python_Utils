import requests
"""
# Authentication
url_Server = "https://knowledge.opentext.com/knowledge/cs.dll"
url_Auth = "/api/v1/auth"
username = ""
password = ""
token = "6884523805093773312"
header = {
    'Authorization': 'token {}'.format(token)
}
response = requests.get(url_Server + url_Auth, headers=header)

print(response.status_code) # response.json(), 
"""

# Download a file 
url_Server = "https://knowledge.opentext.com/knowledge/cs.dll/open/79098147"
url_Auth = "/api/v1/auth"
username = ""
password = ""
token = "6884523805093773312"
header = {
    'Authorization': 'token {}'.format(token)
}
response = requests.get(url_Server, headers=header)

print(response.status_code, response.json()) # ,response.json()


# open('facebook.ico', 'wb').write(r.content)