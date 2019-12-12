#!/usr/bin/Python

#
# リレーショナルデータベース
#

# SQL

# DDL(データ定義言語): テーブルやデータベースの作成、削除、制約、許可などの処理
# DML(データ操作言語): データの挿入、選択、更新、削除などの処理

# SQL DDL の基本コマンド
SQL_DDL = {  # パターン : 操作 : サンプル
    'CREATE DATABASE dbname':
        ('データベースの作成', 'CREATE DATABASE d'),
    'USE dbname':
        ('現在のデータベースの選択', 'USE d'),
    'DROP DATABASE dbname':
        ('データベースとテーブルの削除', 'DROP DATABASE d'),
    'CREATE TABLE tbname (coldefs)':
        ('テーブルの作成', 'CREATE TABLE t (id INT, count INT)'),
    'DROP TABLE tbname':
        ('テーブルの削除', 'DROP TABLE t'),
    'TRUNCATE TABLE tbname':
        ('テーブルのすべての行の削除', 'TRUNCATE TABLE t'),
    }

# SQL DML の主要な操作
SQL_DML_CRUD = {
    'C(Create)': 'INSERT文を使った作成',
    'R(Read)':   'SELECT文を使った読み出し',
    'U(Update)': 'UPDATE文を使った更新',
    'D(Delete)': 'DELETE文を使った削除',
    }

# SQL DML の基本コマンド
SQL_DML = {  # パターン : 操作 : サンプル
    'INSERT INTO tbname VALUES (...)':
        ('行の追加', 'INSERT INTO t VALUES(7, 40)'),
    'SELECT * FROM tbname':
        ('すべての行と列の選択', 'SELECT * FROM t'),
    'SELECT cols FROM tbname':
        ('すべての行と特定の列の選択', 'SELECT id, count FROM t'),
    'SELECT cols FROM tbname WHERE condition':
        ('一部の行の一部の列の選択', 'SELECT id, count FROM t WHERE count > 5 AND id = 9'),
    'UPDATE tbname SET col = value WHERE condition':
        ('一部の行の列の変更', 'UPDATE t SET count = 3 WHERE id = 5'),
    'DELETE FROM tbname WHERE condition':
        ('一部の行の削除', 'DELETE FROM t WHERE count <= 10 OR id = 16'),
    }

# DB-API (リレーショナルデータベースにアクセスするための PYthon の標準 API)
DB_API = {
    'connect()':
        'データベースへの接続を開設',
    'cursor()':
        'クエリーを管理するカーソルオブジェクトを作る',
    'execute(), executemany()':
        'データベースに対してひとつまたは複数のSQLコマンドを実行',
    'fetchone(), fetchmany(), fetchall()':
        'executeの結果を取得する',
    }

# SQLite

# enterprise.db : zooテーブルの列
zoo = {
    'critter': '動物の名前、主キー(可変長文字列)',
    'count':   'その動物の現在の個体数(整数)',
    'damages': '動物とのふれあいによる現在の損失額(整数)',
    }


def zoo_sqlite():
    import sqlite3
    conn = sqlite3.connect('files/enterprise.db')  # enterprise.db の作成
    curs = conn.cursor()  # カーソルオブジェクトの作成
    query = 'CREATE TABLE zoo' + \
            '(critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)'
    try:
        curs.execute(query)  # SQLコマンドの実行(zooテーブルの作成)
    except sqlite3.OperationalError:
        print('table zoo already exists')

    curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')  # duckを追加
    curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')  # bearを追加

    # プレースホルダーを使った安全な挿入(SQLインジェクションからシステムを守る)
    ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
    curs.execute(ins, ('weasel', 1, 2000.0))  # weaselを追加

    curs.execute('SELECT * FROM zoo')  # すべての情報を引き出す
    rows = curs.fetchall()  # 実行
    print(rows)

    curs.execute('SELECT * from zoo ORDER BY count')  # 個体数順にソートする
    rows = curs.fetchall()
    print(rows)

    curs.execute('SELECT * from zoo ORDER BY count DESC')  # 個体数順にソート(降順)
    rows = curs.fetchall()
    print(rows)

    query = 'SELECT * FROM zoo WHERE ' + \
            'damages = (SELECT MAX(damages) FROM zoo)'
    curs.execute(query)  # もっとも損失の大きい動物は何か
    rows = curs.fetchall()
    print(rows)

    curs.close()    # カーソルを閉じる
    conn.close()    # コネクションを閉じる


zoo_sqlite()


# MySQL

# MySQL ドライバ
MySQL_Driver = {  # 名前 : インポート名 : Pypi パッケージ
    'MySQL Connector': ('mysql.connector', 'mysql-connector-python'),
    'PYMySQL': ('pymysql', 'pymysql'),
    'oursql': ('oursql', 'oursql'),
    }

# PostgreSQL

# PostgreSQL ドライバ
PostgreSQL_Driver = {  # 名前 : インポート名 : Pypi パッケージ
    'psycopg2': ('psycopg2', 'psycopg2'),
    'py-postgresql': ('postgresql', 'py-postgresql'),
    }

# SQLAlchemy (リレーショナルデータベースの差異を埋めるマッパー)
#
# dialect + driver://usr:password@host:port/dbname
#
# dialect: データベースのタイプ
# driver: そのデータベースに対して使いたいと思っているドライバ
# userとpassword: データベースの認証文字列
# hostとport: データベースサーバーの位置(port:はデフォルトのポートなら不要)
# dbname: 最初に接続するサーバー上のデータベース

# SQLAlchemy の接続先
SQLAlchemy_Connection = {  # 方言 : ドライバ
    'sqlite', 'pysqlite(または省略)',
    'mysql', 'musqlconnector',
    'mysql', 'pymysql',
    'mysql', 'ousql',
    'postgresql', 'psycopg2',
    'postgresql', 'pypostgresql',
    }


# SQLAlchemy: エンジンレイヤ
def sqlalchemy_enginelayer():
    import sqlalchemy as sa
    conn = sa.create_engine('sqlite:///:memory:')  # データベースを作りメモリ内に記憶領域を作る
    query = '''CREATE TABLE zoo
            (critter VARCHAR(20) PRIMARY KEY,
             count INT,
             damages FLOAT)'''
    print(conn.execute(query))  # zooテーブルの作成(ResultProxyオブジェクトが返される)

    ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
    conn.execute(ins, 'duck', 10, 0.0)      # duckを挿入
    conn.execute(ins, 'bear', 2, 1000.0)    # bearを挿入
    conn.execute(ins, 'weasel', 1, 2000.0)  # weaselを挿入

    rows = conn.execute('SELECT * FROM zoo')  # すべての情報をデータベースに要求
    print(rows)  # ResultProxyオブジェクトが返っている
    for row in rows:
        print(row)  # 内容はイテレーションで取得できる


# SQLAlchemy: SQL 表現言語
def sqlalchemy_metadata():
    import sqlalchemy as sa
    conn = sa.create_engine('sqlite:///:memory:')  # データベースを作りメモリ内に記憶領域を作る

    meta = sa.MetaData()  # zooテーブルの定義に表現言語を使う
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)
    zoo = sa.Table('zoo', meta, critter, count, damages)
    meta.create_all(conn)

    conn.execute(zoo.insert(('bear', 2, 1000.0)))       # bearを追加
    conn.execute(zoo.insert(('weasel', 1, 2000.0)))     # weaselを追加
    conn.execute(zoo.insert(('duck', 10, 0)))           # duckを追加

    result = conn.execute(zoo.select())  # zooオブジェクトが表現するテーブルからすべての情報を取得
    rows = result.fetchall()
    print(rows)


# SQLAlchemy: ORM(Object Relational Mapping)
def sqlalchemy_orm():
    import sqlalchemy as sa
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    conn = sa.create_engine('sqlite:///:memory:')

    Base = declarative_base()

    class Zoo(Base):  # zooテーブルを実現するクラス(ORM)
        __tablename__ = 'zoo'
        critter = sa.Column('critter', sa.String, primary_key=True)
        count = sa.Column('count', sa.Integer)
        damages = sa.Column('damages', sa.Float)

        def __init__(self, critter, count, damages):
            self.critter = critter
            self.count = count
            self.damages = damages

        def __repr__(self):
            return "<Zoo({}, {}, {})>".format
            (self.critter, self.count, self.damages)

    Base.metadata.create_all(conn)  # クラスで定義したzooテーブルとデータベースの作成

    first = Zoo('duck', 10, 0.0)        # duck行
    second = Zoo('bear', 2, 1000.0)     # bear行
    third = Zoo('weasel', 1, 2000.0)    # weasel行

    Session = sessionmaker(bind=conn)  # データベースとやり取りするためのセッションを作成
    session = Session()
    session.add(first)  # duckを追加
    session.add_all([second, third])   # bearとweaselをリストで追加
    session.commit()  # データベースにコミット


sqlalchemy_enginelayer()
sqlalchemy_metadata()
sqlalchemy_orm()


#
# NoSQL データストア
#


# dbm ファミリ (キーバリューストア)
def dbm_datastore():
    import dbm
    db = dbm.open('files/definitions.dbm', 'c')  # 読み書き両用でdbmファイルをオープン

    db['mustard'] = 'yellow'
    db['ketchup'] = 'red'
    db['pesto'] = 'green'

    print(len(db))      # 3
    print(db['pesto'])  # b'green'

    db.close()  # ファイルを閉じる
    db = dbm.open('files/definitions.dbm', 'r')  # 書き込みモードで開く
    print(db['mustard'])  # b'yellow'


dbm_datastore()


# memcached (インメモリのキャッシュサーバー)
def memcached():
    import memcache
    db = memcache.Client(['127.0.0.1:11211'])  # memcached サーバーに接続
    print(db.set('marco', 'polo'))  # キー 'marco', 値 'polo' で登録(True)
    print(db.get('marco'))          # キー 'marco' で値の取得('polo')
    print(db.set('ducks', 0))       # キー 'ducks', 値 0 で登録(True)
    print(db.get('ducks'))          # 0
    print(db.incr('ducks', 2))      # ducks の値を 2 に更新
    print(db.get('ducks'))          # 2


# memcached()


# Redis (データ構造サーバー)
def redis():
    import redis
    import time
    conn = redis.Redis('localhost', 6379)  # redis-server に接続

    # 文字列
    print(conn.keys('*'))  # すべてのキーのリストを表示(今のところキーなし)
    print(conn.set('secret', 'ni!'))  # キー 'secret', 値 'ni!'(文字列)(True)
    print(conn.set('carats', 24))  # キー 'carats', 値　24(整数)(True)
    print(conn.set('fever', '101.5'))  # キー 'fever', 値　101.5(float)(True)
    print(conn.get('secret'))  # b'ni!'
    print(conn.get('carats'))  # b'24'
    print(conn.get('fever'))  # b'101.5'
    print(conn.setnx(
        'secret', 'icky-icky-icky-ptang-zoop-boing!'))  # キーが存在しない時に限り設定(False)
    print(conn.get('secret'))  # b'ni!'
    print(conn.getset(
        'secret', 'icky-icky-icky-ptang-zoop-boing!'))  # もとの値を返して新しく設定(b'ni!')
    print(conn.get('secret'))  # b'icky-icky-icky-ptang-zoop-boing!'
    print(conn.getrange('secret', -6, -1))  # 部分文字列の取り出し(b'boing!')
    print(conn.setrange('secret', 0, 'ICKY'))  # 部分文字列を置換(32,文字列の長さ)
    print(conn.get('secret'))  # b'ICKY-icky-icky--ptang-zoop-boing!'
    print(conn.mset({'pie': 'cherry', 'cordial': 'sherry'}))  # 同時に複数設定(True)
    print(conn.mget(['fever', 'carats']))  # 同時に複数の値を得る([b'101.5, b''24'])
    print(conn.delete('fever'))  # キーを削除(1)
    print(conn.incr('carats'))  # 値をインクリメント(24+1=25)
    print(conn.incr('carats', 10))  # 25+10=35
    print(conn.decr('carats'))  # 35-1=34
    print(conn.decr('carats', 15))  # 34-15=19
    print(conn.set('fever', '101.5'))  # True
    print(conn.incrbyfloat('fever'))  # floatをインクリメント(101.5+1=102.5)
    print(conn.incrbyfloat('fever', 0.5))  # 102.5+0.5=103.0
    print(conn.incrbyfloat('fever', -2.0))  # 実質デクリメント(103.0-2.0=101.0)

    conn.flushall()

    # リスト
    print(conn.lpush('zoo', 'bear'))  # リストzoozの先頭にbearを追加(1)
    print(conn.lpush('zoo', 'alligator', 'duck'))  # 先頭に複数の要素を追加(3)
    print(conn.lrange('zoo', 0, 2))  # duck, alligator, bear の順になっている
    print(conn.linsert(
        'zoo', 'before', 'bear', 'beaver'))  # bearの前にbeaverを追加(4)
    print(conn.linsert(
        'zoo', 'after', 'bear', 'cassowary'))  # bearの後にcassowaryを追加(5)
    print(conn.lset('zoo', 2, 'marmoset'))  # index 2 の位置にmarmosetを挿入(True)
    print(conn.rpush('zoo', 'yak'))  # 末尾にyakを追加(6)
    print(conn.lindex('zoo', 3))  # 指定したオフセットの値を得る(b'bear')
    print(conn.lrange('zoo', 0, 2))  # 範囲(b'duck',b'alligator',b'marmoset')
    print(conn.ltrim('zoo', 1, 4))  # リストの刈り込み,指定されたオフセットの範囲の要素が残る(True)
    print(conn.lrange('zoo', 0, -1))  # 0から-1で全体の値を得る

    conn.flushall()

    # ハッシュ
    print(conn.hmset('song', {
        'do': 'a deer', 're': 'about a deer'}))  # songハッシュにdo,reを追加(True)
    print(conn.hset('song', 'mi', 'a note to follow re'))  # miキーの値を追加(1)
    print(conn.hget('song', 'mi'))  # miキーの値を取得(b'a note to follow re')
    print(conn.hmget(
        'song', 're', 'do'))  # 複数のキー(re,do)から取得([b'about a beer', b'a deer'])
    print(conn.hkeys('song'))  # すべてのキーを取得([b'do', b're', b'mi'])
    print(conn.hvals('song'))  # すべての値([b'a deer', ... b'a note to follow re'])
    print(conn.hvals('song'))  # フィールドの数を取得(3)
    print(conn.hgetall('song'))  # すべてのキーと値を取得({b'do': b'a deer', ... })
    print(conn.hsetnx('song', 'fa', 'a note that rhymes with la'))  # キーがなければ設定

    conn.flushall()

    # 集合
    print(conn.sadd(
        'zoo', 'duck', 'goat', 'turkey'))  # duck,goat,turkeyの集合zoo(3)
    print(conn.scard('zoo'))  # 集合の値の数を取得(3)
    print(conn.smembers('zoo'))  # 集合のすべての値を取得({b'duck', b'goat', b'turkey'})
    print(conn.srem('zoo', 'turkey'))  # turkeyを取り除く(1)
    print(conn.sadd('better_zoo', 'tiger', 'wolf', 'duck'))  # 集合better_zooを作る
    print(conn.sinter('zoo', 'better_zoo'))  # zooとbetter_zooの積集合({b'duck'})
    print(conn.sinterstore(
        'fowl_zoo', 'zoo', 'better_zoo'))  # fowl_zooにzooとbetter_zooの積集合を格納(1)
    print(conn.smembers('fowl_zoo'))  # {b'duck'}
    print(conn.sunion(
        'zoo', 'better_zoo'))  # zooとbetter_zooの和集合({b'duck', ... b'tiger'})
    print(conn.sunionstore(
        'fabulous_zoo', 'zoo', 'better_zoo'))  # fablous_zooに和集合を格納(4)
    print(conn.smembers('fabulous_zoo'))  # {b'duck',b'goat',b'wolf',b'tiger'}
    print(conn.sdiff('zoo', 'better_zoo'))  # zooとbetter_zooの差集合({b'goat'})
    print(conn.sdiffstore(
        'zoo_sale', 'zoo', 'better_zoo'))  # zoo_saleにzooとbetter_zooの差集合を格納(1)
    print(conn.smembers('zoo_sale'))  # {b'goat'}

    conn.flushall()

    # ソート済み集合
    now = time.time()  # 現在時間を基にしてソート
    print(conn.zadd('logins', {'smeagol': now}))  # logins集合に最初のゲストsmeagolを追加
    print(conn.zadd('logins', {'sauron': now+(5*60)}))  # 5分後に次のゲスト(sauron)
    print(conn.zadd('logins', {'bilbo': now+(2*60*60)}))  # 2時間後に次のゲスト(bilbo)
    print(conn.zadd('logins', {'treebeard': now+(24*60*60)}))  # 1日後(treebeard)
    print(conn.zrank('logins', 'bilbo'))  # bilboがやってきたのは2番目(2)
    print(conn.zscore('logins', 'bilbo'))  # それは何時か(now+(24*60*60))
    print(conn.zrange('logins', 0, -1))  # 全員をログイン順に見る([b'smeagol', ... ])
    print(conn.zrange('logins', 0, -1, withscores=True))  # 時間付きでログイン順

    conn.flushall()

    # ビット
    days = ['2013-02-25', '2013-02-26', '2013-02-27']  # 3日間
    big_spender = 1089      # ID
    tire_kicker = 40459     # ID
    late_joiner = 550212    # ID

    print(conn.setbit(days[0], big_spender, 1))  # 最初の日にbig_spenderがログイン(0)
    print(conn.setbit(days[0], tire_kicker, 1))  # 最初の日にtire_kickerがログイン(0)
    print(conn.setbit(days[1], big_spender, 1))  # 次の日もbig_spenderがログイン(0)
    print(conn.setbit(days[2], big_spender, 1))  # 3日目もbig_spenderがログイン(0)
    print(conn.setbit(days[2], late_joiner, 1))  # 3日目にlate_joinerがログイン(0)
    for day in days:
        conn.bitcount(day)  # この３日の各日の訪問者数(2, 1, 2)
    print(conn.getbit(days[1], tire_kicker))  # tire_kickerは２日目には来ていない(0)
    conn.bitop('and', 'everyday', *days)  # 毎日ログインしてきたユーザー
    print(conn.bitcount('everyday'))  # １人(1)
    print(conn.getbit('everyday', big_spender))  # big_spenderだった(1)
    conn.bitop('or', 'alldays', *days)  # ３日間のユニークユーザーの合計
    print(conn.bitcount('alldays'))  # 3人(3)

    # キーの有効期限
    key = 'now you see it'
    conn.set(key, 'but not for long')
    print(conn.expire(key, 5))  # キーを５秒間有効にする(True)
    print(conn.ttl(key))  # 5
    print(conn.get(key))  # まだ生存している(b'but not for long')
    time.sleep(6)  # 6秒間スリープ
    print(conn.get(key))  # 期限切れでもうないので取得できない


# redis()
