import requests
import json

url = "https://api.sms.ir/v1/send/bulk"

payload = json.dumps({
    "lineNumber": 30007732003190,
    "messageText": " hi Omid",
    "mobiles": [
        "9306615521",
        "9022069032",
        '9053172724'
    ],
    "sendDateTime": None
})
headers = {
    'Content-Type': 'application/json',
    'Accept': 'text/plain',
    'x-api-key': 'FlFvdJvGfSzddemIoY7PwjIFQ1xDUzNvrn83gjyBiqXHypZyKfeWlvfsCzT8SZVf'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

