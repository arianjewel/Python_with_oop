import re
import requests
import sys

url='http://dimik.pub'
response=requests.get(url)
if response.ok is False:
    sys.exit('could not get response from server')
page_content=response.text

reg_ex=re.compile(r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)".*?<h2 class="sd-title">\s*<a.*?>(.*?)<',re.S)
result=re.findall(reg_ex,page_content)

for item in result:
    print('Book Name:',item[2])
    print('URL:',item[0])
    print('Image:',item[1])
    print('')





'''with open('cricket_team.html','r') as f:
    html=f.read()

import re

pat=re.compile(r'<li>\s*(.+?)\s*<ol>\s*<li>(.+?)</li>\s*<li>(.+?)</li>')
result=pat.findall(html)
with open('cricket_team.txt','a') as f:
    for item in result:
        f.write(item[0]+' - '+item[1]+', '+item[2]+'\n')'''




'''import re

with open('player name.html','r') as f:
    file=f.read()

li=re.findall(r'<li>\s*(\w+)\s*.+\s*<li>(.+?)</li>\s*<li>(.+?)</li>',file)
for tup in li:
    print(tup[0]+' - '+tup[1]+', '+tup[2])'''
