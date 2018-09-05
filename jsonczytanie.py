import json
from pprint import pprint



with open("E:\\Seriale\\pliczki\\json.txt") as f:
    txt = f.read()
    d = json.loads(txt)
    for l in (d['hits']['hits']):

        print(l['fields']['dc_title'])
