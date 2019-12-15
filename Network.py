#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


#
# パブリッシュ / サブスクライブモデル
#


# Redis
def redis_pub():  # パブリッシャ
    import redis
    import random

    conn = redis.Redis()
    cats = ['siamese', 'persian', 'maine coon', 'norwegian forest']
    hats = ['stovepipe', 'bowler', 'tam-o-shanter', 'fedora']
    for msg in range(10):  # ランダムでチョイスした10のトピックをランダムなメッセージでパブリッシュする
        cat = random.choice(cats)  # チャンネル
        hat = random.choice(hats)  # メッセージ
        print('Publish: %s wears %s' % (cat, hat))
        conn.publish(cat, hat)  # 何らかのcatsチャンネルのhatsメッセージをパブリッシュ


def redis_sub():  # サブスクライバ
    import redis
    conn = redis.Redis()

    topics = ['maine coon', 'persian']  # このサブスクライバはmaine coonとpersianに興味がある
    sub = conn.pubsub()    # サブスクライブを実現するpubsubオブジェクトを取得
    sub.subscribe(topics)  # topicsに一致するチャンネルのメッセージをサブスクライブ
    for msg in sub.listen():  # メッセージの受信を待つ
        if msg['type'] == 'message':  # typeがmessageならtopicsに合致
            cat, hat = msg['channel'], msg['data']
            print('Subscribe: %s wears a %s' % (cat, hat))


# ZeroMQ
def zmq_pub():
    import zmq
    import random
    import time
    host, port = '*', 6789
    ctx = zmq.Context()  # ZeroMQのコンテキストを取得
    pub = ctx.socket(zmq.PUB)  # zmq.PUB(パブリッシャ)タイプでZeroMQソケットを作成
    pub.bind('tcp://%s:%s' % (host, port))  # TCPのポート6789にバインド(6789にパブリッシュ)
    cats = ['siamese', 'persian', 'maine coon', 'norwegian forest']
    hats = ['stovepipe', 'bowler', 'tam-o-shanter', 'fedora']
    time.sleep(1)
    for msg in range(10):  # ランダムでチョイスした10のトピックをランダムなメッセージでパブリッシュする
        cat = random.choice(cats)
        cat_bytes = cat.encode('utf-8')  # トピックを utf-8 にエンコード
        hat = random.choice(hats)
        hat_bytes = hat.encode('utf-8')  # メッセージを utf-8 にエンコード
        print('Publish: %s wears a %s' % (cat, hat))
        pub.send_multipart([cat_bytes, hat_bytes])  # 最初の要素がトピックとなる複数の要素を送る


def zmq_sub():
    import zmq
    host, port = 'localhost', 6789
    ctx = zmq.Context()
    sub = ctx.socket(zmq.SUB)  # zmq.SUB(サブスクライバ)タイプでZeroMQソケットを作成
    sub.connect('tcp://%s:%s' % (host, port))  # tcp://localhost:6789 で待つ
    topics = ['maine coon', 'persian']  # このサブスクライバはmaine coonとpersianに興味がある
    for topic in topics:  # サブスクライブするtopicを設定する
        sub.setsockopt(zmq.SUBSCRIBE, topic.encode('utf-8'))
    while True:  # パブリッシュを待機
        cat_bytes, hat_bytes = sub.recv_multipart()  # topicが一致するものをレシーブ
        cat = cat_bytes.decode('utf-8')
        hat = hat_bytes.decode('utf-8')
        print('Subscribe: %s wears a %s' % (cat, hat))


# その他のパブサブツール
other_pubsub = {
    'RabbitMQ', 'http://pypi.python.org', 'pubsubhubbub',
    }


#
# ソケット
#


def udp_server():  # ソケットを使ってUDPでデータのやり取りをするサーバー
    from datetime import datetime
    import socket

    server_address = ('localhost', 6789)
    max_size = 4076

    print('Starting the server at', datetime.now())
    print('Waiting for a clint to call.')
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP/IPでソケットを作成
    server.bind(server_address)  # localhost:6789にバインド(このアドレスとポートでデータをリスン)

    data, client = server.recvfrom(max_size)  # データの到着を待つ(clientは送り元のクライアントの情報)

    print('At', datetime.now(), client, 'said', data)
    server.sendto(b'Are you talking to me?', client)  # クライアントにバイト列を送信
    server.close()


def udp_client():  # ソケットを使ってUDPでデータのやり取りをするクライアント
    import socket
    from datetime import datetime

    server_address = ('localhost', 6789)
    max_size = 4096

    print('Starting the client at', datetime.now())
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP/IPでソケットを作成
    client.sendto(b'Hey!', server_address)  # localhost:6789にバイト列を送信
    data, server = client.recvfrom(max_size)  # サーバーからの返信を待つ
    print('At', datetime.now(), server, 'said', data)
    client.close()


def tcp_server():  # ソケットを使ってTCPでデータのやり取りをするサーバー
    from datetime import datetime
    import socket

    server_address = ('localhost', 6789)
    max_size = 1000

    print('Starting the server at', datetime.now())
    print('Waiting for a clint to call')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP/IPでソケット作成
    server.bind(server_address)  # localhost:6789でリスン
    server.listen(5)  # キューに5個のクライアント接続が溜まったら新しい接続を拒否

    client, addr = server.accept()  # クライアントとの接続を確立(接続してきたクライアントの情報を取得)
    data = client.recv(max_size)  # クライアントからのデータ送信を受信(受信できるサイズの上限はmax_size)

    print('At', datetime.now(), client, 'said', data)
    client.sendall(b'Are you talking to me?')  # クライアントにバイト列を送信
    client.close()
    server.close()


def tcp_client():  # ソケットを使ってTCPでデータのやり取りをするクライアント
    import socket
    from datetime import datetime

    server_address = ('localhost', 6789)
    max_size = 1000

    print('Starting the client at', datetime.now())
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP/IPでソケット作成
    client.connect(server_address)  # localhost:6789に接続
    client.sendall(b'Hey!')  # サーバーにバイト列を送信
    data = client.recv(max_size)  # サーバーからのデータ送信を受信（受信できるサイズの上限はmax_size）
    print('At', datetime.now(), 'someone replied', data)
    client.close()


#
# ZeroMQ : 強化版ソケット
#


# ZeroMQ のソケットタイプ
zmq_socktype = {
    'REQ':      '同期要求',
    'REP':      '同期応答',
    'DEALER':   '非同期要求',
    'ROUTERS':  '非同期応答',
    'PUB':      'パブリッシュ',
    'SUB':      'サブスクライブ',
    'PUSH':     'プッシュ',
    'PULL':     'プル',
    }


def zmq_server():  # 同期的に応答するZeroMQサーバー
    import zmq

    host, port = '127.0.0.1', 6789
    context = zmq.Context()  # Contextオブジェクトを作成(状態を管理する)
    server = context.socket(zmq.REP)  # 同期応答のZeroMQソケットを作成
    server.bind("tcp://%s:%s" % (host, port))  # tcp://localhost:6789にバインド(リスン)
    while True:
        request_bytes = server.recv()  # クライアントからのリクエストを待つ
        request_str = request_bytes.decode('utf-8')
        print("That voice in my head says: %s" % request_str)
        reply_str = "Stop saying: %s" % request_str
        reply_bytes = bytes(reply_str, 'utf-8')
        server.send(reply_bytes)  # クライアントにバイト列を送信


def zmq_client():  # 同期的に要求するZeroMQクライアント
    import zmq

    host, port = '127.0.0.1', 6789
    context = zmq.Context()
    client = context.socket(zmq.REQ)  # 同期要求のZeroMQオブジェクトの作成
    client.connect("tcp://%s:%s" % (host, port))  # tcp://localhost:6789にコネクト
    for num in range(1, 6):  # ６つリクエストを送信する
        request_str = "message #%s" % num
        request_bytes = request_str.encode('utf-8')
        client.send(request_bytes)  # サーバーにバイト列を送信
        reply_bytes = client.recv()  # サーバーからの返信を待つ
        reply_str = reply_bytes.decode('utf-8')
        print("Sent %s, received %s" % (request_str, reply_str))


#
# Scapy : パケット操作ツール
#
Scapy = {'Scapy': 'http://bit.ly/scapy-docs'}


#
# インターネットサービス
#


# DNS
def dns_service(args):
    import socket
    url, = args
    print(url)
    print(socket.gethostbyname(url))        # ドメイン名に対応するIPアドレスを返す
    print(socket.gethostbyname_ex(url))     # 引数の名前と代替名のリスト、IPアドレスのリストを返す
    print(socket.getaddrinfo(url, 80))      # ソケットを作るために必要な情報も返す
    print(socket.getaddrinfo(
        url, 80, socket.AF_INET, socket.SOCK_STREAM))  # TCP/IPの情報のみ返す
    print(socket.getservbyname('http'))     # サービス名をポート番号に変換
    print(socket.getservbyport(80))         # ポート番号をサービス名に変換


# Python の電子メールモジュール
py_mail_module = {  # モジュール名 : プロトコル
    'smtplib': 'SMTP',
    'email': '電子メールメッセージの作成、構文解析',
    'poplib': 'POP3',
    'imaplib': 'IMAP',
    'smtpd': 'SMTPサーバー',
    'Lamson': 'SMTPサーバー',
    }


# その他のプロトコル
other_module = {  # モジュール名 ： プロトコル
    'ftplib': 'FTP'
    }


#
# ウェブサービスと API
#


def youtube_top_rated():  # YouTubeから最も人気の高いビデオを拾ってくる
    import requests
    url = "https://raw.githubusercontent.com/koki0702/introducing-python/" + \
          "master/dummy_api/youTube_top_rated.json"
    response = requests.get(url)
    data = response.json()  # データをJSONで取得
    for video in data['feed']['entry'][0:5]:  # 最初の５本を取得
        print(video['title']['$t'])


# 様々な ウェブサービス API
other_webservice_API = {
    'New York Times', 'YouTube', 'Twitter', 'Facebook',
    'Weather Underground', 'Marvel Comics',
    }


#
# リモート処理
#


# RPC (Remote Procedure Calls)
def xmlrpc_server():  # XMLを交換形式とするRPC関数を提供するサーバー
    from xmlrpc.server import SimpleXMLRPCServer

    def double(num):  # RPC関数として提供される
        return num * 2

    server = SimpleXMLRPCServer(("localhost", 6789))  # localhost:6789でサーバーを起動
    server.register_function(double, "double")  # double関数を登録
    server.serve_forever()  # リクエストのハンドルを開始


def xmlrpc_client():  # XMLを交換形式とするRPC関数を利用するクライアント
    import xmlrpc.client

    proxy = xmlrpc.client.ServerProxy("http://localhost:6789")  # サーバーに接続
    num = 7
    result = proxy.double(num)  # double をリモート関数として呼び出す
    print("Double %s is %s" % (num, result))


# Python RPC 実装
def msgpack_server():  # メッセージバックによるRPC実装のサーバー
    from msgpackrpc import Server, Address

    class Services():
        def double(self, num):
            return num * 2

    server = Server(Services())  # ServicesクラスのメソッドをRPCサービスとして提供
    server.listen(Address("localhost", 6789))  # localhost:6789でリスン
    server.start()


def msgpack_client():  # メッセージバックによるRPC実装のクライアント
    from msgpackrpc import Client, Address

    client = Client(Address("localhost", 6789))  # サーバーに接続
    num = 8
    result = client.call('double', num)  # double をリモート呼び出し
    print("Double %s is %s" % (num, result))


# fabric
fabric = {'fabric': 'http://docs.fabfile.org'}


# Salt
salt = {'Salt': 'http://www.saltstack.com'}


#
# ビッグデータと MapReduce : 分散コンピューティング
#
distributed_comp = {
    'Hadoop', 'Luigi', 'Spark', 'Disco',
}


#
# クラウドでの処理
#


# Google
google_cloud = {
    'App Engine': '高水準プラットフォーム',
    'Compute Engine': '大規模な分散コンピューティングのための仮想マシンクラスタ',
    'Cloud Strage': 'オブジェクトのストレージ',
    'Cloud Datastore': '大規模なNoSQLデータベース',
    'Cloud SQL': '大規模なSQLデータベース',
    'Cloud Endpoints': 'アプリケーションへのRESTfullによるアクセス',
    'BigQuery': 'Hadoop風のビッグデータ',
    }


# Amazon
amazon_web_services = {
    'Elastic Beanstalk': '高水準アプリケーションプラットフォーム',
    'EC2(Elastic Compute)': '分散コンピューティング',
    'S3(Simple Storage Service)': 'オブジェクトのストレージ',
    'RDS': 'リレーショナルデータベース(MySQL, PostgreSQL, Oracle, MSSQL)',
    'DynamoDB': 'NoSQLデータベース',
    'Redshift': 'データウェアハウス',
    'EMR': 'Hadoop',
    }
boto = {'boto': 'Python AWS ライブラリ'}


# OpenStack
openstack = {
    'Keystone': 'アイデンティティサービス',
    'Nova': 'ネットワーク分散計算サービス',
    'Swift': 'オブジェクトストレージ',
    'Glance': 'イメージストレージサービス',
    'Cinder': 'ブロックストレージサービス',
    'Horizon': 'ウェブベースダッシュボード',
    'Neutron': 'ネットワーク管理サービス',
    'Heat': 'オーケストレーション(マルチクラウド)サービス',
    'Ceilometer': '遠隔測定(メトロニクス,管理モニタリング,検針)サービス',
    }
Devstack = {'Devstack': 'OpenStack サービス管理'}


#
# $ python3 Network.py runfunc ... 起動用
#
if (__name__ == '__main__') and (len(sys.argv) > 1):
        print('runnning: ' + sys.argv[1])
        if len(sys.argv) > 2:
            eval(sys.argv[1])(tuple(sys.argv[2:]))
        else:
            eval(sys.argv[1])()
