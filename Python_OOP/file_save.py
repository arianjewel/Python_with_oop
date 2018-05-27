#html code save as a file
'''import requests
response=requests.get('http://dimikcomputing.com')
with open('dimik.html','w',encoding=response.encoding) as f:
    f.write(response.text)'''




#hmtl code save, file directory store and open in web browser
'''import requests
import os
import webbrowser as wb

response=requests.get('http://dimikcomputing.com')

file_name='dimik.html'
with open(file_name,'w',encoding=response.encoding) as f:
    f.write(response.text)

file_path=os.path.realpath(file_name)
print(file_path)
wb.open('file://'+file_path)'''




#image download from web page
'''import requests

img_url='https://goo.gl/PsibBu'

r=requests.get(img_url)


with open('pybook1.jpg','wb') as f:
    f.write(r.content)'''



'''import requests

img_url=input()
r=requests.get(img_url)

file_name=input()

with open(file_name+'.png','wb') as f:
    f.write(r.content)'''




'''import requests
import sys

img_url=sys.argv[1]
file_name=sys.argv[2]
mode=sys.argv[3]
r=requests.get(img_url)

with open(file_name,mode) as f:
    f.write(r.content)'''





#download a pdf book from a website
'''import requests
import sys

base_url='http://subeen.com/download/'
info_dt= {'name': 'Jewel','email':'arianjewel@gmail.com','country':'Bangladesh'}

url=base_url+'process.php'

response=requests.post(url,data=info_dt)

if response.ok is False:
    sys.exit('Error downloading the file..')

with open('cpbook.pdf','wb') as f:
    f.write(response.content)

print('Book download complete')'''




#save how much line i wanna write
'''while True:
    inp=input('write something to your file (0 for exit): ')
    if inp=='0':
        break
    else:
        with open('file.txt','a') as f:
            f.write(inp+"\n")'''



'''lines=['This is first line','This is second line','This is third line']

with open('file.txt','w') as f:
    for line in lines:
        f.write(line+'\n')'''



#save country alphabetically from country_name.txt
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open('country_name.txt','r') as f:
    country_list=f.readlines()
    for country in country_list:
        for i in alphabet:
            if country.startswith(i):
                with open('country_'+i+'.txt','a') as fb:
                    fb.write(country)
                    break
