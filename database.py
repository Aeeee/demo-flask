import json
import random


def get_random():
    with open('memes.json', 'r') as file:
        db = json.load(file)
    return random.choice(db['entries'])


def add_like(id: int):
    with open('memes.json', 'r') as file:
        db = json.load(file)
    for i in range(len(db['entries'])):
        if db['entries'][i]['id'] == id:
            db['entries'][i]['likes'] += 1
            like_count = db['entries'][i]['likes']
            break
    else: # выполнится, если цикл for не был прерван через break
        return 'no such id'
    with open('memes.json', 'w') as file:
        json.dump(db, file)
    return like_count
