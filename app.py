import json, requests
from requests.auth import HTTPBasicAuth

API_TOKEN = "replace-this-with-your-api-token"
BASE_URL = "replace-this-with-your-institutions-link"
EMAIL = "replace-this-with-your-email"
HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

auth = HTTPBasicAuth(EMAIL, API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

def create_jira_issue(summary, description, projectKey, issue):
    payload = json.dumps({
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": description,
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    }
                ],
                "type": "doc",
                "version": 1
            },
            "issuetype": {
                "name": issue
            },
            "project": {
                "key": projectKey
            },
            "summary": summary,
            
        },
        "update": {}
    })

    response = requests.post(
        f"{BASE_URL}/rest/api/3/issue",
        data=payload,
        headers=headers,
        auth=(EMAIL, API_TOKEN)
    )

    if response.status_code == 201:
        print("Issue created successfully!")
        print(response.json())
    else:
        print("Issue creation failed.")
        print(response.text)

summary="Insert Summary Here"
description = "Insert Description Here"
projectKey = "Insert Project Key Here"
issue = "Insert Project Key Here"
create_jira_issue(summary, description, projectKey, issue)
