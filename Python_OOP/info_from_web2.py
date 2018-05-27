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
