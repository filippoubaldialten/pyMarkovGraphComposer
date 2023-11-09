from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os
from get_words import get_words_from_text


class Pagina_Repubblica():
    def __init__(self, news, my_news):
        self.x_news = news
        self.x_my_news = my_news

    def art_scraper(self):
        url: str = self.x_news + self.x_my_news

        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        text_0 = soup.find_all('div', class_="story__text")
        # print(text_0)

        text_good = re.sub("<.*?>", "", str(text_0))
        path = "./webtext"
        filename = "webtextstring.txt"
        if not os.path.exists(path):
            os.makedirs(path)
        f = open(path + "/" + filename, "a")
        f.write(text_good)
        f.close()
        # return text_good


# page = urlopen(url)
# html_bytes = page.read()
# html = html_bytes.decode("utf-8")
# tag_ini = "\"articleBody\": "
# tag_end = "articleSection"
# title_index = html.find(tag_ini)
# start_index = title_index + len(tag_ini)
# end_index = html.find(tag_end)
# print(title_index, start_index, end_index, end_index - start_index)
# my_web_text = html[start_index:end_index]
# print(my_web_text)

if __name__ == '__main__':
    from compose import *
    news = "https://www.repubblica.it/la-zampa/2023/11/01"
    my_news = "/news/deserto_pesci_vivono_100_anni-419333274/?utm_source=pocket-newtab-it-it"
    pg_rep = Pagina_Repubblica(news, my_news)
    _ = pg_rep.art_scraper()
    words = get_words_from_text('webtext/webtextstring.txt')
    g = make_graph(words)
    composition = compose(g, words, 50)
    print(' '.join(composition))
