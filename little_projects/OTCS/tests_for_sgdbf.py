import requests, json

url_sgdbf_dev = "http://sgdbf.aerowteam.com/OTCS/cs.exe"
url_auth = "/api/v1/auth"
url_apiinfo = "/api/v1/apiinfo"
url_search = "/api/v2/search"
url_createNode = "/api/v1/nodes"

# Get ticket (Authentication)
params = {"username" : "User-test-DSI", "password" : "zAi.U;)ZbaGr+[RNq>xGg[3Li oogn|rFK?:"}
response = requests.post(url_sgdbf_dev+url_auth, data=params, verify=False)
ticket = json.loads(response.content)["ticket"]
#print(ticket) # Youhou

"""
# Get ApiInfo
header = {"OTCSTicket" : ticket}
params = {"resource" : "api/v1/nodes/2000/nodes"}
response = requests.get(url_sgdbf_dev+url_apiinfo, headers = header, params = params, verify=False)
data = json.loads(response.content)#["ticket"]
print(data) # Youhou
"""

# Search Business Workspace ID
params = {"where" : "B1321777", "limit" : 1}
header = {"OTCSTicket" : ticket}
response = requests.post(url_sgdbf_dev+url_search, headers=header, data=params, verify=False)
bwsID = json.loads(response.content)["results"][0]["data"]["properties"]["id"]
#print(bwsID)

# Search a final folder from BWS
params = {"where" : "Accidents de travail", "limit" : 1, "within" : bwsID}
header = {"OTCSTicket" : ticket}
response = requests.post(url_sgdbf_dev+url_search, headers=header, data=params, verify=False)
folderID = json.loads(response.content)["results"][0]["data"]["properties"]["id"]
#print(folderID)

# POST - create folder in a BWS
params = {"type" : 0, "parent_id" : folderID, "name" : "test create folder with RestAPI doc"}
header = {"OTCSTicket" : ticket}
response = requests.post(url_sgdbf_dev+url_createNode, headers=header, data=params, verify=False)
folderID = json.loads(response.content)
print(folderID)

# POST - upload file in a BWS
