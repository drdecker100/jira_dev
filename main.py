# https://developer.atlassian.com/cloud/jira/platform/rest/v3/
import requests
import json
from masterfile import auth

issueIdOrKey = "SSP-5"

def check_response_valid():         # check if response is valid
    url = f"https://drdecker100.atlassian.net/rest/api/3/issue/{issueIdOrKey}"   
    headers = {"Accept": "application/json"}
     
    response = requests.request("GET",url,headers=headers,auth=auth)
    return response

def get_issue():                     # fetch issue with key or id  
    resp = json.dumps(json.loads(res.text), sort_keys=True, indent=4, separators=(",", ": "))
    response = json.loads(resp)      # convert json obj to dict
    return response

def check_if_attachment_exist():     # check if issue has attachment
    if res_d["fields"]["attachment"]:
        return True
    return False

def get_attachments():               # fetch all atachments
    if check_if_attachment_exist():
        metadata = res_d["fields"]["attachment"]

        for _, attachment in enumerate(metadata):          
            content_url = attachment["content"]
            filename = attachment["filename"]
            res_b = requests.get(content_url, auth=auth)
            with open(filename, 'wb') as f:
                f.write(res_b.content)
                print(f"{filename} downloaded to local machine")
        
    else:
        print("No attachment to this issue")

def get_issue_metadata():
    pass

             
# Call function
res = check_response_valid()
if res.status_code == 200:
    print(f"Response status code: {res.status_code}")
    res_d = get_issue()
    get_attachments()
else:
    print(f"Response status code: {res.status_code}")
