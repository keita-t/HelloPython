#!/usr/bin/python

#
# Hello World
#

print("hello python!")
print(8 * 9)

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
