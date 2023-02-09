import requests

url = 'http://localhost:9200/btrc_docs/_search'

headers = {'Content-Type': 'application/json'}

auth = ("", "") #Elasticsearch Username & Password

response = requests.get(url, auth=auth, headers=headers)
print(response.text)