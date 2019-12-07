#!/user/bin/python

# コメントは # を使う

# \ による行の継続
alphabet = 'abcdefg' + \
    'hijklmnop' + \
    'qrstuv' + \
    'wxyz'
print(alphabet)

#
# if, elif, else による比較
#

disaster = True
if disaster:
    print("Woe!")               # True なので Woe! と表示
else:
    print("Whee!")

funny, small = True, True
if funny:
    if small:
        print("It's a cat.")    # funny かつ small なので　It's a cat
    else:
        print("It's a bear!")
else:
    if small:
        print("It's a skink!")
    else:
        print("It's a human. Or a hairless bear.")

color = "puce"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)   # puce はどれも当てはまらない

# 比較演算子
#
# 等しい          ==
# 等しくない       ！＝
# より小さい       <
# 以下           <=
# より大きい       >
# 以上           >=
# 要素になっている  in
#
x = 7
print(x == 5)               # False
print(x == 7)               # True
print(5 < x)                # True
print(x < 10)               # True

# ブール演算子
#
# かつ           and
# もしくは         or
# ではない        not
#
print(5 < x and x < 10)         # True
print((5 < x) and (x < 10))     # ()で優先順位を明確化する(True)
print(5 < x or x < 10)          # True
print(5 < x and x > 10)         # False
print(5 < x and not x > 10)     # True
print(5 < x < 10)               # and の省略(True)
print(5 < x < 10 < 999)         # 省略形の長い比較(True)

# True と False

# False と見なされるもの
#
# ブール値        False
# null          None
# 整数のゼロ      0
# floatのゼロ    0.0
# 空文字列       ''
# 空リスト        []
# 空タプル       ()
# 空辞書        {}
# 空集合        set()
#
some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")           # 空リスト(False)なのでこれを表示

#
# while による反復処理
#

count = 1
while count <= 5:       # 比較式が True の間ループする
    print(count)
    count += 1

# break によるループ中止
count = 1
while True:             # 無限ループ
    if count > 5:       # 5 より大きくなるとループを抜ける
        break
    print(count)
    count += 1

# continue による次のイテレーションの開始
count = 1
while count <= 10:
    if count % 2 == 0:  # 偶数なら表示せず次のループへ
        count += 1
        continue
    print(count)
    count += 1

# else による break のチェック
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    num = numbers[position]
    if num % 2 == 0:             # 偶数が見つかればループを抜ける
        print('Found even number', num)
        break
    position += 1
else:                               # break が呼び出されなかった場合この節を実行
    print('No even number found')

#
# for による反復処理
#

rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
for rabbit in rabbits:              # for によるリストのイテレーション
    print(rabbit)

word = 'cat'
for letter in word:                 # 文字列の場合は一文字ずつイテレーションする
    print(letter)

accusation = {
        'room': 'ballroom',
        'weapon': 'lead pipe',
        'person': 'Col.Mustard',
        }
for card in accusation:             # 辞書の場合はキーを返す
    print(card)

for value in accusation.values():   # 値を処理したい場合は values 関数を使う
    print(value)

for item in accusation.items():     # キーと値の両方をタプルで返す場合は items 関数
    print(item)
for card, contents in accusation.items():   # タプルの一括代入
    print('Card', card, 'has the contents', contents)

# ※ break, continue, else　による break チェックは while 文と同様

# zip() を使った複数シーケンスの反復処理
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'crange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tirmisu', 'ice cream', 'pie', 'pudding']   # プリンはペアに出来る要素がない
for day, fruit, drink, dessert in \
        zip(days, fruits, drinks, desserts):    # オフセットが共通の要素をタプルに出来る
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(list(zip(english, french)))               # タプルのリストになる
print(dict(zip(english, french)))               # 辞書になる

# range() による数値シーケンスの生成
for x in range(0, 3):           # 0~3 の範囲を生成
    print(x)
print(list(range(0, 3)))        # 0~3 の範囲をリストに
for x in range(2, -1, -1):      # 2~0 の範囲を作成
    print(x)
print(list(range(2, -1, -1)))   # 2~0 の範囲をリストに
list(range(0, 11, 2))           # 2ずつのステップで 0~10 の偶数の範囲をリストに

#
# 内包表記
#

# リスト内包表記
number_list = [number for number in range(1, 6)]    # 1~5 の範囲のリストを作成
print(number_list)
number_list = [number-1 for number in range(1, 6)]  # 式に基づいて 0~4 の範囲になる
print(number_list)

a_list = [number for number in range(1, 6) if number % 2 == 1]  # 奇数のみ
print(a_list)

rows, cols = range(1, 4), range(1, 3)
cells = [(row, col) for row in rows for col in cols]    # for のネスト
for cell in cells:
    print(cell)
for row, col in cells:      # タプルのアンパック
    print(row, col)

# 辞書包括表記
word = 'letters'
letter_counts = \
    {letter: word.count(letter) for letter in word}     # 文字の出現数の辞書を作成
print(letter_counts)

letter_counts = \
    {letter: word.count(letter) for letter in set(word)}    # set で重複を削除
print(letter_counts)

# 集合内包表記
a_set = {number for number in range(1, 6) if number % 3 == 1}   # 3ずつの集合
print(a_set)

# ジェネレータ内包表記
number_thing = (number for number in range(1, 6))       # ジェネレータオブジェクトを返す
for number in number_thing:
    print(number)

number_list = list((number for number in range(1, 6)))  # リスト内包表記のように動作
print(number_list)

try_again = list(number_thing)          # ジェネレータは一度しか使えない
print(try_again)                        # 空になっている

#
# 例外処理
#

short_list = [1, 2, 3]
position = 5
try:                            # 例外をキャッチする
    short_list[position]        # リストの範囲より大きい位置を参照しているため例外発生
except IndexError as err:       # キャッチする例外の種類を指定 err に格納する
    print('Need a position between 0 and',
          len(short_list)-1, 'but got', position)  # IndexError なので表示される
except Exception as other:      # その他のあらゆる例外(Ｅｘｃｅｐｔｉｏｎ)をキャッチする
    print('Something else broke:', other)


# 独自例外の作成
class UppercaseException(Exception):    # Exception を継承した独自例外を定義
    pass


words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        try:
            raise UppercaseException(word)  # 大文字の単語が含まれていたら例外を投げる
        except UppercaseException as err:
            print('Uppercase:', err)
