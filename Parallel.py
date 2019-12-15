#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


#
# 並行処理
#


# プロセス(キュー)
def process_dishes():
    import multiprocessing as mp

    # 洗浄係
    def washer(dishes, output):
        for dish in dishes:
            print('Washing', dish, 'dish')
            output.put(dish)  # キューにタスクを追加

    # 乾燥係
    def dryer(input):
        while True:  # キューに登録されるタスクを待ち、タスクが発生し次第とり出して実行する
            dish = input.get()
            print('Drying', dish, 'dish')
            input.task_done()

    dish_queue = mp.JoinableQueue()
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()  # dryer関数を別個のプロセスとして起動
    dishes = ['salad', 'bread', 'entree', 'dessert']
    washer(dishes, dish_queue)  # 洗浄係(タスクを終え次第キューを介して乾燥係にタスクを渡す)
    dish_queue.join()  # dryerが全ての仕事を終えるまで待つ


# スレッド
def threading_process():
    import threading as trd

    def do_this(what):
        whoami(what)

    def whoami(what):
        print("Thread %s says: %s" % (trd.current_thread(), what))

    whoami("I'm the current process")
    for n in range(4):  # 4個分スレッドを作成して実行
        p = trd.Thread(
            target=do_this, args=("I'm function %s" % n,))
        p.start()


def thread_dishes():  # process_dishesのスレッドバージョン
    import threading as trd
    import queue
    import time

    def washer(dishes, dish_queue):
        for dish in dishes:
            print("Washing", dish)
            time.sleep(1)
            dish_queue.put(dish)

    def dryer(dish_queue):
        while True:
            dish = dish_queue.get()
            print("Drying", dish)
            time.sleep(2)
            dish_queue.task_done()

    dish_queue = queue.Queue()
    for n in range(2):
        dryer_thread = trd.Thread(
            target=dryer, args=(dish_queue,))
        dryer_thread.start()

    dishes = ['saled', 'bread', 'entree', 'desert']
    washer(dishes, dish_queue)
    dish_queue.join()


# グリーンスレッドと gevent : イベント駆動
def gethostbyname_gevent():
    import gevent
    from gevent import socket
    hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com',
             'www.antique-taxidermy.com']
    # gevent.spawn()はgevent.socket.gethostbyname(url)を実行するためにグリーンレットを作る
    # gethostbynameは非同期的に実行される
    jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
    gevent.joinall(jobs, timeout=5)  # 派生した全てのジョブが終了するのを待つ
    for job in jobs:
        print(job.value)


def monkey_patching_gevent():
    import gevent
    from gevent import monkey
    monkey.patch_all()  # socketなどの標準ライブラリがグリーンレットを使うように書き換えるモンキーパッチング
    import socket
    hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com',
             'www.antique-taxidermy.com']
    # 標準ライブラリのsocketだが書き換えられている
    jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
    gevent.joinall(jobs, timeout=5)
    for job in jobs:
        print(job.value)


# twisted : 非同期のイベント駆動型ネットワーキングフレームワーク
def twisted_knock_server():  # 小さなノックサーバー
    from twisted.internet import protocol, reactor

    class Knock(protocol.Protocol):  # コネクションを定義するProtocol派生クラス
        def dataReceived(self, data):  # クライアントからデータを受け取ったら駆動するメソッド
            print('Client: ' + data)
            if data.startswith("Knock knock"):
                response = "Who's there?"
            else:
                response = data + " who?"
            print('Server: ' + response)
            self.transport.write(response)

    class KnockFactory(protocol.Factory):  # コネクションを生成するファクトリ
        def buildProtocol(self, addr):
            return Knock()

    reactor.listenTCP(8000, KnockFactory())  # 8000ポートでクライアントからのTCP接続を待機
    print('exit: ctl+c')
    reactor.run()


def twisted_knock_client():  # 小さなノッククライアント
    from twisted.internet import reactor, protocol

    class KnockClient(protocol.Protocol):  # コネクションを定義するProtocol派生クラス
        def connectionMade(self):  # コネクション生成時に実行
            self.transport.write("Knock knock")

        def dataReceived(self, data):  # サーバーからデータを受け取った時に駆動するメソッド
            if data.startswith("Who's there?"):
                response = "Disappering client"
                self.transport.write(response)
            else:
                self.transport.loseConnection()
                reactor.stop()

    class KnockFactory(protocol.ClientFactory):  # コネクションを生成するクライアントファクトリ
        protocol = KnockClient

    f = KnockFactory()
    reactor.connectTCP("localhost", 8000, f)  # サーバーの8000ポートに接続
    reactor.run()


# Redis : Redis サーバーによるキューの実現
def redis_washer():  # リストにメッセージをプッシュしていくプロバイダクライアント
    import redis
    conn = redis.Redis()
    print('Washer is starting')
    dishes = ['salad', 'bread', 'entree', 'dessert']
    for dish in dishes:
        msg = dish.encode('utf-8')
        conn.rpush('dishes', msg)  # dishesリストの末尾にmsgを追加していく
        print('Washed', dish)
    conn.rpush('dishes', 'quit')  # 最後にquitメッセージ(終わりを表す番兵値)を送る
    print('Washer is done')


def redis_dryer():  # ブロックを起こすポップ処理を行うワーカークライアント
    import redis
    conn = redis.Redis()
    print('Dryer is starting')
    while True:
        msg = conn.blpop('dishes')  # ブロックを起こすポップ処理(メッセージが届くまでここで待機)
        if not msg:
            break
        val = msg[1].decode('utf-8')
        if val == 'quit':  # 終わりを表す番兵値
            break
        print('Dried', val)
    print('Dishes are dried')


def redis_dryer_mw():  # 複数のワーカーが独立したプロセスとして働く
    import multiprocessing

    def dryer():
        import redis
        import os
        import time
        conn = redis.Redis()
        pid = os.getpid()
        timeout = 20
        print('Dryer process %s is starting' % pid)
        while True:
            msg = conn.blpop('dishes', timeout)
            if not msg:
                break
            val = msg[1].decode('utf-8')
            if val == 'quit':
                break
            print('%s: dried %s' % (pid, val))
            time.sleep(0.1)
        print('Dryer process %s is done' % pid)

    DRYERS = 3
    for num in range(DRYERS):  # 3つのdryerプロセスが働く
        p = multiprocessing.Process(target=dryer)
        p.start()


# その他 Python ベースのキューパッケージ
other_queue = {
    'celery', 'thoonk', 'rq',
    }


#
# $ python3 Parallel.py runfunc ... 起動用
#
if (__name__ == '__main__') and (len(sys.argv) > 1):
        print('runnning: ' + sys.argv[1])
        if len(sys.argv) > 2:
            eval(sys.argv[1])(tuple(sys.argv[2:]))
        else:
            eval(sys.argv[1])()
