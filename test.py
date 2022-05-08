import requests
  
# initialize a session
session = requests.Session()
  
# send a get request to the server
response = session.get('http://notion.so')
  
# print the response dictionary
print(session.cookies.get_dict())