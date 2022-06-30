import requests
import json
from masterfile import auth

issueIdOrKey = "SSP-5"

url = f"https://drdecker100.atlassian.net/rest/api/3/issue/{issueIdOrKey}"   

headers = {"Accept": "application/json"}

response = requests.request("GET",url,headers=headers,auth=auth)

def get_issue(resp): # fetch issue with key or id  https://developer.atlassian.com/cloud/jira/platform/rest/v3/
    res = json.dumps(json.loads(resp.text), sort_keys=True, indent=4, separators=(",", ": "))
    res_d = json.loads(res)      #convert json to dict
    return res_d

def check_if_attachment_exist(): # check if issue has attachment
    res_d = get_issue(response)
    if res_d["fields"]["attachment"]:
        return True
    return False

def get_attachments():           # fetch all atachments
    if check_if_attachment_exist():
        res_d = get_issue(response)
        metadata = res_d["fields"]["attachment"]

        for i, v in enumerate(metadata):
            attachment = res_d["fields"]["attachment"][i]
            content_url = attachment["content"]
            filename = attachment["filename"]
            res_b = requests.get(content_url, auth=auth)
            with open(filename, 'wb') as f:
                f.write(res_b.content)
                print(f"{filename} downloaded to local machine")
        
    else:
        print("No attachment to this issue")
   

# call functions
get_issue(response)
get_attachments()
