# Comando para identificar os campos de uma fase no pipefy


payload = {"query": "query{   phase(id:317129403){     cards{       edges{         node{           id  title     fields {field {id index_name description}}    }       }     }   } }"}


# Comando para criar um card atraves do python

import requests

url = "https://api.pipefy.com/graphql"

payload = {"query": "mutation {  createCard(input: {   pipe_id: 302751447,   title: \"card muito muit o legal\", fields_attributes:[ {field_id: \"assunto\", field_value: \"Texto de assunto\"},{field_id: \"texto_longo\", field_value: \"muito texto\"} ]} ) {   card { title conteudo }  } }"}


headers = {

"accept": "application/json",

"content-type": "application/json",

"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozMDIwODg1NjcsImVtYWlsIjoibWF0aGV1cy5zaWx2YUBzcHRlY2guc2Nob29sIiwiYXBwbGljYXRpb24iOjMwMDIxMzMwOX19.iZPooHUDHJBA1-dXDlzzEYVtmzKAPCIHK0YuY0-IwePMeQobX04Y_g_TM_2nrcR1m7f0oTof9Ey2irE6E1jnnA"

}

response = requests.post(url, json=payload, headers=headers)

print(response.text)