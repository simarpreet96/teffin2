# key
# V/eW+6qrm60-L1B4rHl4H7sbrjkBjeA0eX5DSVV8vn
import json
import urllib.request
import urllib.parse
import random
n = random.randint(0,22)
print(n)
import random
import math

## storing strings in a list
digits = [i for i in range(0, 10)]

## initializing a string
random_str = ""

## we can generate any lenght of string we want
for i in range(5):
    index = math.floor(random.random() * 10)
    random_str += str(digits[index])



## displaying the random string
print(random_str)
# key = '6QhtKzS71RQ-FPiYTJYl4W5IeyH6CfDq32Q6hKo8vu'
key = 'V/eW+6qrm60-Bw8qAXFEKBlvbeOwyrVmMQD5AGl2f5'

# print(type(key))
# def sendSMS(apikey, numbers):
#     otp_genrated=random.randint(0, 22)
#     data = urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,'sender':'RADEON',
#                                    'message': 'Thankyou for registering with Rade onn\r\n\r\nOTP- {}'.format(otp_genrated),})
#     data = data.encode('utf-8')
#     request = urllib.request.Request("https://api.textlocal.in/send/?")
#     f = urllib.request.urlopen(request, data)
#     fr = f.read()
#     return (fr)
#
#
# resp = sendSMS(key, '8437379367'
#                 )
# print(resp)

# def getTemplates(apikey):
#     data = urllib.parse.urlencode({'apikey': apikey})
#     data = data.encode('utf-8')
#     request = urllib.request.Request("https://api.textlocal.in/get_templates/?")
#     f = urllib.request.urlopen(request, data)
#     fr = f.read()
#     return (fr,type(fr))
#
#
# resp = getTemplates(key)
# print(resp)






#
#
# def Balance(apikey):
#     data = urllib.parse.urlencode({'apikey': apikey})
#     data = data.encode('utf-8')
#     request = urllib.request.Request("https://api.textlocal.in/balance/?")
#     f = urllib.request.urlopen(request, data)
#     fr = f.read()
#     return (fr)
#
#
# resp = Balance(key)
# print(resp)



data = urllib.parse.urlencode({'apikey': key, 'numbers': '9779018605','sender':'RADEON',
                                   'message': 'Thankyou for registering with Rade onn\r\n\r\nOTP- {}'.format(random_str),})
data = data.encode('utf-8')
request = urllib.request.Request("https://api.textlocal.in/send/?")
urllib.request.urlopen(request, data)