import urllib
import requests
from bs4 import BeautifulSoup

LINK = "https://codeforces.com"
PROBLEMSET_LINK = LINK + "/problemset/page/"
SAVE_DIRECTORY = "problems"
START = 2, END = 2


def get_links():
    result = []
    for page_no in range(START, END + 1):
        print("Page " + str(page_no) + '...')
        page = requests.get(PROBLEMSET_LINK + str(page_no))
        soup = BeautifulSoup(page.content, 'html.parser')
        alist = soup.select('.problems div[style="float: left;"] a')
        for a in alist:
            result.append(a['href'])
    return result


def save_problem(link):
    page = urllib.request.urlopen(LINK + link)
    seg = link.split('/')
    with open(SAVE_DIRECTORY + '/' + seg[-2] + seg[-1] + '.html', 'wb') as file:
        file.write(page.read())


print("Getting links to problems...")
links = get_links()

print("Getting htmls of each problem...")
i = 0
for link in links:
    i += 1
    print("Problem " + str(i) + '...')
    save_problem(link)
