#!/usr/bin/python

#
# モジュールと import 文
#


# モジュールのインポート
def import_module():
    import mod_report       # mod_report.py をインポート
    description = mod_report.get_description()  # mod_report の get_description
    print("Today's weather:", description)


# 別名によるインポート
def import_as():
    import mod_report as wr     # mod_report を wr の別名でインポート
    description = wr.get_description()
    print("Today's weather:", description)


# 必要なものだけをインポート
def from_import():
    from mod_report import get_description  # get_description のみインポート
    description = get_description()
    print("Today's weather:", description)


# 必要なものだけを別名でインポート
def from_import_as():
    from mod_report import get_description as do_it  # get_description を do_it
    description = do_it()
    print("Today's weather:", description)


import_module()
import_as()
from_import()
from_import_as()


# モジュールサーチパス
def module_search_pass():
    import sys
    for place in sys.path:  # sys.path 変数にはモジュールを探すパスが定義（書き換え可能）
        print(place)        # 最初にマッチしたファイルが優先的に使われる


module_search_pass()


#
# パッケージ
#

# packages ディレクトリをパッケージとして扱う
def weather():
    from packages import daily, weekly  # packages パッケージの daily, weekly
    print("Daily forecast:", daily.forecast())
    print("Weekly forecast:")
    for number, outlook in enumerate(weekly.forecast(), 1):  # 各要素に番号を追加
        print(number, outlook)


weather()


#
# Python 標準ライブラリ
#

# setdefault() と defaultdict() による存在しないキーの処理
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)

print(periodic_table.setdefault('carbon', 12))  # キーがなければ追加し、対応する値を返す
print(periodic_table)

print(periodic_table.setdefault('Helium', 947))  # キーがあると元の値が返され変更されず
print(periodic_table)


def default_dict():
    from collections import defaultdict
    periodic_table = defaultdict(int)   # 辞書の値にデフォルト値を設定する(int の 0)
    periodic_table['Hydrogen'] = 1
    print(periodic_table['Lead'])   # Lead は存在しないがデフォルト値で追加される
    print(periodic_table)


def default_dict_func():
    from collections import defaultdict

    def no_idea():
        return 'Huh?'

    bestiary = defaultdict(no_idea)  # デフォルト値の設定に no_idea を呼び出す
    bestiary['A'] = 'Abominable Snowman'
    bestiary['B'] = 'Basilisk'
    print(bestiary['A'], bestiary['B'], bestiary['C'])  # C はない(Huh?)


def default_dict_lambda():
    from collections import defaultdict
    beatiary = defaultdict(lambda: 'Huh?')  # ラムダでデフォルト値を渡す
    print(beatiary['E'])    # E はない(Huh?)


def default_dict_counter():
    from collections import defaultdict
    food_counter = defaultdict(int)
    for food in ['spam', 'spam', 'eggs', 'spam']:
        food_counter[food] += 1     # 出現数を数える独自のカウンタ

    for food, count in food_counter.items():
        print(food, count)


default_dict()
default_dict_func()
default_dict_lambda()
default_dict_counter()


# Counter() による要素数の計算
def counter():
    from collections import Counter
    breakfast = ['spam', 'spam', 'eggs', 'spam']
    breakfast_counter = Counter(breakfast)      # Counter オブジェクトを作成
    print(breakfast_counter)

    print(breakfast_counter.most_common())      # 全ての要素を降順で返す
    print(breakfast_counter.most_common(1))     # 引数として指定した分だけ表示する

    lunch = ['eggs', 'eggs', 'bacon']
    lunch_counter = Counter(lunch)

    print(breakfast_counter + lunch_counter)    # ２つのカウンタの結合
    print(breakfast_counter - lunch_counter)    # 片方から片方を引く
    print(lunch_counter - breakfast_counter)    # 上とは結果が異なる
    print(breakfast_counter & lunch_counter)    # 積集合(共通する eggs は1つ)
    print(breakfast_counter | lunch_counter)    # 和集合(eggs 大きい方の２)


counter()


# OrderedDict() によるキー順のソート
def ordered_dict():
    from collections import OrderedDict
    quotes = OrderedDict([  # OrderedDict はキーが追加された順番を覚えている
        ('Moe', 'A wise guy, huh?'),
        ('Larry', 'Ow!'),
        ('Curly', 'Nyuk nyuk!'),
    ])

    for stooges in quotes:
        print(stooges)      # 追加された順に表示される


ordered_dict()


# スタック + キュー = デック
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():    # 単語が回分かを調べる
            return False
    return True


print(palindrome('a'))              # True
print(palindrome('racecar'))        # True
print(palindrome(''))               # True
print(palindrome('radar'))          # True
print(palindrome('halibut'))        # False


# itertools によるコード構造の反復処理
def iter_chain():
    import itertools
    for item in itertools.chain([1, 2], ['a', 'b']):  # 引数の要素を順次反復処理する
        print(item)


def iter_cycle():
    import itertools
    for item, count in zip(itertools.cycle([1, 2]), range(0, 10)):  # 無限反復
        print(count, item)


def iter_accumlate():
    import itertools
    for item in itertools.accumulate([1, 2, 3, 4]):  # 要素をまとめた値を計算(標準は和)
        print(item)


def iter_accumlate_func():
    import itertools

    def multiply(a, b):
        return a * b

    for item in itertools.accumulate([1, 2, 3, 4], multiply):  # 式に関数を使える
        print(item)


iter_chain()
iter_cycle()
iter_accumlate()
iter_accumlate_func()


# pprint() によるきれいな表示
def p_print():
    from collections import OrderedDict
    from pprint import pprint
    quotes = OrderedDict([
        ('Noe', 'A wise guy, huh?'),
        ('Larry', 'Ow!'),
        ('Curly', 'Nyuk nyuk!'),
    ])

    print(quotes)
    pprint(quotes)  # 要素の位置を揃えて読みやすくする


p_print()
