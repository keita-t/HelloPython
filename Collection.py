#!/user/bin/python

#
# リスト
#

empty_list = []     # 空のリストを作成
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
print(empty_list, weekdays, big_birds, first_names)

another_empty_list = list()     # 空のリストを作成
print(another_empty_list)

# list() による他のデータ型からリストへの変換
print(list('cat'))                          # 文字列を一文字ごとにリストに
print(list(('ready', 'fire', 'aim')))       # タプルをリストに
print('1/6/1952'.split('/'))                # 文字列を分割してリストに
print('a/b//c/d//e'.split('/'))             # セパレータが連続していると空文字が入る
print('a/b//c/d//e'.split('//'))            # この場合は // がセパレータ

# リストの操作 #
marxes = ['Groucho', 'Chico', 'Harpo']

# [offset] を使った要素の取り出しと書き換え
print(marxes[0], marxes[1], marxes[2])
print(marxes[-1], marxes[-2], marxes[-3])   # 末尾から逆に

marxes[2] = 'Wanda'     # Harpo を Wanda に書き換え
print(marxes)

# スライスによるサブシーケンスの取り出し
print(marxes[0:2])      # 先頭から marxes[1] の要素まで取り出す
print(marxes[::2])      # ステップによる一つおき
print(marxes[::-2])     # ステップによる一つおき逆順
print(marxes[::-1])     # リストが逆順になる

# リストの末尾への要素の追加
marxes.append('Zeppo')          # 末尾に Zeppo を追加
print(marxes)

# リストの結合
others = ['Gummo', 'Karl']

marxes.extend(others)           # marxes に others の要素を追加
print(marxes)                   # marxes += others ... += でも同じようにできる

marxes = ['Groucho', 'Chico', 'Harpo']

# 指定した位置への挿入
marxes.insert(3, 'Gummo')       # marxes[3] に Gummo を挿入
print(marxes)
marxes.insert(10, 'Karl')       # 指定したオフセットがリストより大きい場合は末尾に挿入
print(marxes)

# 指定した要素の削除
del marxes[-1]                  # Karl を削除
print(marxes)
marxes.remove('Gummo')          # 値を指定して要素（Gummo）を削除
print(marxes)

# 要素のポップ
print(marxes.pop())             # Harpo を取り出してリストから削除
print(marxes)
print(marxes.pop(1))            # marxes[1](Chico)をを取り出してリストから削除
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']

# 要素のオフセットを調べる
print(marxes.index('Chico'))    # Chico のインデックス(1)

# 要素の有無を調べる
print('Groucho' in marxes)      # marxes リストに Grouch はあるので True
print('Bob' in marxes)          # marxes リストに Bob はないので False

# 要素の個数の計算
print(marxes.count('Harpo'))    # Harpo の個数(1)
print(marxes.count('Bob'))      # Bob の個数(0)

snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger'))  # cheeseburger の個数(3)

# 文字列への変換
print(', '.join(marxes))        # marxes リストを ', ' で結合して文字列に

# 要素の並び替え
sorted_marxes = sorted(marxes)  # 昇順に並び替え sorted はリストのコピーを返す
print(marxes, sorted_marxes)
marxes.sort()                   # sort はリスト自体をソートする
print(marxes)
marxes.sort(reverse=True)       # reverse=True 引数で降順ソート
print(marxes)

# 長さの取得
print(len(marxes))              # marxes リストの要素数(4)

# 代入とコピー
a = [1, 2, 3]
b = a                           # b に a のリストを代入（参照渡し）
a[0] = 'surprise'               # 参照なので a を変えると b も変わる
print(a, b)

a = [1, 2, 3]
b = a.copy()                    # a を b にコピー（値渡し）
c = list(a)                     # list 関数も値渡し
d = a[:]                        # スライスも値渡し
a[0] = 'surprise'               # a を変えても他に影響はない
print(a, b, c, d)

#
# タプル ... イミュータブル（上書き不可）な要素のシーケンス
#

empty_tuple = ()                # 空のタプルを作成
print(empty_tuple)
one_marx = 'Groucho',           # 要素が一つの場合は末尾にカンマをつけて作る
print(one_marx)
marx_tuple = 'Groucho', 'Chico', 'Harpo'    # 複数要素のタプル
print(marx_tuple)
marx_tuple = ('Groucho', 'Chico', 'Harpo')  # ()を付けるとタプルとわかりやすい
print(marx_tuple)

# タプルのアンパック ... 複数の変数を一度に代入
a, b, c = marx_tuple            # a, b, c にタプルの要素を代入
print(a, b, c)
a, b, c = c, b, a               # 一文で値を交換できる
print(a, b, c)

marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))         # 変換関数でタプルを作れる

#
# 辞書
#

empty_dict = {}     # 空の辞書を作成
print(empty_dict)

bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never sisses",
    }
print(bierce)

# 辞書への変換
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]      # 2要素のリストのリスト
lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]      # 2要素のタプルのリスト
tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])      # 2要素のリストのタプル
los = ['ab', 'cd', 'ef']                        # 2文字の文字列のリスト
tos = ('ab', 'cd', 'ef')                        # 2文字の文字列のタプル
print(dict(lol), dict(lot), dict(tol), dict(los), dict(tos))  # 辞書に変換

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Falin': 'Michael',
    }
print(pythons)                  # メンバーが一人足りない辞書

# [key]による要素の追加と変更
pythons['Gilliam'] = 'Gerry'    # 名前を間違えて辞書に追加
print(pythons)
pythons['Gilliam'] = 'Terry'    # キー Gilliam を使って正しい名前に置き換え
print(pythons)                  # キーは一意である必要がある

# 辞書の結合
others = {'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)          # pythons に others を結合
print(pythons)                  # others はモンティパイソンのメンバーではない

# キーによる要素の削除
del pythons['Marx']             # Marx キーの要素を削除
del pythons['Howard']           # Howard キーの要素を削除
print(pythons)                  # 正しいモンティパイソンのメンバー辞書

# キーの有無のテスト
print('Chapman' in pythons)     # Chapman キーは pythons にあるか（True）
print('Falin' in pythons)       # Falin キーは pythons にあるか(True)
print('Marx' in pythons)        # Marx キーは pythons にあるか(False)

# [key]による要素の取得
print(pythons['Cleese'])                    # Cleese キーの要素を取得
# print(pythons['Marx'])                    # キーがない場合は例外が発生
print(pythons.get('Cleese'))                # get関数でキーを指定できる
print(pythons.get('Marx', 'Not a Python'))  # 無い場合は指定したオプション値を返す
print(pythons.get('Marx'))                  # 指定がない場合は None

signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': 'smile for the camera',
    }

# 全てのキーの取得
print(signals.keys())           # dict_keys オブジェクトを返す
print(list(signals.keys()))     # リストに変換

# 全ての値の取得
print(signals.values())         # dict_alues オブジェクトを返す
print(list(signals.values()))   # リストに変換

# 全てのキー/値のペアを取得
print(signals.items())          # dict_items オブジェクトを返す
print(list(signals.items()))    # リストに変換（タプルのリスト）

# 代入とコピー
save_signals = signals          # save_signals に signals を代入（参照渡し）
signals['blue'] = 'confuse everyone'    # blueキーと値を追加
print(save_signals)                     # 参照なので save_signals も変わる

copy_signals = signals.copy()   # copy_signals に signals をコピー（値渡し）
del signals['blue']             # blue キーの値を削除
print(signals, copy_signals)    # コピーした辞書に影響はない

# 全ての要素の削除
signals.clear()
print(signals)

#
# 集合
#

empty_set = set()   # 空の集合を作成
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}      # 偶数の集合
print(even_numbers)
odd_numbers = {1, 3, 5, 7, 9}       # 奇数の集合
print(odd_numbers)

# set()による他のデータ型からの集合への変換
print(set('letters'))               # 文字列から集合（重複は取り除かれる）
print(set(['Dasher', 'Dancer', 'Francer', 'Mason-Dixon']))          # リストから集合
print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))            # タプルから集合
print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))   # 辞書から集合

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
    }

# 値の有無のテスト
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)                     # drinks から集合内に vodka のあるものを表示

for name, contents in drinks.items():
    if 'vodka' in contents \
            and not ('vermouth' in contents or 'cream' in contents):
        print(name)                     # vermouth と cream は除外して表示

# 組み合わせと演算
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)                     # $ は集合と集合の積集合の結果の集合を返す

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)                     # 積集合を利用した　vermouth と cream の除外

bruss = drinks['black russian']
wruss = drinks['white russian']

print(bruss & wruss)                # 積集合（両方の集合に共通する要素の集合）
print(bruss.intersection(wruss))    # intersection関数は & と同じ

print(bruss | wruss)                # 和集合（どちらかの集合に含まれている要素の集合）
print(bruss.union(wruss))           # union関数は | と同じ

print(bruss - wruss)                # 差集合（第1の集合には含まれ、第2の集合には含まれない）
print(bruss.difference(wruss))      # difference関数は - と同じ
print(wruss - bruss)                # この場合 cream が残る

print(bruss ^ wruss)                # 排他的論理和(片方に含まれるが両方には含まれない)
print(bruss.symmetric_difference(wruss))    # symmetric_difference関数は ^ と同じ

print(bruss <= wruss)           # 部分集合（片方の集合がもう片方の集合の部分集合）(True)
print(bruss.issubset(wruss))    # issubset関数は <= と同じ

print(bruss < wruss)    # 真部分集合（第2集合が第1集合の全ての要素に加え別の要素を持つ）（True）

print(wruss >= bruss)   # 上位集合（第２集合の全ての要素が第１集合の要素にもないっている）（True）
print(wruss.issuperset(bruss))  # issuperset関数は >= と同じ

print(wruss > bruss)    # 真上位集合（第1集合が第2集合の全ての要素に加え別の要素を持つ）（Ｔｒｕｅ）
