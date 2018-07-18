import os
import requests
import re
import sys

def create_dir(name):
    print('creating directory',name)
    try:
        os.mkdir(name)
    except Exception as e:
        print(e)

def down_image(img_url,file_name):
    print('downloading image!')
    r=requests.get(img_url)

    with open(file_name,'wb') as f:
        f.write(r.content)

def save_book_info(book_name,book_url,file_name):
    print('saving '+book_name+' info')
    with open(file_name,'w',encoding='utf-8') as f:
        f.write(book_name)
        f.write('\n')
        f.write(book_url)

def get_dir_name(reg_exp,url):
    result=re.findall(reg_exp,url)
    dir_name='_'.join(result[0])
    return dir_name

def process():
    #create home directory
    create_dir(main_dir)



if __name__=='__main__':

    main_dir='dimik_pub'

    process()

    url='http://dimik.pub/'

    res=requests.get(url)

    if res.ok is False:
        sys.exit('couldn\'t get response from server')

    page_cont=res.text
    new_page_cont=page_cont.replace('\n',' ')

    pat=re.compile(r'<div class="book-cover">\s*<a.+?"(.+?)">.+?"(.+?)">.+?<h2.+?<a.+?>(.+?)<')

    result=re.findall(pat,new_page_cont)

    dir_pat=re.compile(r'book/(\d+)/(\w+)-(\w+)-')

    for item in result:
        name=item[2]
        url=item[0]
        img_url=item[1]

        dir_name=main_dir+'/'+get_dir_name(dir_pat,url)
        create_dir(dir_name)

        file_name=dir_name+'/info.txt'
        save_book_info(name,url,file_name)

        img_file_name=dir_name+'/image.png'
        down_image(img_url,img_file_name)
