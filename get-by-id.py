#Elasticsearch GET request

import requests

url = 'http://localhost:9200/btrc_docs/_search'

headers = {'Content-Type': 'application/json'}

auth = ("", "") #Elasticsearch Username & Password

query = {
    "query": {
        "match": { "_id": "10D4FYYB3z34O_b0iU2-" }
    }
}
 
response = requests.get(url, auth=auth, headers=headers, json=query) 
print(response.json())