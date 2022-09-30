import requests
import json

def sms(shomare,code):
    url = "https://api.sms.ir/v1/send/bulk"

    payload = json.dumps({
        "lineNumber": 30007732003190,
        "messageText": f"کد تایید ورود به سایت بیمه : {code}",
        "mobiles": [
            shomare,
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

