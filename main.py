#! /bin/python

import os
import requests

if __name__ == '__main__':
    j = requests.get('https://api.lolicon.app/setu/v2?size=original&proxy=i.pixiv.cat&r18=0').json()
    data = j['data']
    url = data[0]['urls']['original']

    path = '/tmp/lolicon_res.jpg'
    with open(path, 'wb') as f:
        f.write(requests.get(url).content)
    os.system(f'feh --no-fehbg --bg-fill {path}')
