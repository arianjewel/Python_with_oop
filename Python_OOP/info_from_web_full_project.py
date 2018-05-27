'''import os

dir_name='dimik_pub'
os.mkdir(dir_name)'''





import re
import os
import requests
import sys

def create_dir(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print(name,'already exist')

def write_book_info(book_name,url,file_name):
    print('your book info is writting')
    with open(file_name,'w',encoding=response.encoding) as f:
        f.write(name+'\n')
        f.write(url)

def downlaod_image(img_url,file_name):
    print('downlaoding image')
    r=requests.get(img_url)

    with open(file_name,'wb') as f:
        f.write(r.content)

def get_dir_name(reg_ex,url):
    result=re.findall(reg_ex,url)
    dir_name='_'.join(result[0])
    return dir_name

def process():
    create_dir(main_dir)



main_dir='dimik_pub'

url='http://dimik.pub'
response=requests.get(url)
if response.ok is False:
    sys.exit('could not get response from server')
page_content=response.text

reg_ex=re.compile(r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)".*?<h2 class="sd-title">\s*<a.*?>(.*?)<',re.S)
result=re.findall(reg_ex,page_content)

dir_reg_ex=re.compile(r'book/(\d+)/(\w+)-(\w+)-')

for item in result:
    name=item[2]
    url=item[0]
    img_url=item[1]

    dir_name=main_dir+'_'+get_dir_name(dir_reg_ex,url)
    create_dir(dir_name)

    file_name=dir_name+'_'+'info.txt'
    write_book_info(name,url,file_name)

    img_file_name=dir_name+'_'+'image.jpg'
    downlaod_image(img_url,img_file_name)


if __name__=='__main__':
    process()
