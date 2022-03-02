import time

import requests
from bs4 import BeautifulSoup
import concurrent.futures

LINK = "https://codeforces.com"
PROBLEMSET_LINK = LINK + "/problemset/page/"
SAVE_DIRECTORY = "problems"
START = 31
END = 40


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
    resp = requests.get(LINK + link)
    seg = link.split('/')
    title = SAVE_DIRECTORY + '/' + seg[-2] + seg[-1] + '.html'

    with open(title, 'wb') as file:
        file.write(resp.content)

    time.sleep(0.25)


print("Getting links to problems...")
links = get_links()

print("Getting htmls of each problem...")
with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(links), 30)) as executor:
    executor.map(save_problem, links)