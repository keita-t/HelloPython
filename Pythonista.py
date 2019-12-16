#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import doctest


#
# IDE (総合開発環境)
#
IDE = {
    'IDLE': 'http://bit.ly/py-idle',
    'PyCharm': 'http://www.jetbrains.com/pycharm/',
    'IPython': 'http://ipython.org',
}


#
# テスト
#


# unittest
def just_do_it(text):  # テストするサンプルコード
    # "<text>に含まれているすべての単語をタイトルケースに"
    from string import capwords
    return capwords(text)


class TestCap(unittest.TestCase):  # just_do_it をテストする

    def setUp(self):  # テストメソッドの前に実行される
        pass

    def tearDown(self):  # テストメソッドの後に実行される
        pass

    def test_one_word(self):
        text = 'duck'
        result = just_do_it(text)
        self.assertEqual(result, 'Duck')  # duck は Duck になっているか

    def test_multiple_words(self):
        text = 'a veritable flock of ducks'
        result = just_do_it(text)
        self.assertEqual(result, 'A Veritable Flock Of Ducks')  # 単語の先頭は大文字

    def test_words_with_apostrophes(self):
        text = "I'm fresh out of ideas"
        result = just_do_it(text)
        self.assertEqual(result, "I'm Fresh Out Of Ideas")  # ' は正しく処理できるか


# doctest
def just_doc_it(text):  # dockstring の中にテストを書ける(>>>の後ろに呼び出し、次の行に結果)
    """
    >>> just_doc_it('duck')
    'Duck'
    >>> just_doc_it('a veritable flock of ducks')
    'A Veritable Flock Of Ducks'
    >>> just_doc_it("I'm fresh out of ideas")
    "I'm Fresh Out Of Ideas"
    """
    from string import capwords
    return capwords(text)


# 継続的インテグレーション
CI_tools = {
    'buildbot': 'http://buildbot.net',
    'jenkins': 'http://jenkins-ci.org',
    'travis-ci': 'http://travis-ci.com',
}


#
# Python コードのデバッグ
#


# vars()
def print_vars():
    def func(*args, **kwargs):
        print(vars())  # 関数への引数を含むローカル変数の値を抽出する

    func(1, 2, 3)             # {'kwargs': {}, 'args': (1, 2, 3)}
    func(['a', 'b', 'argh'])  # {'kwargs': {}, 'args': (['a', 'b', 'argh'])}


# デコレータ
def dump_decorator():
    def dump(func):
        "入力引数と出力値を表示する"
        def wrapped(*args, **kwargs):
            print("Function name: %s" % func.__name__)
            print("Input arguments: %s" % ' '.join(map(str, args)))
            print("Input keyword arguments: %s" % kwargs.items())
            output = func(*args, **kwargs)
            print("Output:", output)
            return output
        return wrapped

    @dump  # 関数の詳細をダンプする
    def double(*args, **kwargs):  # 数値の引数を受け取り値を倍にしてリストにまとめて返す
        "Double every argument"
        output_list = [2 * arg for arg in args]
        output_dict = {k: 2 * v for k, v in kwargs.items()}
        return output_list, output_dict

    print(double(3, 5, first=100, next=98.6, last=-40))


#
# pdb によるデバッグ
#
pdb = {'pdb': 'https://docs.python.org/3/library/pdb.html'}


#
# エラーメッセージのロギング
#
def message_logging():
    import logging
    import os

    if os.path.exists('files/blue_ox.log'):
        os.remove('files/blue_ox.log')

    fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'  # ログの書式を設定
    logging.basicConfig(
        level=logging.DEBUG,  # デフォルトレベルをDEBUGに設定(すべてロギング)
        filename='files/blue_ox.log',  # ログのログファイルへの書き込み設定
        format=fmt)  # ロギングされるメッセージのフォーマット設定

    # ランク付けのための優先順位レベル
    logging.debug("Looks like rain")                    # DEBUG
    logging.info("And hail")                            # INFO
    logging.warn("Did I hear thunder?")                 # WARNING(デフォルト)
    logging.error("Was that lightning?")                # ERROR
    logging.critical("Stop fencing and get inside!")    # CRITICAL


#
# コードの最適化
#


# 実行時間の計測
def execute_timer():
    from time import time
    from timeit import timeit, repeat  # コードを実行して実行時間をテストする

    t1 = time()
    num = 5
    num += 2
    print(time() - t1)  # 終了時の計測時から開始時の計測時を引く(アバウトな実行時間)

    print(timeit('num = 5; num *= 2', number=1))
    print(repeat('num = 5; num *= 2', number=1, repeat=3))  # ３回繰り返してテスト


# アルゴリズムとデータ構造
def make_list_test():
    from timeit import timeit

    def make_list_1():  # appendを使ってリストに1000の要素を追加
        result = []
        for value in range(1000):
            result.append(value)
        return result

    def make_list_2():  # リスト内包表記で1000の要素をリスト化(こちらの方がはるかに高速)
        result = [value for value in range(1000)]
        return result

    print('make_list_1 takes', timeit(make_list_1, number=1000), 'seconds')
    print('make_list_2 takes', timeit(make_list_2, number=1000), 'seconds')


# Cython, NumPy, Cエクステンション (パフォーマンスの為のC言語)
C_bind = {
    'Cython': 'アノテーションを付けたものをコンパイルされたCコードに変換',
    'NumPy': 'Python数学ライブラリ',
    }

# PyPy : 高速なPythonインタプリタ
PyPy = {'PyPy': 'http://pypy.org'}


#
# ソース管理
#
version_ctrl_system = {
    'Mercurial': 'http://mercurial.selenic.com',
    'Git': 'http://git-scm.com/',
    }

if __name__ == '__main__':
    print_vars()
    dump_decorator()
    message_logging()
    execute_timer()
    make_list_test()

    print('\ndoctest:\n')
    doctest.testmod(verbose=True)
    print('\nunittest:\n')
    unittest.main()
