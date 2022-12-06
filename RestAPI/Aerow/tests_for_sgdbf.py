import requests, json

url_sgdbf_dev = "http://sgdbf.aerowteam.com/OTCS/cs.exe"
url_auth = "/api/v1/auth"
url_apiinfo = "/api/v1/apiinfo"

# Get ticket
params = {"username" : "User-test-DSI", "password" : "zAi.U;)ZbaGr+[RNq>xGg[3Li oogn|rFK?:"}
response = requests.post(url_sgdbf_dev+url_auth, data=params, verify=False)
ticket = json.loads(response.content)["ticket"]
print(ticket) # Youhou

# Get ApiInfo
header = {"OTCSTicket" : ticket}
params = {"resource" : "api/v1/nodes/2000/nodes"}
response = requests.get(url_sgdbf_dev+url_apiinfo, headers = header, params = params, verify=False)
data = json.loads(response.content)#["ticket"]
print(data) # Youhou

# POST - upload a file in Enterprise (2000)

# Search a final folder