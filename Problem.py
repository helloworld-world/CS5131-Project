from bs4 import BeautifulSoup


class Problem:
    def __init__(self, path):
        self.content = ''
        self.tags = []
        html = ''
        with open(path, 'rb') as file:
            html = file.read()

        soup = BeautifulSoup(html, 'html.parser')

        self.get_content(soup)
        self.get_tags(soup)

    def __str__(self):
        return self.content + '\n' + str(self.tags)

    def get_content(self, soup):
        str = ' '.join(soup.find('div', class_='problem-statement').
                       find_all('div', recursive=False)[1].stripped_strings)
        self.content = ' '.join(''.join([i if i.isalnum() or i.isspace() else '' for i in str]).split())

    def get_tags(self, soup):
        spans = soup.find(id='sidebar').find_all('span', class_='tag-box')
        for span in spans:
            self.tags.append(span.text.strip())
        pass


if __name__ == '__main__':
    problem = Problem('problems/1644F.html')
    print(problem)
