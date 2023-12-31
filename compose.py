"""
Implemented Markov Chain Composer by Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import os
import re
import string
import random
from graph import Graph, Vertex
from web_scraper import Pagina_Repubblica
from get_words import get_words_from_text

# def get_words_from_text(text_path):
#     with open(text_path, 'rb') as file:
#         # web ( e forse anche non web)
#         text = file.read().decode("latin-1")
#         # non-web
#         # text = file.read().decode("utf-8")
#
#         # remove [verse 1: artist]
#         # include the following line if you are doing song lyrics
#         text = re.sub(r'\[(.+)\]', ' ', text)
#
#         text = ' '.join(text.split())
#         text = text.lower()
#         text = text.translate(str.maketrans('', '', string.punctuation))
#
#     words = text.split()
#
#     words = words[:1000]
#
#     return words


def make_graph(words):
    g = Graph()
    prev_word = None
    # for each word
    for word in words:
        # check that word is in graph, and if not then add it
        word_vertex = g.get_vertex(word)

        # if there was a previous word, then add an edge if does not exist
        # if exists, increment weight by 1
        if prev_word:  # prev word should be a Vertex
            # check if edge exists from previous word to current word
            prev_word.increment_edge(word_vertex)

        prev_word = word_vertex

    g.generate_probability_mappings()
    
    return g

def compose(g, words, length=100):
    composition = []
    # I choose randomly the first word!
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition
# poesie
def main():

# canzoni
# def main(artist):
    # poesie
    # words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    # canzoni
    # words = []
    # for song in os.listdir('songs/{}'.format(artist)):
    #     if song == '.DS_Store':
    #         continue
    #     words.extend(get_words_from_text('songs/{artist}/{song}'.format(artist=artist, song=song)))

    # web
    # web scraping
    news = "https://www.repubblica.it/la-zampa/2023/11/01"
    my_news = "/news/deserto_pesci_vivono_100_anni-419333274/?utm_source=pocket-newtab-it-it"
    pg_rep = Pagina_Repubblica(news, my_news)
    _ = pg_rep.art_scraper()
    words = get_words_from_text('webtext/webtextstring.txt')



    g = make_graph(words)
    composition = compose(g, words, 500)
    print(' '.join(composition))


if __name__ == '__main__':
    # Poesie, web
    print(main())
    # Canzoni
    # print(main('taylor_swift'))
