import json
import random


def get_random():
    with open('memes.json', 'r') as file:
        db = json.load(file)
    return random.choice(db['entries'])


def add_like(id: int):
    with open('memes.json', 'r') as file:
        db = json.load(file)
    db['entries'][id]['likes'] += 1
    like_count = db['entries'][id]['likes']
    with open('memes.json', 'w') as file:
        json.dump(db, file)
    return like_count
