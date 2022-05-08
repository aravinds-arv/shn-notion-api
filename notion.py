
import json
import requests

class NotionClient:

    def __init__(self,token,database_id):
        self.database_id = database_id
        self.token = token

        self.headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json",
        "Authorization": "Bearer "+token
        }

    def create_page(self,description,date,status):
        create_url = "https://api.notion.com/v1/pages"

        data = {
        "parent": { "database": self.database },
        "properties": {
            "NO": {
                "number": [
                    {
                        "text": {
                            "content": description
                        }
                    }
                ]
            },
            "Description": {
                "title": [
                    {
                        "text": {
                            "content": description
                        }
                    }
                ]
            },
            "Date": {
                "date": {
                            "start": date,
                            "end": None
                        }
            },
            "Status": {
                "rich_text": [
                    {
                        "text": {
                            "content": description
                        }
                    }
                ]
            }
        }}


        data = json.dumps(data)
        res = requests.post(create_url,headers=self.headers,data=data)
        print(res.status_code)
        return res
