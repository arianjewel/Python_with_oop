
'''import requests
url='http://subeen.com/allpost/'
response=requests.get(url)
print(type(response))
print(dir(response))
print(response.ok)                          #for right webaddress
print(response.status_code)
print(response.reason)'''




'''import requests
res=requests.get('http://dimikcomputing.com/abc.html')
print(res.ok)                               #for wrong webaddress
print(res.reason)
print(res.status_code)'''



import requests
res=requests.get('http://example.com')
print(res.text)                           #show html code
print(type(res.text))
