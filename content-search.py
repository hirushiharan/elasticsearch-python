#Elasticsearch Content search

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

username = "" #Elasticsearch Username
password = "" #Elasticsearch Password

# Connect to the Elasticsearch instance
es = Elasticsearch(["http://" + username + ":" + password + "@localhost:9200"])

# Create a Search object and set the query to search for Kibana content 
s = Search(using=es).query("match", content="Bangladesh") 

# Execute the search and print out the results 
response = s.execute() 
print(response)