#Elasticsearch DELETE request
import requests

url = "http://localhost:9200/btrc_docs"

headers = {'Content-Type': 'application/json'}

auth = ("", "") #Elasticsearch Username & Password)

response = requests.delete(url, auth=auth, headers=headers) 
print(response.status_code)
print(response.text)