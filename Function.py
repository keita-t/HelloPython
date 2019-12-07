#!/usr/bin/python

#
# 関数
#


# 基本的な定義
def do_nothing():       # 何もしない
    pass


do_nothing()            # 定義した関数の呼び出し


def make_a_sound():     # 一個の単語を出力する
    print('quack')


make_a_sound()


def agree():            # True の値を返す
    return True


if agree():
    print('Splendid!')      # agree が True を返すのでこれを表示
else:
    print('That was unexpected.')


def echo(anything):             # anything という一つの引数を取る
    return anything + ' ' + anything


print(echo('Rumplestiltskin'))


def commentary(color):          # color で渡された色に対してコメントを返す
    if color == 'red':
        return "It's a tomato."
    elif color == 'green':
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."


print(commentary('blue'))       # blue は知らない


def is_none(thing):             # None か　True か　False か判断する
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")


is_none(None)                   # None
is_none(True)                   # True
is_none(False)                  # False(None は False 扱いにもなるがあくまで None)


# 位置引数
def menu(wine, entree, dessert):    # 渡された引数の位置に対応する仮引数にコピーされる
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken', 'cake'))


# キーワード引数
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))    # 引数の名前で指定
print(menu('frontenac', dessert='flan', entree='fish'))  # 両方なら先に位置引数を指定


# デフォルト引数
def menu(wine, entree, dessert='pudding'):      # dessert にデフォルトの値を指定
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken'))    # dessert を指定しないとデフォルト値（pudding）
print(menu('dunkelfelder', 'duck', 'doughnut'))     # 指定でその値（doughnut）


def buggy(arg, result=[]):              # デフォルト引数は関数定義時に評価される
    result.append(arg)                  # 可変のデータ型を操作する
    print(result)


buggy('a')
buggy('b')          # 関数の再呼び出し時に result の値が残っている!


# *による位置引数のタプル化
def print_args(*args):      # 可変個の位置引数をタプルにまとめて渡す
    print('Positional argument tuple:', args)


print_args()                            # 空のタプル
print_args(3, 2, 1, 'wait!', 'uh...')   # 可変個の引数をタプルとして渡せる


def print_more(required1, required2, *args):     # 必須の引数がある場合は最後に書く
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)


print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')  # 最初の２つは必須


# **によるキーワード引数の辞書化
def print_kwargs(**kwargs):         # キーワード引数を一つの辞書にまとめて渡す
    print('Keyword arguments:', kwargs)


print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')  # 引数が辞書化


# ※ *args と **kwargs を併用する場合はこの順序で並べる必要がある


# docstring
def echo(anything):
    'echoは、与えられた入力引数を返す'  # 関数本体の先頭に文字列を付けると、関数のドキュメントとなる
    return anything


def print_if_true(thing, check):  # トリプルクォートで書式整形が出来る
    '''
    第２引数が真なら、第１引数を表示する
    処理内容：
        １． ＊第２＊引数が真かどうかをチェックする。
        ２． 真なら＊第１＊引数を表示する
    '''
    if check:
        print(thing)


print(help(echo))       # help 関数で 整形された docstring が返される
print(echo.__doc__)     # 整形前の素のままの docstring が返される


# オブジェクトとしての関数
def answer():               # 42 と答える単純な関数
    print(42)


def run_something(func):
    func()                  # ()を付けて引数を呼び出すことで関数呼び出しとなる


run_something(answer)       # answer 関数を引数として渡して実行
print(type(run_something))  # 関数もオブジェクトとして定義されている


def add_args(arg1, arg2):   # arg1 + arg2 を表示する関数
    print(arg1 + arg2)


def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)        # arg1 と arg2 の引数を func に渡して実行する


run_something_with_args(add_args, 5, 9)     # 5 + 9 = 14


def sum_args(*args):        # 任意個の引数の値の合計を返す関数
    return sum(args)


def run_with_positional_args(func, *args):
    return func(*args)       # *args（タプル）を渡して func を実行


print(run_with_positional_args(sum_args, 1, 2, 3, 4))   # 1 + 2 + 3 + 4 = 10


# 関数内関数
def outer(a, b):
    def inner(c, d):        # outer 関数内で inner 関数を定義
        return c + d
    return inner(a, b)


print(outer(4, 7))          # 4 + 7 = 11


def knights(saying):
    def inner(quote):       # 引数にテキストを追加する関数内関数
        return "We are the kights who say: '%s'" % quote
    return inner(saying)


print(knights('Ni!'))       # ニッ！ のナイト


# 関数内関数を利用した遅延評価（クロージャ)
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2   # saying の値を保持した inner2 関数を生成して返す


a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(a())          # Duck を渡された inner2 を遅延評価
print(b())          # Hasenpfeffer を渡された inner2 を遅延評価


# 無名関数 : ラムダ関数
def edit_story(words, func):    # words で渡された単語のリストに func 関数を適用する
    for word in words:
        print(func(word))


def enliven(word):      # 文の衝撃力を上げる
    return word.capitalize() + '!'


stairs = ['thud', 'meow', 'thud', 'Hiss']
edit_story(stairs, enliven)     # stairs 単語リストに enliven 関数を適用

edit_story(stairs, lambda word: word.capitalize() + '!')  # enliven をラムダにする


# ジェネレータ
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number        # return の代わりに yield でジェネレータとして返す
        number += step


for x in my_range(1, 5):    # ジェネレータオブジェクトをイテレーション
    print(x)


# デコレータ
def document_it(func):  # 関数の情報を表示するデコレータ
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function  # func として渡された関数を遅延評価する new function 関数を返す


def add_ints(a, b):     # a + b を実行する単純な関数
    return a + b


print(document_it(add_ints)(3, 5))     # add_ints を document_it でデコレートして実行


@document_it                    # デコレートしたい関数の直前に @ で書くと同じ動作を得られる
def sub_ints(a, b):             # a - b を実行する単純な関数
    return a - b


print(sub_ints(10, 4))          # デコレートされた結果を実行


def square_it(func):    # 結果を乗算するデコレータ
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function


@document_it
@square_it              # def に近いものから先に実行される（square_it → document_it）
def mul_ints(a, b):
    return a * b


print(mul_ints(3, 5))   # 15 * 15 = 225


@square_it
@document_it            # document_it → square_it の順
def div_ints(a, b):
    return a // b


print(div_ints(8, 4))   # Result: 2 と表示され、結果は 2 * 2 = 4 となる
