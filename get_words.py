import re
import string


def get_words_from_text(text_path):
    with open(text_path, 'rb') as file:
        # web ( e forse anche non web)
        text = file.read().decode("latin-1")
        # non-web
        # text = file.read().decode("utf-8")

        # remove [verse 1: artist]
        # include the following line if you are doing song lyrics
        text = re.sub(r'\[(.+)\]', ' ', text)

        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    words = words[:1000]

    return words
