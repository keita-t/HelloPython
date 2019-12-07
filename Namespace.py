#!/usr/bin/python

#
# 名前空間とスコープ
#

animal = 'fruitbat'                         # グローバル変数


def print_global():
    print('inside print_global:', animal)   # グローバル変数は関数内から参照できる


print('at the top level:', animal)          # animal を参照
print_global()                              # 関数内で animal を参照


def change_local():             # ローカルの animal 変数を変更する
    animal = 'wombat'           # ローカル変数
    print('inside change_local:', animal, id(animal))


change_local()                  # ローカルの animal を表示
print(animal, id(animal))       # グローバルの animal を表示


def change_and_print_global():
    global animal               # 関数内のスコープでグローバル変数へのアクセスを明示する
    animal = 'wombat'           # グローバルの animal が変更される
    print('inside change_and_print_global:', animal)


print(animal)                   # グローバルの animal は fruitbat
change_and_print_global()       # グローバルの animal を wombat に変更
print(animal)                   # グローバルの animal は wombat


# 名前空間へのアクセス
animal = 'fruitbat'             # グローバル変数


def change_local():
    animal = 'wombat'           # ローカル変数
    print('locals:', locals())  # locals() はローカル名前空間の内容の辞書を表示


print(animal)                   # グローバルの animal は fruitbat
change_local()                  # ローカルの animal は wombat （辞書）
print('globals:', str(globals()).replace(',', ',\n'))  # グローバル名前空間の内容(辞書)


# 名前のなかの_と__
def amazing():                  # 先頭と末尾が__の変数はシステム変数
    '''これは素晴らしい関数だ。
    もう一度見る？'''
    print('この関数の名前:', amazing.__name__)     # __name__ は関数の名前
    print('docstring:', amazing.__doc__)        # __doc__ は docstring


amazing()
