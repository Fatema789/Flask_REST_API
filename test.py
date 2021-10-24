import requests

BASE="http://127.0.0.1:5000/"
response=requests.get(BASE+"/info")
response=requests.post(BASE+"/info")
response=requests.get(BASE+"/info/Fatema")
#response=requests.get(BASE+'/info/0')
response=requests.put(BASE+'/info/0',{"name":"box","num":10})
print(response.json())
response=requests.delete(BASE+'/info/0')
print(response)
