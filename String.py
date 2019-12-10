#!/usr/bin/python

#
# 文字列
#

print('Snap')        # シングルクォート
print("Crackle")     # ダブルクォート

# トリプルクォート（複数行の文字列）
poem = '''There was a Young Lady of Norway,
Who casually sat in a doorway;
When the door squeezed her flat,
She exclaimed, "What of that?"
This courageous Young Lady of Norway.'''
print(poem)

# 文字列変換
print(str(98.6))
print(str(1.0e4))
print(str(True))

# エスケープ
print("\"Text A\tText B\"\n\'Text C\'")

# 連結
print('Release the Kraken!' + 'At once!')
print("My word! " "A gentlemen caller!")

# 繰り返し
print('Na ' * 4)
print('Hey ' * 4)

letters = 'abcdefghijklmnopqrstuvwxyz'

# 抽出
print(letters[0])
print(letters[-1])
print(letters[-2])
print(letters[25])

# スライス
# [start:end:step] ... end は　-1 となる
print(letters[:])
print(letters[20:])
print(letters[12:15])
print(letters[-3:])
print(letters[18:-3])
print(letters[-6:-2])
print(letters[::7])
print(letters[4:20:3])
print(letters[19::4])
print(letters[:21:5])
print(letters[-1::-1])  # 逆向きステップ
print(letters[::-1])    # 上に同じ

# 文字列の長さの取得 len()
print(len(letters))

# 文字列の分割 split()
todos = 'get gloves,get mask,give cat vitamins,call ambulance'
print(todos.split(','))

# 文字列の結合 join()
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)

# 多彩な文字列操作
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

print(poem[:13])                                # 12文字目まで取り出し
print(len(poem))                                # 何文字含まれているか
print(poem.startswith('All'))                   # 先頭は All?
print(poem.endswith('That\'s all, folks!'))     # では終わりの文字列は?

word = 'the'

print(poem.find(word))         # 最初に the が現れる位置
print(poem.rfind(word))        # 最後に the が現れる位置
print(poem.count(word))        # the は何回現れるか
print(poem.isalnum())          # 全て英字と数字か（記号もあるので False）

# 大文字と小文字の区別と配置
setup = 'a duck goes into a bar...'

print(setup.strip('.'))                         # .のシーケンスを取り除く
print(setup.capitalize())                       # 先頭の単語だけタイトルケース
print(setup.title())                            # 全ての単語をタイトルケース
print(setup.upper())                            # 全ての文字を大文字
print(setup.lower())                            # 全ての文字を小文字
print(setup.swapcase())                         # 大文字と小文字を逆に

print(setup.center(30))                         # 30 字分のスペースに中央揃え
print(setup.ljust(30))                          # 30 字分のスペースに左揃え
print(setup.rjust(30))                          # 30 字分のスペースに右揃え

print(setup.replace('duck', 'marmoset'))        # duck を marmoset に置換
print(setup.replace('duck', 'marmoset', 100))   # 最高で 100回　置換

#
# Unicode
#


def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)  # Unicode 文字を与えると大文字の名前を返す
    value2 = unicodedata.lookup(name)  # 名前を与えると Unicode 文字を返す
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))


unicode_test('A')       # ASCII 文字
unicode_test('$')       # ASCII 記号
unicode_test('\u00a2')  # Unicode 通過記号
unicode_test('\u20ac')  # 別の Unicode 通過記号
unicode_test('\u2603')  # スノーマン記号(☃)

place = 'caf\u00e9'     # café
print(place)
place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'   # 名前 (lookup) で指定
print(place)

u_umlaut = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'
drink = 'Gew' + u_umlaut + 'rztraminer'     # 文字を追加して文字列を組み立てる
print('Now I can finally have my', drink, 'in a', place)

print(len('$'))            # 文字数は 1
print(len('\U0002f47b'))   # Unicode の文字数を数える(文字数は 1)

# エンコーディング
encode = {
    'ascii': '古き良き7ビットASCII',
    'utf-8': '8ビット可変長エンコーディング',
    'latin-1': 'ISO 8859-1とも呼ばれているもの',
    'cp-1252': '一般的なWindowsエンコーディング',
    'unicode-escape': 'Python Unicodeリテラル形式 \\uxxxx \\Uxxxxxxxx',
    }

snowman = '\u2603'
print(len(snowman))     # snowman は 1 文字の Python Unicode 文字列
ds = snowman.encode('utf-8')
print(len(ds))          # ds は byte 変数(3バイトなので 3 を返す)
print(ds)

try:
    ds = snowman.encode('ascii')    # 有効な ASCII 文字ではない
except UnicodeEncodeError as err:
    print("'ascii' codec can't encode")

print(snowman.encode('ascii', 'ignore'))    # エンコード出来ないものを捨てる
print(snowman.encode('ascii', 'replace'))   # ? に置き換える
print(snowman.encode('ascii', 'backslashreplace'))  # unicode-escape 形式
print(snowman.encode('ascii', 'xmlcharrefreplace'))  # ウェブページで使えるエンティティ

# デコーディング
place = 'caf\u00e9'
print(place, type(place))               # Unicode 文字列
place_bytes = place.encode('utf-8')     # UTF-8 形式にエンコード(bytes)
print(place_bytes, type(place_bytes))   # 5バイト
place2 = place_bytes.decode('utf-8')    # バイト列を Unicode 文字列にデコード

try:
    place3 = place_bytes.decode('ascii')    # ASCII では無効
except UnicodeDecodeError as err:
    print("'ascii' codec can't decode")

#
# 書式指定
#

# % を使った古いスタイル
format = {
    '%s': '文字列',
    '%d': '10進整数',
    '%x': '16進整数',
    '%o': '8進整数',
    '%f': '10進float',
    '%e': '指数形式float',
    '%g': '10進floatまたは指数形式float',
    '%%': 'リテラルの%',
    }

print('%s' % 42)        # 文字列(42)
print('%d' % 42)        # 10進整数(42)
print('%x' % 42)        # 16進整数(2a)
print('%o' % 42)        # 8進整数(52)
print('%s' % 7.03)      # 文字列(7.03)
print('%f' % 7.03)      # 10進float（7.030000）
print('%e' % 7.03)      # 指数形式float(7.030000e+00)
print('%g' % 7.03)      # 10進floatまたは指数形式float(7.03)
print('%d%%' % 100)     # 整数とリテラルの % (100%)

actor = 'Richard Gere'
cat = 'Chester'
weight = 28
print("My wife's favorite actor is %s" % actor)         # actor の挿入
print("Our cat %s weights %s pounds" % (cat, weight))   # cat, weight (タプル）

n = 42
f = 7.03
s = 'string cheese'
print('%d %f %s' % (n, f, s))               # デフォルトの幅
print('%10d %10f %10s' % (n, f, s))         # 最小限の幅 10, 右揃え（余った部分はスペース）
print('%-10d %-10f %-10s' % (n, f, s))      # 同じ幅を使って左揃え
print('%10.4d %10.4f %10.4s' % (n, f, s))   # フィールド幅 10, 文字数制限 4, 右揃え
print('%.4d %.4f %.4s' % (n, f, s))         # フィールド幅指定なし, 文字数制限 4
print('%*.*d %*.*f %*.*s' %
      (10, 4, n, 10, 4, f, 10, 4, s))       # フィールド幅と字数制限を引数から指定

# {} と書式指定を使った新しいスタイル
print('{} {} {}'.format(n, f, s))           # もっとも簡単な使い方
print('{2} {0} {1}'.format(n, f, s))        # 引数の順序を指定(s,n,fの順)
print('{n} {f} {s}'.format
      (n=42, f=7.03, s='string cheese'))    # キーワード引数で指定
d = {'n': 42, 'f': 7.03, 's': 'string cheese'}
print('{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other'))  # 辞書で指定(引数{1}はother)
print('{n:d} {f:f} {s:s}'.format
      (n=42, f=7.03, s='string cheese'))    # : の後ろに型指定子を使える
print('{0:10d} {1:10f} {2:10s}'.format(n, f, s))     # フィールド幅 10, 右揃え(デフォルト)
print('{0:>10d} {1:>10f} {2:>10s}'.format(n, f, s))  # フィールド幅 10, >(右揃え)
print('{0:<10d} {1:<10f} {2:<10s}'.format(n, f, s))  # フィールド幅 10, <(左揃え)
print('{0:^10d} {1:^10f} {2:^10s}'.format(n, f, s))  # フィールド幅 10, ^(中央揃え)

try:
    '{0:>10.4d} {1:>10.4f} {2:>10.4s}'.format(n, f, s)  # 精度（小数点後ろ）は整数では使えない
except ValueError as err:
    print('Precision not allowed in integer format specifier')
    print('{0:>10d} {1:>10.4f} {2:>10.4s}'.format(n, f, s))  # 小数点以下の桁数, 文字列 4

print('{0:!^20s}'.format('BIG SALE'))  # フィールドの隙間を指定した文字(!)で埋める(パディング)

#
# 正規表現とマッチング
#


def basic_match():
    import re
    pattern = 'You'                     # パターン
    source = 'Young Frankenstein'       # ソース
    result = re.match(pattern, source)  # ソースの先頭がパターンになっているかチェック

    youpattern = re.compile(pattern)    # パターンを予めコンパイル
    result = youpattern.match(source)   # コンパイルによってマッチングのスピードが上がる

    print(result.group())


# match() による正確なマッチ
def match():
    import re
    pattern = 'You'
    source = 'Young Frankenstein'
    m = re.match(pattern, source)  # match は source の先頭がパターンに一致するか調べる
    if m:   # match はオブジェクトを返す。マッチした部分を確かめる
        print(m.group())

    pattern = '^You'  # パターンの先頭に ^ を付けても同じになる
    m = re.match(pattern, source)
    if m:
        print(m.group())

    pattern = 'Frank'
    m = re.match(pattern, source)
    if m:   # パターンがソースの先頭にないのでマッチせず False となる
        print(m.group())  # 実行されない

    pattern = '.*Frank'  # .(任意の一文字), *(任意の個数) で任意の個数の任意の文字(ワイルドカード)
    m = re.match(pattern, source)
    if m:
        print(m.group())  # Young Frank が返る


# search() による最初のマッチ
def search():
    import re
    pattern = 'Frank'
    source = 'Young Frankenstein'
    m = re.search(pattern, source)  # 任意の位置にあるパターンを探しマッチする
    if m:
        print(m.group())  # Frank が返る


# findall() によるすべてのマッチの検査
def findall():
    import re
    pattern = 'n'
    source = 'Young Frankenstein'
    m = re.findall(pattern, source)  # ソースの中でパターンにマッチするすべてのリストを返す
    print(m)    # 4つの n がマッチ
    print('Found', len(m), 'matches')   # ソースには n が４つあった　

    pattern = 'n.'  # n の後ろに任意の一文字が続いている
    m = re.findall(pattern, source)
    print(m)  # ng, nk, ns の３つがマッチ

    pattern = 'n.?'  # n の後ろに任意の一文字(オプション)が続いている
    m = re.findall(pattern, source)
    print(m)  # ng, nk, ns, n(最後の n)の４つがマッチ


# split() のよるマッチを利用した分割
def split():
    import re
    pattern = 'n'  # 分割文字列パターン
    source = 'Young Frankenstein'
    m = re.split(pattern, source)  # パターンで文字列を分割し、分割文字列のリストを返す
    print(m)  # ['You', 'g Fra', 'ke', 'stei', '']


# sub() によるマッチした部分の置換
def sub():
    import re
    pattern = 'n'   # 置換対象となるパターン
    repl = '?'      # 置換するパターン
    source = 'Young Frankenstein'
    m = re.sub(pattern, repl, source)
    print(m)  # 'You?g Fra?ke?stei?'


# パターンの特殊文字
pattern_escape = {
    r'\d': '１個の数字',
    r'\D': '１個の数字以外の数字',
    r'\w': '１個の英字',
    r'\W': '１個の英字以外の英字',
    r'\s': '１個の空白文字',
    r'\S': '１個の空白以外の文字',
    r'\b': '単語の境界（\\w と \\W の間）',
    r'\B': '単語の境界以外の文字間',
    }

# ※ 文字列の前に r をつけると Python のエスケープ文字は無効になる
# 　 正規表現のパターン文字列であることを正確に明示できる
# 　 例: r'\b' ... \b はバックスペースの意味だが、 r をつけることで単語の境界と明示できる


def find_printable_escape():
    import re
    import string
    printable = string.printable  # 100種類の印刷可能 ASCII 文字を取得
    print(printable)

    print(re.findall(r'\d', printable))  # 数字
    print(re.findall(r'\w', printable))  # 数字、英字、アンダースコアのいずれかに含まれるもの
    print(re.findall(r'\s', printable))  # 空白文字

    x = 'abc' + '-/*' + '\u00ea' + '\u0115'
    print(re.findall('\\w', x))  # ３つの ASCII 文字と２つの Unicode


# パターン ： メタ文字
pattern_meta = {
    'abc': 'リテラルのabc',
    '(expr)': 'expr',
    'expr1|expr2': 'expr1またはexpr2',
    '.': '\n以外の任意の文字',
    '^': 'ソース文字列の先頭',
    '$': 'ソース文字列の末尾',
    'prev?': '0個か1個のprev',
    'prev*': '0個以上のprev(欲張り)',
    'prev*?': '0個以上のprev(控えめ)',
    'prev+': '1個以上のprev(欲張り)',
    'prev+?': '1個以上のprev(控えめ)',
    'prev{m}': 'm個の連続したprev',
    'prev{m,n}': 'm個以上n個未満の連続したprev(欲張り)',
    'prev{m,n}?': 'm個以上n個未満の連続したprev(控えめ)',
    '[abc]': 'aまたはbまたはc(a|b|c)',
    '[^abc]': 'aまたはbまたはc以外',
    'prev(?=next)': 'nextが続いているprev',
    'prev(?!next)': 'nextが続いていないprev',
    '(?<=prev)next': 'prevが前にあるnext',
    '(?<!prev)next': 'prevが前にないnext',
    }


def find_source_meta():
    import re
    source = '''I wish I may, I wish I might
                Have a dish of fish tonight.'''

    pattern = 'wish'
    m = re.findall(pattern, source)  # 任意の位置にある wish を探す
    print(m)  # ['wish', 'wish']

    pattern = 'wish|fish'  # wish または fish
    m = re.findall(pattern, source)  # 任意の位置にある wish か fish を探す
    print(m)  # ['wish', 'wish', 'fish']

    pattern = '^wish'  # 先頭の wish
    m = re.findall(pattern, source)  # 先頭で wish を探す
    print(m)  # []

    pattern = '^I wish'  # 先頭の I wish
    m = re.findall(pattern, source)  # 先頭で I wish を探す
    print(m)  # ['I wish']

    pattern = 'fish$'  # 末尾の fish
    m = re.findall(pattern, source)  # 末尾で fish を探す
    print(m)  # []

    pattern = r'fish tonight\.$'  # 末尾の fish tonight.
    m = re.findall(pattern, source)  # 末尾で fish tonight. を探す
    print(m)  # ['fish tonight.']

    pattern = '[wf]ish'  # w か f のあとに ish が続く
    m = re.findall(pattern, source)  # wish か fish を探す
    print(m)  # ['wish', 'wish', 'fish']

    pattern = '[wsh]+'  # w, s, h のどれかが１個以上続く
    m = re.findall(pattern, source)  # w, s, h で構成される一文字以上を探す
    print(m)  # ['w', 'sh', 'w', 'sh', 'h', 'sh', 'sh', 'h']

    pattern = r'ght\W'  # ght の後に英字以外が続く
    m = re.findall(pattern, source)  # ghtの後ろが英字以外の部分を探す
    print(m)  # ['ght\n', 'ght.']

    pattern = 'I (?=wish)'  # 'I '(Iとスペース)の後ろに wish が続く
    m = re.findall(pattern, source)  # wish につながる 'I ' を探す
    print(m)  # ['I ', 'I ']

    pattern = '(?<=I) wish'  # ' wish'(スペースと wish)の前に I がある
    m = re.findall(pattern, source)  # I から始まる ' wish' を探す
    print(m)  # [' wish', ' wish']


# パターン : マッチした文字列の出力の指定
def find_groups():
    import re
    source = '''I wish I may, I wish I might
                Have a dish of fish tonight.'''
    pattern = r'(. dish\b).*(\bfish)'  # '任意の一文字 dish' で始まり fish で終わる箇所
    m = re.search(pattern, source)
    print(m.group())   # 全てのマッチを取り出せる
    print(m.groups())  # パターンの () で囲んだ箇所にマッチした文字列をタプルで返す

    pattern = r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)'
    m = re.search(pattern, source)  # ?P<name>expr: exprにマッチした部分はnameグループに保存
    print(m.group())        # 'a dish of fish'
    print(m.groups())       # ('a dish', 'fish')
    print(m.group('DISH'))  # 'a dish'(DISH グループ)
    print(m.group('FISH'))  # 'fish'(FISH グループ)


basic_match()
match()
search()
findall()
split()
sub()
find_printable_escape()
find_source_meta()
find_groups()
