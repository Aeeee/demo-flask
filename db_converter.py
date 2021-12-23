import json


def convert():
    with open('meme_urls.txt', 'r') as file:
        original = file.read().split('\n')
    entries = []
    id = 0
    for url in original:
        entries.append({
            'id': id,
            'url': url,
            'likes': 0
        })
        id += 1
    converted = {
        'entries': entries
    }
    with open('memes.json', 'w') as file:
        json.dump(converted, file, indent=4)


if __name__ == '__main__':
    convert()
