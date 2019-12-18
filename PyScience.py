#!/user/bin/python

#
# 標準ライブラリでの数学と統計
#


# math 関数
def py_math():
    import math

    print(math.pi)  # pi
    print(math.e)   # e

    print(math.fabs(98.6))      # 引数の絶対値を返す(98.6)
    print(math.fabs(-271.1))    # 271.1

    print(math.floor(98.6))     # 引数以下でもっとも大きい整数を返す(98)
    print(math.floor(-271.1))   # -272
    print(math.ceil(98.6))      # 引数以上でもっとも小さい整数を返す(99)
    print(math.ceil(-271.1))    # -271

    print(math.factorial(0))    # 階乗(n!)を計算する(1)
    print(math.factorial(1))    # 1
    print(math.factorial(2))    # 2
    print(math.factorial(3))    # 6
    print(math.factorial(10))   # 3628800

    print(math.log(1.0))        # eを底とする引数の対数を計算する(0.0)
    print(math.log(math.e))     # 1.0
    print(math.log(8, 2))       # 別の底を使いたい場合は第２引数として指定(3.0)

    print(math.pow(2, 3))       # 第1引数の第2引数乗を計算する(8.0)
    print(2**3)     # 指数演算子(**)は基数と指数がともに整数なら結果をflootに自動変換しない(8)
    print(2.0**3)               # 8.0

    print(math.sqrt(100.0))         # 平方根を計算する(10.0)

    print(math.hypot(3.0, 4.0))     # ユークリッド距離を計算する(5.0)

    print(math.radians(180.0))      # 弧度法と度数法の相互変換(pie)
    print(math.degrees(math.pi))    # 180.0


# 複素数の操作
def complex_number():
    print(5)                    # 実数
    print(8j)                   # 虚数
    print(3 + 2j)               # 虚数(3+2j)

    print(1j * 1j)              # (-1+0j)
    print((7 + 1j) * 1j)        # (-1+7j)


# decimal による正確な浮動小数点数計算
def tax_calc():  # ドルとセントの正確な計算
    from decimal import Decimal

    price = Decimal('19.99')
    tax = Decimal('0.06')
    total = price + (price * tax)  # 値段と税の正確な算出
    print(total)  # Decimal('21.1894')

    penny = Decimal('0.01')
    print(total.quantize(penny))  # 端数の丸め計算(Decimal('21.19'))


# fracitions による有理数計算
def py_fractions():
    import fractions
    from fractions import Fraction
    from decimal import Decimal

    print(Fraction(1, 3) * Fraction(2, 3))  # 1/3 * 2/3 (2/9)
    Fraction(Decimal('1.0')/Decimal('3.0'))  # Decimalを使うと小数点以下を正確に表現できる
    fractions.gcd(24, 16)  # ２つの数値の最大公約数を計算(8)


# array によるパッキングされたシーケンス
def py_array():
    from array import array
    ary = array('u', 'abcde')  # unicode文字列のarray配列を作る
    print(ary[0], ary[1], ary[2])


# その他
other_sci_mod = {
    'statistics': '平均や中央値など統計のための計算モジュール',
    '@': 'Python 3.5 以降行列の乗算のための演算子として使われる',
}


#
# Scientific Python
#
scientific_python = {  # サードパーティの科学、数学用Pythonパッケージ
    'Anaconda': 'フリーで範囲の広いデータサイエンス用ディストリビューション',
    'Enthought Canopy': 'フリーバージョンと商用バージョンがある',
    'Python(x,y)': 'Windows専用リリース',
    'Pyzo': 'Anacondaに含まれるツールに他のツールをくわえたもの',
    'ALGORETE Loopy': 'これもAnacondaを基礎として他のツールを追加している',
    }


def math_function():
    py_math()
    complex_number()
    tax_calc()
    py_fractions()
    py_array()


#
# NumPy : 高速な多次元数値配列
#


# array() による配列の作成
def array_numpy():
    import numpy as np
    b = np.array([2, 4, 6, 8])

    print(b.ndim)   # 配列の階数(次元数)(1)
    print(b.size)   # 配列内の値の総数(4)
    print(b.shape)  # 各階の値の数(4,)


# arange() による配列の作成
def arange_numpy():
    import numpy as np
    a = np.arange(10)  # 引数numを与えて0からnum-1までのarray配列を作成
    print(a)  # ndarray([0 1 2 3 4 5 6 7 8 9])
    print(a.ndim, a.shape, a.size)  # 1, (10,), 10

    a = np.arange(7, 11)  # 最初の値から第２の値-1までの配列が作られる
    print(a)  # ndarray([7 8 9 10])
    a = np.arange(7, 11, 2)  # 第3引数として１以外のステップ数を指定できる
    print(a)  # ndarray([7 9])
    f = np.arange(2.0, 9.8, 0.3)  # floatの配列
    print(f)  # ndarray([2.  2.3 2.6 2.9 ... 9.8])
    g = np.arange(10, 4, -1.5, dtype=np.float)  # dtype引数で生成するデータ型を指定できる
    print(g)  # ndarray([10.  8.5 7.  5.5])


# zoros(), ones(), random() による配列の作成
def init_array_numpy():
    import numpy as np

    a = np.zeros((3,))  # 要素を0で初期化する１次元配列を作成
    print(a)  # ndarray([0.  0.  0. ])
    print(a.ndim, a.shape, a.size)  # 1, (3,), 3
    b = np.zeros((2, 4))  # 階数が２
    print(b)  # ndarray([[0.  0.  0.  0. ] [0.  0.  0.  0. ]])
    print(b.ndim, b.shape, b.size)  # 2, (2, 4), 8
    k = np.ones((3, 5))  # 要素を１で初期化する３次元配列の作成
    print(k)  # ndarray [[1.  1.  1.  1. ] [1.  1.  1.  1. ] [1.  1.  1.  1. ]]
    m = np.random.random((3, 5))  # 0.0から1.0までの無作為な値を使って配列を生成
    print(m)


# reshape() による配列形状の変更
def reshape_numpy():
    import numpy as np

    a = np.arange(10)
    print(a)  # ndarray([0 1 2 3 4 5 6 7 8 9])
    a = a.reshape(2, 5)  # 階数２,要素数5の配列に変更
    print(a)  # ndarray([[0 1 2 3 4] [5 6 7 8 9]])
    print(a.ndim, a.shape, a.size)  # 2, (2, 5), 10
    a = a.reshape(5, 2)  # 階数５,要素数2の配列に変更
    print(a)  # ndarray([[0 1] [2 3] [4 5] [6 7] [8 9]])
    print(a.ndim, a.shape, a.size)  # 2, (5, 2), 10
    a.shape = (2, 5)  # shapeにタプルを代入する方法でも同じ結果が得られる
    print(a)  # ndarray([[0 1 2 3 4] [5 6 7 8 9]])


# [] による要素の取得
def array_acsses_numpy():
    import numpy as np

    a = np.arange(10)
    print(a[7])         # １次元配列はリストと同じように動作する(7)
    print(a[-1])        # 9

    a.shape = (2, 5)
    print(a)            # ndarray([[0 1 2 3 4] [5 6 7 8 9]])
    print(a[1, 2])      # 多階層の配列のアクセスにはカンマ区切りを使う(7)
    ls = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
    print(ls[1][2])     # Pythonの２次元配列リストとは異なる(7)
    print(a[0, 2:])     # スライスを使える(ndarray([2 3 4]))
    print(a[-1, :3])    # ndarray([5 6 7])
    a[:, 2:4] = 1000    # ndarray([[0 1 1000 1000 4] [5 6 1000 1000 9]])
    print(a)


# 配列の数学演算
def array_calc_numpy():
    import numpy as np

    a = np.arange(4)
    print(a)    # ndarray([0 1 2 3])
    a *= 3      # 配列の要素全てに３を乗算
    print(a)    # ndarray([0 3 6 9])

    a = np.zeros((2, 5)) + 17.0  # 配列の要素を17.0で初期化
    print(a)  # ndarray [[17.  17.  17.  17.  17. ] [17.  17.  17.  17.  17. ]]


# 線形代数
def liner_algebra_numpy():
    import numpy as np

    # 連立一次方程式の解
    # 4x + 5y = 20　
    # x + 2y = 13
    coefficients = np.array([[4, 5], [1, 2]])   # 係数(xとyに掛けられている値)
    dependents = np.array([20, 13])             # 従属変数(方程式の右辺)
    answers = np.linalg.solve(coefficients, dependents)  # 連立方程式の解決
    print(answers)  # ndarray([-8.33333333 10.66666667])

    # 解は正しいか
    print(4 * answers[0] + 5 * answers[1])      # 20.0
    print(1 * answers[0] + 2 * answers[1])      # 13.0
    product = np.dot(coefficients, answers)     # 配列のドット積を計算
    print(product)                              # ndarray([20.  13. ])
    print(np.allclose(product, dependents))     # ２つの配列はほぼ等しいか(True)


def numpy_mod():
    array_numpy()
    arange_numpy()
    init_array_numpy()
    reshape_numpy()
    array_acsses_numpy()
    array_calc_numpy()
    liner_algebra_numpy()


#
# SciPy ライブラリ
#
SciPy = {'SciPy': 'NumPyを基礎としたさらに多くの数学、統計関数のライブラリ'}


#
# SciKit ライブラリ
#
SciKit = {'SciKit': 'SciPyを基礎とする科学パッケージのグループ、専門分野は機械学習'}


#
# IPython ライブラリ
#
IPython = {'IPython': 'Pythonの改良されたリアクティブな対話型インタプリタ'}


#
# Pandas
#
Pandas = {'Pandas': '対話的データ分析のためのパッケージ'}


#
# Python と科学分野
#


# 全般
py_comp_sci = {
    ('科学技術分野におけるPythonを使った計算', 'http://bit.ly/py-comp-sci'),
    ('科学者のためのPython集中コース', 'http://bit.ly/pyforsci'),
    }


# 物理学
py_comp_phys = {
    ('コンピュータ物理学', 'http://bit.ly/comp-phys-py'),
    }


# 生物学、医学
py_comp_bio = {
    ('生物学者のためのPython', 'http://pythonforbiologists.com'),
    ('Pythonによる神経画像', 'http://nipy.org'),
}


if __name__ == '__main__':
    math_function()
    numpy_mod()
