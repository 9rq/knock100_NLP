import gzip
import json

def open_json_gzip():
    with gzip.open('./jawiki-country.json.gz','rt') as f:
        res = {i['title']:i['text'] for i in [json.loads(line) for line in f]}
    return res

ans = open_json_gzip()
for key in ans:
    if 'イギリス' in key:
        print(ans[key])
