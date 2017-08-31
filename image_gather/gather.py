import traceback
from urllib.request import urlopen, Request
from urllib.parse import quote
from mimetypes import guess_extension
import os
import sys
from bs4 import BeautifulSoup
from time import time, sleep

MY_UA = ''

class Fetcher:
    '''
    ua = ユーザーエージェント
    受け取ったurlを指定されたuaでリクエストし、html、MIMEタイプとエンコード（Content-Type）を貰う
    '''
    def __init__(self, ua=''):
        self.ua = ua

    def fetch(self, url, ):
        req = Request(url, headers={'User-Agent': self.ua})
        try:
            with urlopen(req, timeout=3) as p:
                content = p.read()
                mime = p.getheader('Content-Type')
        except:
            sys.stderr.write('Error in fetching :'+ format(url))
            sys.stderr.write(traceback.format_exc())

            return None, None

        return content, mime

fetcher = Fetcher(MY_UA)



def url_search(word, n):
    '''
    ヤフーの画像検索を使って画像収集
    :param word: 検索キーワード
    :param n: 枚数
    :return: 画像のURL群　これをpcのフォルダにDLして終わり
    '''
    code = '&ei=UTF-8'
    url = ('http://image.search.yahoo.co.jp/search?n={}&p={}'+code).format(n, quote(word))
    byte_content, mime = fetcher.fetch(url)
    soup = BeautifulSoup(byte_content.decode('UTF-8'), 'html.parser')
    img_link_elem = soup.find_all('a', attrs={'target': 'imagewin'})
    img_urls = [e.get('href') for e in img_link_elem if e.get('href').startswith('http')]
    #重複を取るテク
    img_urls = list(set(img_urls))
    return img_urls


def image_collector_in_url(urls,fname):
    '''
    取得したURL群をfetchし画像ダウンロード
    :param urls:  画像の存在するURL
    :param fname: 作成されるフォルダの名前
    :return: ダウンロードに成功した数
    '''
    dir = 'img/'+str(fname)
    scount = 0
    if not os.path.exists(dir):
        os.makedirs(dir)

        for i , url in enumerate(urls):
            sleep(0.1)
            img, mime = fetcher.fetch(url)
            if not mime or not img:
                continue
            try:
                ext = guess_extension(mime.split(';')[0])
                if ext in ('.jpe', '.jpg', '.png'):
                    ext = '.png'
                elif not ext:
                    continue
            except:
                print('Error in converting extension ¥n URL:{}').format(str(url))
                continue
            file = os.path.join(dir, str(i) + ext)
            with open(file, mode='wb') as f:
                f.write(img)
            print('ダウンロード成功 URL:'+str(url))
            scount += 1
        return scount

if __name__ == '__main__':
    print('欲しい画像のキーワードを入力してください')
    keyword = input('>> ')
    print('枚数を入力してください')
    get_num = int(input('>> '))
    image_urls = url_search(keyword, get_num)
    download_count = image_collector_in_url(image_urls, keyword)
    print(str(download_count)+'件の画像の収集に成功しました')