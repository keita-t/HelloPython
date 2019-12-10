#!/usr/bin/python

#
# ファイル入出力
#

# ファイル操作のモード
mode = {
    'r': '読み出し',
    'w': '書き込み（上書き）',
    'x': '書き込み（ファイルが存在しない時のみ）',
    'a': '追記(末尾の後ろに書き込み)',
    't': 'テキスト',
    'b': 'バイナリ',
    }

# write() によるテキストファイルへの書き込み
poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''
print(len(poem))

fout = open('files/relativity.txt', 'wt')  # poem を files/relativity.txt に書き込む
fout.write(poem)
fout.close()

fout = open('files/relativity.txt', 'wt')
print(poem, file=fout)  # print 関数でも書き込みが出来る(デフォルトで末尾が改行となる)
fout.close()

fout = open('files/relativity.txt', 'wt')
print(poem, file=fout,
      sep='', end='')  # sep=セパレータ(デフォルトは' '), end=末尾の文字列(デフォルトは'\n')
fout.close()

fout = open('files/relativity.txt', 'wt')
size = len(poem)
offset, chunk = 0, 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])  # 全部書き込むまでチャンクに分けて順次書き込む
    offset += chunk
fout.close()

try:
    fout = open('files/relativity.txt', 'xt')  # xモードだと上書き出来ない
    fout.wite('stomp', 'stomp', 'stomp')  # 書き込めず例外発生
except Exception:
    print('relativity already exists!. That was a close one.')

# read(), readline(), readlines() によるテキストファイルの呼び出し
fin = open('files/relativity.txt', 'rt')
poem = fin.read()  # ファイル全体を一度に読みだす(大きなサイズのファイルに注意)
fin.close()
print(len(poem))

poem = ''
fin = open('files/relativity.txt', 'rt')
while True:
    line = fin.readline()  # ファイルを1行ずつ読み出す
    if not line:
        break
    poem += line  # １行ずつ poem に追加していく
fin.close()
print(len(poem))

poem = ''
fin = open('files/relativity.txt', 'rt')
for line in fin:  # イテレータで１行ずつ読み込む
    poem += line
fin.close()
print(len(poem))

fin = open('files/relativity.txt', 'rt')
lines = fin.readlines()  # 一度に１行ずつ読み出して、１行文字列のリストを返す
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end='')

print('')

# write() によるバイナリファイルの書き込み
bdata = bytes(range(0, 256))  # 0 から 255 までの 256 バイトの生成
print(len(bdata))

fout = open('files/bfile', 'wb')  # バイナリモードで開く
print(fout.write(bdata))  # バイトを書き込み(書き込んだバイト数を返す)
fout.close()

fout = open('files/bfile', 'wb')
size = len(bdata)
offset, chunk = 0, 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])  # バイナリデータをチャンク単位で書き込む
    offset += chunk
fout.close()

# read() によるバイナリファイルの読み出し
fin = open('files/bfile', 'rb')  # バイナリモードで読み込み
bdata = fin.read()  # bdata にバイナリを読み込む
print(len(bdata))
fin.close()

# with によるファイルの自動的なクローズ
with open('files/relativity.txt', 'wt') as fout:  # コンテキストマネージャ
    print(fout.write(poem))  # コードブロック終了時に自動的にファイルを閉じる

# seek() による位置の変更
fin = open('files/bfile', 'rb')
print(fin.tell())       # 現在のファイルの先頭からのオフセットを返す
print(fin.seek(255))    # ファイルの末尾の1バイト手前に移動(移動後のオフセットを返す)
bdata = fin.read()      # 1バイト読み込む
print(len(bdata))       # 1
print(bdata[0])         # 255


def seek():
    import os
    os.SEEK_SET     # 0: 先頭から offset バイトの位置に移動する
    os.SEEK_CUR     # 1: 現在の位置から offset バイトの位置に移動する
    os.SEEK_END     # 2: 末尾から offset バイトの位置に移動する

    fin = open('files/bfile', 'rb')
    fin.seek(-1, os.SEEK_END)   # ファイルの末尾よりも１バイト前に移動する
    print(fin.tell())           # 現在位置は 255
    bdata = fin.read()          # ファイルの末尾まで読みだす
    print(len(bdata))           # 1
    print(bdata[0])             # 255
    fin.close()

    fin = open('files/bfile', 'rb')
    fin.seek(254, os.SEEK_SET)  # ファイルの末尾2バイト前に移動する
    print(fin.tell())           # 254
    fin.seek(1, 1)              # 1バイト前進する
    print(fin.tell())           # 255
    bdata = fin.read()          # ファイルの末尾まで読みだす
    print(len(bdata))           # 1
    print(bdata[0])             # 255


seek()


#
# 構造化されたテキストファイル
#


# CSV
def write_csv():
    import csv
    villains = [  # 列のリストが含まれるような行のリスト(CSV)
        ['Doctor', 'No'],
        ['Rosa', 'Klebb'],
        ['Mister', 'Big'],
        ['Auric', 'Goldfinger'],
        ['Ernst', 'Blofeld'],
        ]
    with open('files/villains.csv', 'wt') as fout:  # コンテキストマネージャ
        csvout = csv.writer(fout)   # CSV形式で書き込む writer オブジェクト
        csvout.writerows(villains)  # villains を書き込み


def read_csv():
    import csv
    with open('files/villains.csv', 'rt') as fin:
        cin = csv.reader(fin)  # CSV形式で読み込む reader オブジェクト
        villains = [row for row in cin]  # 行をリストとして抽出
    print(villains)


def read_dict_csv():
    import csv
    with open('files/villains.csv', 'rt') as fin:
        cin = csv.DictReader(
            fin, fieldnames=['first', 'last'])  # 列名(first, last)を指定して辞書で読み込む
        villains = [row for row in cin]  # 行を辞書とするリストを抽出
    print(villains)


def write_dict_csv():
    import csv
    villains = [  # 列をキーとする辞書による行のリスト(CSV)
        {'last': 'No', 'first': 'Doctor'},
        {'last': 'Klebb', 'first': 'Rosa'},
        {'last': 'Big', 'first': 'Mister'},
        {'last': 'Goldfinger', 'first': 'Auric'},
        {'last': 'Blofeld', 'first': 'Ernst'}
        ]
    with open('files/villains.csv', 'wt') as fout:
        cout = csv.DictWriter(fout, ['first', 'last'])  # 辞書のリストを書き込む writer
        cout.writeheader()  # CSV ファイルの先頭に列名(first, last)を書き込む
        cout.writerows(villains)  # 辞書のリストを行として書き込む


def read_dict_field_csv():
    import csv
    with open('files/villains.csv', 'rt') as fin:
        cin = csv.DictReader(fin)  # fieldnames　を省略すると、ヘッダー(第1行の値)が列ラベル
        villains = [row for row in cin]  # 辞書のリストを読み込む
    print(villains)


write_csv()
read_csv()
read_dict_csv()
write_dict_csv()
read_dict_field_csv()


# XML
def read_menu_xml():
    import xml.etree.ElementTree as et
    tree = et.ElementTree(file='files/menu.xml')  # menu.xml をツリー構造で読み込む
    root = tree.getroot()   # ルートを取得
    print(root.tag)         # menu

    for child in root:  # ルートから子をたどる
        print('tag:', child.tag, 'attributes;', child.attrib)
        for grandchild in child:  # 子の子をたどる
            print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)

    print(len(root))        # menu セクションの数
    print(len(root[0]))     # 朝食の項目の数


read_menu_xml()


# JSON
menu = {  # サンプルデータを格納する Python データ構造
 "breakfast": {
        "hours": "7-11",
        "items": {
                "breakfast burritos": "$6.00",
                "pancakes": "$4.00"
                }
        },
 "lunch": {
        "hours": "11-3",
        "items": {
                "hamburger": "$5.00"
                }
        },
 "dinner": {
        "hours": "3-10",
        "items": {
                "spaghetti": "$8.00"
                }
        }
}


def convert_menu_json():
    import json
    menu_json = json.dumps(menu)  # menu を JSON文字列(menu_json) にエンコード
    print(menu_json)

    menu2 = json.loads(menu_json)  # JSON文字列(menu_json) を Python データ構造(menu2)に
    print(menu2)


def datetime_json():
    import json
    import datetime
    from time import mktime
    now = datetime.datetime.utcnow()
    print(now)  # 現在の UTC 時間を表示

    try:
        json.dumps(now)  # JSON標準が日付、時計型を定義していないので例外が発生する
    except TypeError:
        print("'datetime' is not JSON serializable")

    print(json.dumps(str(now)))  # 文字列にするとJSONが理解できる
    print(json.dumps(int(mktime(now.timetuple()))))  # Unix時間にするとJSONが理解できる

    class DTEncoder(json.JSONEncoder):  # 継承による JSON のエンコード方法の変更
        def default(self, obj):  # JSONEncoder の default をオーバーライド
            # instance() は obj の型をチェックする
            if isinstance(obj, datetime.datetime):
                return int(mktime(obj.timetuple()))
            # でなければ、通常のデコーダの処理を行う
            return json.JSONEncoder.default(self, obj)

    print(json.dumps(now, cls=DTEncoder))  # DTEncoder を使って datetime を処理する

    # isinstance() ： 第1引数が第2引数で指定したオブジェクトの型と一致した場合 True を返す
    print(type(now))                            # <class 'datetime.datetime'>
    print(isinstance(now, datetime.datetime))   # True
    print(type(234))                            # <class 'int'>
    print(isinstance(234, int))                 # True
    print(type('hey'))                          # <class 'str'>
    print(isinstance('hey', str))               # True


convert_menu_json()
datetime_json()


# YAML
def load_yaml():
    import yaml
    with open('files/mcintyre.yaml', 'rt') as fin:
        text = fin.read()  # mcintyre.yaml をテキストとして読み込む
    data = yaml.safe_load(text)  # YAML 形式として安全に変換
    print(data['details'])  # {'themes': ['cheese', 'Canada'], 'bearded': True}
    print(len(data['poems']))  # poems の個数は 2
    print(data['poems'][1]['title'])  # poems の２つ目の title


load_yaml()


# 設定ファイル
def read_ini_config():
    import configparser
    cfg = configparser.ConfigParser()
    print(cfg.read('files/settings.cfg'))  # 設定ファイルを読み込む(成功したファイル名のリストを返す)
    print(cfg['french'])  # <Section: french>
    print(cfg['french']['greeting'])  # Bonjour
    print(cfg['files']['bin'])  # /usr/local/bin


read_ini_config()


# pickle によるシリアライズ
def pickle_serialize():
    import pickle
    import datetime
    now1 = datetime.datetime.utcnow()  # 現在の UTC 時間を取得
    pickled = pickle.dumps(now1)  # datetime型のシリアライズ
    now2 = pickle.loads(pickled)  # datetime型のデシリアライズ
    print(now1)
    print(now2)


class Tiny():  # 文字列を返す小さなクラス
    def __str__(self):
        return 'tiny'


def pickle_serialize2():
    import pickle
    obj1 = Tiny()
    print(obj1)
    print(str(obj1))
    pickled = pickle.dumps(obj1)  # 独自クラスのオブジェクトをシリアライズ
    obj2 = pickle.loads(pickled)  # デシリアライズ
    print(obj2)
    print(str(obj2))  # 'tiny'


pickle_serialize()
pickle_serialize2()
