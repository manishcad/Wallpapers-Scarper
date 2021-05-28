import requests
from bs4 import BeautifulSoup
import os

search = input("Enter the type of iamges you want: ")
req = requests.get(
    f"https://www.hdwallpapers.in/search.html?q={search}").content

soup = BeautifulSoup(req, 'html.parser')
body = soup.findAll('div', id="body")


# images pages links
images_html_pages = []
print("Downloading")
for i in body:
    block_main = i.findAll('div', id="block-main")
    for i in block_main:
        block_content = i.findAll('div', id="block-content")
        for i in block_content:
            content_wrapper = i.findAll('div', id="content-wrapper")
            for i in content_wrapper:
                thumb = i.findAll('div', class_="thumb")
                for i in thumb:
                    anchor_tag = i.findAll('a')
                    for i in anchor_tag:
                        images_html_pages.append(i['href'])

# making a directory and changing the directory
os.mkdir(search)
os.chdir(search)

# getting all the images links,title,resolution
for i in images_html_pages:

    req = requests.get(f"https://www.hdwallpapers.in{i}").content
    soup = BeautifulSoup(req, 'html.parser')
    href_list = []
    title_list = []
    content = soup.findAll('section', id="content")
    for i in content:
        resolution = i.findAll('div', class_="wallpaper-resolutions")
        for i in resolution:
            anchor_tags = i.findAll('a')
            for i in anchor_tags:
                href = i['href']
                title = i['title']
                real_title = title[0::]
                title_list.append(real_title)
                real_href = href[0::]
                href_list.append(real_href)

    replace_title = title_list[-1].replace(" ", "")

# Writing the image byte code using using requets and save it to the folder
    for i in href_list:
        request = requests.get(f"https://www.hdwallpapers.in/{i}").content
        with open(replace_title+'.jpg', 'wb') as f:
            f.write(request)
