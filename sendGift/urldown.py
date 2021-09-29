import requests, threading, time, json
from urllib.parse import urlparse


def read_json():
    j = json.load(open(r'json.txt'))

    for i in range(0, 95):
        print(j['data']['in_room'][i]['value'])
        with open(r'hello.txt', 'a+') as f:
            f.write(j['data']['in_room'][i]['value'])
            f.write('\r\n')


def read_url():
    with open(r'hello.txt', 'r') as f:
        url = f.readlines()
        for i in url:
            print(''.join(i).strip())
            r = requests.get(''.join(i).strip())
            surl = urlparse(''.join(i).strip())
            with open(r'/Users/yixia/Documents/tt/%s' % surl.path[20:], "wb") as code:
                code.write(r.content)


if __name__ == '__main__':
    time1 = time.perf_counter()
    print(time1)
    t = threading.Thread(target=read_json())
    t.run()
    t1 = threading.Thread(target=read_url())
    t1.run()
    time2 = time.perf_counter()
    t3 = time2 - time1
    print('共耗时：', t3, '秒')
