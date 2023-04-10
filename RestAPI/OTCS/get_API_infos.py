import requests, json

url_sgdbf_dev = "http://sgdbf.aerowteam.com/OTCS/cs.exe"
url_apiinfo = "/api/v1/apiinfo"

# Prerequisites
# Get the OTCS Ticket (cf. auth)

# Get ApiInfo
header = {"OTCSTicket" : ticket}
params = {"resource" : "api/v1/nodes/2000/nodes"}
response = requests.get(url_sgdbf_dev+url_apiinfo, headers = header, params = params, verify=False)
data = json.loads(response.content)#["ticket"]
print(data) # Youhou

# POST - upload a file in Enterprise (2000)

# Search a final folder