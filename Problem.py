from bs4 import BeautifulSoup


class Problem:
    """
    tag                         occurrence
    math                        2000
    greedy                      1928
    dp                          1566
    data structures             1248
    brute force                 1170
    constructive algorithms     1160
    graphs                      828

    We will be guessing these tags as they are the most common
    topics and occur quite a lot
    """

    TAGS = ['math', 'greedy', 'dp', 'data structures', 'brute force', 'constructive algorithms', 'graphs']

    def __init__(self, path):
        self.rating = 0
        self.content = ''
        self.has_tags = [False] * len(self.TAGS)
        html = ''
        with open(path, 'rb') as file:
            html = file.read()

        soup = BeautifulSoup(html, 'html.parser')

        self.get_content(soup)
        self.get_tags(soup)

    def __str__(self):
        return self.content + '\n' + str(self.has_tags) + '\n' + str(self.rating)

    def get_content(self, soup):
        str = ' '.join(soup.find('div', class_='problem-statement').
                       find_all('div', recursive=False)[1].stripped_strings)
        self.content = ' '.join(''.join([i if i.isalnum() or i.isspace() else '' for i in str]).split())

    def get_tags(self, soup):
        spans = soup.find(id='sidebar').find_all('span', class_='tag-box')
        for span in spans:
            str = span.text.strip()
            if str[0] == '*':
                if str[1:].isdigit():
                    self.rating = int(str[1:])
            else:
                for i in range (len(self.TAGS)):
                    if self.TAGS[i] == str:
                        self.has_tags[i] = True
                        break


if __name__ == '__main__':
    problem = Problem('problems/1638F.html')
    print(problem)
