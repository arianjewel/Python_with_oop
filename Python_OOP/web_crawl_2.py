import logging
import sys
import requests
import re
import csv
from html import unescape

def get_page_content(url):
    """get_page_content takes a url and returns the
    content of the page"""
    try:
        res=requests.get(url)

    except Exception as e:
        logging.error(e)

    if res.ok:
        cont=res.text
        content=cont.replace("\n"," ")
        return content
    logging.error("can't get content from url: "+url)
    return None


def get_category_list(content):
    """get_category_list takes content of home page
    and return a list of categories and their url"""

    return category_pat.findall(content)


def get_book_list(content):
    """get_book_list takes content of a book list page
    and return a list of books(name and url)"""

    return book_pat.findall(content)


def get_product_details(content):
    """get_product_details takes content of a product page,
    parses the page and return details about a product"""

    result=img_pat.findall(content)
    if len(result)==0:
        logging.warn("Image URL not founded!")
        img_url=""
    else:
        img_url=result[0]

    result=desc_pat.findall(content)
    if len(result)==0:
        logging.warn("Description not founded!")
        desc=""
    else:
        desc=unescape(result[0])

    result=upc_pat.findall(content)
    if len(result)==0:
        logging.warn("UPC not founded!")
        upc=""
    else:
        upc=result[0]

    result=price_pat.findall(content)
    if len(result)==0:
        logging.warn("Price not founded!")
        price=""
    else:
        price=result[0]

    result=avail_pat.findall(content)
    if len(result)==0:
        logging.warn("Availability not founded!")
        avail=""
    else:
        avail=result[0]

    return img_url, desc, upc, price, avail

def get_next_page(content):
    """checks the content of a book list page and return
    link of next page, return None, if there is no
    more next page"""

    next_page=next_page_pat.findall(content)

    if len(next_page)==0:
        return None

    return next_page


def crawl_website():
    """crawl_website is main function that coordinates
    the whole crawling task"""

    content=get_page_content(url)
    if content is None:
        logging.critical("Failed to get content from "+url)
        sys.exit(1)

    category_list=get_category_list(content)

    for category in category_list:
        category_url, category_name=category
        category_url=url+category_url
        crawl_category(category_name, category_url)


def crawl_category(category_name,category_url):
    """crawls a particular category of a book"""

    while True:
        content=get_page_content(category_url)
        book_list=get_book_list(content)

        for book in book_list:
            scrape_book_info(book, category_name)

        if get_next_page(content) is None:
            break

        next_page=get_next_page(content)
        i=category_url.rfind("/")
        category_url=category_url[0:i+1]+next_page[0]


def scrape_book_info(book_info, category_name):
    """gets the content of a book details page,
    and parses different components and stores the info"""

    book_url, book_name = book_info

    book_name=unescape(book_name)
    book_url=book_url.replace('../../..',url+'catalogue')

    print("Scraping book", book_name)
    logging.info("Scraping: "+book_url)

    content=get_page_content(book_url)

    details=get_product_details(content)

    img_url, description, upc, price, availability=details
    img_url=img_url.replace('../../',url)

    details_dict={"Name": book_name, "Category": category_name, "UPC": upc, "URL": book_url, "ImageURL": img_url,
    "Price": price, "Availability": availability, "Description": description}

    csv_writer.writerow(details_dict)


if __name__=="__main__":

    url="http://books.toscrape.com/"

    category_pat=re.compile(r'<li>\s*<a href="(catalogue/category/books/.+?)">\s*(\w+[\w\s]*\w+)\s*</a>')

    book_pat=re.compile(r'<h3><a href="(.+?)"\s*title="(.+?)">')

    next_page_pat=re.compile(r'<li class="next"><a href="(.+?)">')

    img_pat=re.compile(r'<div class="item active">\s*<img src="(.+?)"\s*alt')

    desc_pat=re.compile(r'<h2>Product Description</h2>.+?<p>(.+?)</p>')

    upc_pat=re.compile(r'<th>UPC</th>\s*<td>(.+?)<')

    price_pat=re.compile(r'<th>Price \(incl\. tax\)</th>\s*<td>\D+([\d.]+?)</td>')

    avail_pat=re.compile(r'<th>Availability</th>\s*<td>(.+?)<')

    logging.basicConfig(filename='bookstore_crawler.log', format='%(asctime)s (%(message)s)',
    datefmt='%D %I:%M:%S %p', level=logging.DEBUG)

    with open('book_list.csv','w',encoding="ISO-8859-1") as f:
        csv_writer=csv.DictWriter(f, fieldnames=["Name", "Category", "UPC", "URL", "ImageURL",
        "Price", "Availability", "Description"])
        csv_writer.writeheader()

        crawl_website()
        print('Crawling Done!')
