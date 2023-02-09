#Elasticsearch Kibana POST Bulk Upload

import os
import glob
import PyPDF2
import pandas as pd
from elasticsearch import Elasticsearch

username = "" #Elasticsearch Username
password = "" #Elasticsearch Password

os.chdir("Documents")
files = glob.glob("*.*")

#PDF extraction function
def extractPdfFiles(files):
    this_loc = 1
    df = pd.DataFrame(columns=("name", "content"))

    
    for file in files:
        pdfFileObj = open(file, "rb")
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        n_pages = len(pdfReader.pages)
        this_doc = ''
        for i in range(n_pages):
            pageObj = pdfReader.pages[i]
            this_text = pageObj.extract_text()
            this_doc += this_text
        df.loc[this_loc] = file, this_doc
        this_loc = this_loc + 1
    return df

#Elasticsearch connection
es = Elasticsearch(["http://" + username + ":" + password + "@localhost:9200"])

index_name = 'btrc_docs'
body = {
    "settings": { 
        "number_of_shards": 1,  # No shards 
        "number_of_replicas": 0  # No replicas 
    } 
} 
  
# Create index request with no shards and replicas  
es.indices.create(index=index_name, body=body)

#Extract documents
df = extractPdfFiles(files)
col_names = df.columns
for row_number in range(df.shape[0]):
    for name in col_names:
        
        #body = dict([name, str(df.iloc[row_number][name])])
        body = {name: str(df.iloc[row_number][name])}
        
        es.index(index = "btrc_docs", document= body)