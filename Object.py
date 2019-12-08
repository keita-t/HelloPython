#!/usr/bin/python

#
# オブジェクトとクラス
#


# class によるクラスの定義
class Nothing():                # 空のクラス
    pass


someone = Nothing()             # NothingPerson インスタンスの生成


class NothingToInit():          # コンストラクタをもつクラス
    def __init__(self):         # コンストラクタ
        pass


class Person():
    def __init__(self, name):   # コンストラクタで引数 name を受け取る
        self.name = name        # self.name でこのクラスの属性 name に値を設定


hunter = Person('Elmer Fudd')   # Person のインスタンス生成
print(hunter.name)              # 属性 name にアクセス


# 継承
class Car():
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):        # Car クラスを継承
    def exclaim(self):  # メソッドのオーバーライド
        print("I'm Yugo! Much like a Car, but more Yugo-ish.")


Car().exclaim()     # Car の exclaim が呼ばれる
Yugo().exclaim()    # Yugo の exclaim が呼ばれる


class MDPerson(Person):                 # 医者
    def __init__(self, name):           # コンストラクタをオーバーライド
        self.name = "Doctor " + name


class JDPerson(Person):                 # 弁護士
    def __init__(self, name):           # コンストラクタをオーバーライド
        self.name = name + ", Esquire"


person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name, doctor.name, lawyer.name)


# メソッドの追加
class CarOfYugo(Car):
    def exclaim(self):
        print("I'm Yugo! Much like a Car, but more Yugo-ish.")

    def need_a_push(self):      # Car クラスにはないメソッドの追加
        print("A little help here?")


CarOfYugo().need_a_push()


# 親クラスのメソッドの呼び出し(super)
class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)    # 親クラス(Person)のコンストラクタを呼び出す
        self.email = email


bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name, bob.email)


# プロパティによる属性値のカプセル化
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):                     # ゲッターメソッド
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):         # セッターメソッド
        print('inside the setter')
        self.hidden_name = input_name

    name = property(get_name, set_name)     # name プロパティのゲッター、セッターとして定義


fowl = Duck('Howard')
print(fowl.name)        # get_name ゲッターメソッドを呼び出す
fowl.name = 'Daffy'     # set_name セッターメソッドを呼び出す
print(fowl.name)        # Daffy


class DecoratedDuck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property       # ゲッターをデコレータで定義
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter    # セッターをデコレータで定義
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


fowl = DecoratedDuck('Howard')
print(fowl.name)        # ゲッターの呼び出し
fowl.name = 'Donald'    # セッターの呼び出し
print(fowl.name)        # Donald


class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property      # ゲッターをデコレータで定義
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(c.radius)     # radius 値は初期化されている
print(c.diameter)   # diameter のゲッターが呼ばれる
c.radius = 7
print(c.diameter)   # diameter は radius の値によって変わる

try:
    c.diameter = 20     # セッターは指定されてないので値は設定できない！
except AttributeError as err:
    print("can't set attribute")


# 非公開属性のための名前のマングリング
class HiddenDuck():
    def __init__(self, input_name):
        self.__name = input_name    # 先頭にふたつのアンダースコア(__)を付けると非公開属性

    @property       # ゲッターを設定
    def name(self):
        print('inside the getter')
        return self.__name

    @name.setter    # セッターを設定
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name


try:
    HiddenDuck('Howard').__name
except AttributeError as err:
    print('\'HiddenDuck\' object has no attribute \'__name\'')


# メソッドのタイプ
class A():
    __count = 0     # クラス属性(かつ非公開)

    def __init__(self):
        A.__count += 1      # このクラスが生成された数を数える

    def exclaim(self):
        print("I'm an A!")

    @classmethod        # クラスメソッド
    def kids(cls):
        print("A has", cls.__count, "little objects.")


easy_a = A()
breezy_a = A()
Wheezy_a = A()
A.kids()        # ３つ生成した


class CoyoteWeapon():
    @staticmethod       # 静的メソッド(クラスにもオブジェクトにも影響を与えない)
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')


CoyoteWeapon.commercial()


# ダックタイピング(ポリモーフィズムの緩やかな実現)
class Quote():
    def __init__(self, person, words):
        self.__person = person
        self.__words = words

    @property
    def person(self):
        return self.__person

    @property
    def words(self):
        return self.__words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'


class QuestionQuote(Quote):         # __init__がないときは親クラスのものを呼び出す
    def says(self):                 # ポリモーフィズムの実現
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):                 # ポリモーフィズムの実現
        return self.words + '!'


def who_says(hunter):
    print(hunter.who(), 'says:', hunter.says())     # says() メソッドが異なる動作


who_says(Quote('Elmer Fudd', "I'm hunting wabbits"))
who_says(QuestionQuote('Bugs Bunny', "What's up, doc"))
who_says(ExclamationQuote('Daffy Duck', "It's rabbit season"))


class BabblingBrook():  # Quote とはまるで関係ないクラス
    def who(self):
        return 'Brook'

    def says(self):
        return 'Babble'


who_says(BabblingBrook())   # 共通のインターフェースなら継承すら必要ない(ダックタイピング)
