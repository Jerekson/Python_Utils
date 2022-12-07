import requests, json

url_sgdbf_dev = "http://sgdbf.aerowteam.com/OTCS/cs.exe"
url_auth = "/api/v1/auth"

# Get ticket (Authentication)
params = {"username" : "User-test-DSI", "password" : "zAi.U;)ZbaGr+[RNq>xGg[3Li oogn|rFK?:"}
response = requests.post(url_sgdbf_dev+url_auth, data=params, verify=False)
ticket = json.loads(response.content)["ticket"]
print(ticket)

# Fill the properties file to change the value for the key "OTCSTicket"
