#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


#
# ウェブクライアント
#


# Python の標準ウェブライブラリ
def urllib_request():
    import urllib.request as ur
    url = 'https://raw.githubusercontent.com/koki0702/' + \
        'introducing-python/master/dummy_api/fortune_cookie_random1.txt'
    conn = ur.urlopen(url)  # URL を開く
    print(conn)  # HTTPResponce オブジェクトを取得(コネクション開始)

    data = conn.read()  # コンテンツの読み込み
    print(data)
    print(conn.status)  # HTTPステータスコードとして 200(成功) が返ってくるはず

    print(conn.getheader('Content-Type'))  # 応答ヘッダーのContent-Typeを取得(text/Plain)
    for key, value in conn.getheaders():  # HTTPヘッダの全ての情報を取得
        print(key, value)


# 標準ライブラリを超えて (requestsライブラリ)
def python_requests():
    import requests
    url = 'https://raw.githubusercontent.com/koki0702/' + \
        'introducing-python/master/dummy_api/fortune_cookie_random1.txt'
    resp = requests.get(url)  # URLリクエストを取得
    print(resp)  # <Response [200]> (成功)
    print(resp.text)  # 取得したテキストの表示


# urllib_request()
# python_requests()


#
# ウェブサーバー
#


# Python によるもっとも単純なウェブサーバー
#
# $ python -m http.server
#


# ウェブフレームワーク : Bottle
def bottle_server_text():
    from bottle import route, run

    @route('/')  # URLと関数を対応付けるデコーダ('/'(ホームページ)をhome関数が処理する)
    def home():  # ホームページが表示されるとこの関数を実行する
        return "It isn't fancy, bout it's my home page"

    run(host='localhost', port=8000)  # HTTPサーバーの起動


def bottle_server_html():
    from bottle import route, run, static_file

    @route('/')
    def main():
        return static_file(
            'files/index.html', root='.')  # カレントディレクトリ下の files/index.html を表示

    run(host='localhost', port=8000)


def bottle_server_url():
    from bottle import route, run, static_file

    @route('/')
    def home():
        return static_file('files/index.html', root='.')

    @route('/echo/<thing>')  # URLの/echo/の後ろの部分を文字列引数に代入する
    def echo(thing):  # http://localhost/echo/<thing>
        return "Say hello to my little firend: %s!" % thing

    run(host='localhost', port='8000')


# ウェブフレームワーク : Flask
def flask_server():
    from flask import Flask
    app = Flask(__name__, static_folder='.', static_url_path='')  # カレントディレクトリ

    @app.route('/')
    def home():
        return app.send_static_file('files/index.html')  # index.html を表示

    @app.route('/echo/<thing>')
    def echo(thing):
        return thing

    app.run(port=8000, debug=True)  # HTTPサーバーの起動


def flask_server_template():
    from flask import Flask, render_template
    app = Flask(__name__)

    @app.route('/echo/<thing>')
    def echo(thing):
        return render_template(
            'flask_template.html', thing=thing)  # templatesディレクトリ下のテンプレートを展開

    app.run(port=8000, debug=True)


# URL パスの一部という形での引数渡し
def flask_server_template2():
    from flask import Flask, render_template, request
    app = Flask(__name__)

    # http://localhost:8000/echo/<thing>/<place> の形で渡す
    @app.route('/echo/<thing>/<place>')
    def echo(thing, place):
        return render_template(
            'flask_template2.html', thing=thing, place=place)

    # http://localhost:8000/echo?thing=<thing>&place=<place> の形で渡す
    @app.route('/echo/')
    def echo2():
        kwargs = {}  # 複数の引数を辞書で渡せる
        kwargs['thing'] = request.args.get('thing')  # GET引数として渡す
        kwargs['place'] = request.args.get('place')  # GET引数として渡す
        return render_template(
            'flask_template2.html', **kwargs)

    app.run(port=8000, debug=True)


# その他のフレームワーク
Other_Web_Frames = {
    'django', 'web2py', 'pyramid', 'turbogears', 'wheezy.web',
    }

# その他の Python ウェブサーバー
Other_Web_Servers = {
    'uwsgi', 'cherrypy', 'pylons', 'tornado', 'gevent', 'gunicorn',
    }


#
# ウェブサービスとオートメーション
#


# webbrowser モジュール
def anti_gravity():
    import antigravity  # webbrowser モジュールが呼び出され、ブラウザに啓蒙的な Python リンクを表示


def web_browser():
    import webbrowser
    url = 'http://www.python.org/'
    webbrowser.open(url)  # 指定したサイトをウェブブラウザで開く


# BeautifulSoup による HTML のスクレイピング
def bs_scraping():
    def get_links(url):
        import requests
        from bs4 import BeautifulSoup as soup
        result = requests.get(url)  # URL リクエストを取得
        page = result.text
        doc = soup(page, features="lxml")
        links = \
            [element.get('href') for element in doc.find_all('a')]  # リンクを取得
        return links

    for num, link in enumerate(get_links(sys.argv[2]), start=1):
        print(num, link)  # 取得したリンクを1から順番に表示
    print()


# $ python3 Web.py runfunc ... サーバー起動用
if __name__ == '__main__':
    print('runnning:' + sys.argv[1])
    eval(sys.argv[1])()
