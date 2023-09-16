from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

# url = "https://scholar.google.com/citations?user=xfW8UvkAAAAJ&hl=en"
url = "https://priceschool.usc.edu/faculty/"
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
# print(page_soup.prettify)

details_list = page_soup.find(id="full-faculty-list-items")
# print(details_list.prettify)

count=0
profPrice_list = details_list.find_all("tr", class_="item clickable")
for profPrice_all in profPrice_list:
    # print(profPrice_all.prettify())
    print(profPrice_all.find("td", class_="name").text.strip(), end="\n")
    print(profPrice_all.find("td", class_="position").text.strip(), end="\n")
    print(profPrice_all.find("td", class_="expertise").text.strip(), end="\n")
    print("\n==============================\n")
    count+=1
print(count)
