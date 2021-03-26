import urllib.request
import urllib.parse

key = 'V/eW+6qrm60-Bw8qAXFEKBlvbeOwyrVmMQD5AGl2f5'

import requests
import json

def sendotp(apikey, numbers,otp_generated):
    data = urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,'sender':'RADEON',
                                   'message': 'Dear Customer ,Please use the otp {} to login into your Rade onn Account.Never share otp with anyone else.'.format(otp_generated),})
    data = data.encode('utf-8')
    try:
        request = urllib.request.Request("https://api.textlocal.in/send/?")
        urllib.request.urlopen(request, data)

        return True
    except:
        return False

def property_added_message(apikey,numbers,property_id,percentage,view_link):
        percentage =int(float(percentage))
        # print(apikey,numbers,property_id,percentage,view_link)
        abc =' '
        data = urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers, 'sender': 'RADEON',
                                       'message': 'Hi {} congrats! Your Ad is successfully posted. Get more response for your Ad update more details with Photos {} '.format(abc,view_link), })
        data = data.encode('utf-8')
        # print('-------------------------------------------------------------------------------------------------------')
        try:
            request = urllib.request.Request("https://api.textlocal.in/send/?")
            response =urllib.request.urlopen(request, data)
            response=response.read()
            # print(response)
            return True
        except:
            return False

def short_url(link):
    linkRequest = {
      "destination": link
      , "domain": { "fullName": "rebrand.ly" }
    }
    requestHeaders = {
      "Content-type": "application/json",
      "apikey": "aa45e7d637a144f48250208128354fd4",
      "workspace": "a7d711c6900949eab78127548f52af0d"
    }
    r = requests.post("https://api.rebrandly.com/v1/links",
        data = json.dumps(linkRequest),
        headers=requestHeaders)
    print(r.json())
    if (r.status_code == requests.codes.ok):
        link = r.json()
        print(link)

    return  str(link["shortUrl"])
#
# abc = short_url('https://www.radeonn.com/')
# print(abc)

# for i in range(0,1200):
#     message = property_added_message(key, numbers='9815047274', property_id=10, percentage=10,view_link=' http://127.0.0.1:8000/login_with_mailer/?email=hazoor@webtunix.com&next=/property_edit/36')

