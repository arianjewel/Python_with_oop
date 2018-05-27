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
