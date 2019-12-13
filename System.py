#!/usr/bin/python

# ファイルとディレクトリ
import os
import shutil
import stat
import glob

# プログラムとプロセス
import subprocess
import multiprocessing

# カレンダーとクロック
import time
import calendar
import datetime
from datetime import date, timedelta
import locale

#
# ファイル
#

# 作業ディレクトリを files/system に変更する
cdir = os.getcwd()  # 現在のカレントディレクトリを保存
os.chdir('files/system')

# open() による作成
fout = open('oops.txt', 'wt')  # テスト用 oops.txt の作成
fout.write('Oops, I created a file.' + '\n')
fout.close()

# exists() によるファイルやディレクトリが存在することのチェック
print(os.path.exists('oops.txt'))     # True
print(os.path.exists('./oops.txt'))   # True
print(os.path.exists('waffles'))      # False
print(os.path.exists('.'))            # カレントディレクトリ(True)
print(os.path.exists('..'))            # 親ディレクトリ(True)

# isfile() によるファイルタイプのチェック
name = 'oops.txt'
print(os.path.isfile(name))             # 引数は普通のファイルか(True)
print(os.path.isdir(name))              # 引数はディレクトリか(False)
print(os.path.isdir('.'))               # True
print(os.path.isabs(name))              # 引数は絶対パスか(実際に存在しなくてもよい,False)
print(os.path.isabs('/big/fake/name'))  # True
print(os.path.isabs('big/fake/name/without/a/leading/slash'))  # False

# copy() によるコピー
shutil.copy(
    'oops.txt', 'ohno.txt')  # oops.txtをohno.txtにコピー
shutil.move(
    'oops.txt', 'ouch.txt')  # コピーしてからオリジナルを削除

# rename() によるファイル名の変更
os.rename('ohno.txt', 'ohwell.txt')  # ファイル名の変更

# link(), symlink() によるリンクの作成
if not os.path.isfile('yikes.txt'):
    os.link('ouch.txt', 'yikes.txt')  # yikes.txtからouch.txtへのハードリンクを作成

if not os.path.islink('jeepers.txt'):  # シンボリックリンク jeepers.txt はあるか
    os.symlink('ouch.txt',
               'jeepers.txt')  # jeepers.txtからouch.txtへのシンボリックリンクを作成

# chmod() によるパーミッションの変更
os.chmod('ouch.txt', 0o400)         # パーミッションを変更する(読み出しのみ)
os.chmod('ouch.txt', stat.S_IRUSR)  # statを使うと明示的に定数で指定できる
# os.chmod('ouch.txt', 0o664)


# chown() によるオーナーの変更
def chown():
    uid, gid = 5, 22
    os.chown('ouch.txt', uid, gid)  # ファイルのオーナー(uid)、グループ所有権(gid)を変更する


# abspath() によるパス名の取得
print(os.path.abspath('ouch.txt'))  # 相対パスを絶対パスに拡張

# realpath() によるシンボリックリンクパス名の取得
print(os.path.realpath('jeepers.txt'))  # シンボリックリンクからリンク先の名前を取得(ouch.txt)

# remove() によるファイルの削除
os.remove('ohwell.txt')  # ohwell.txt を削除
print(os.path.exists('ohwell.txt'))  # False

#
# ディレクトリ
#

# mkdir() による作成
if not os.path.exists('poems'):
    os.mkdir('poems')  # poems ディレクトリの作成
    print(os.path.exists('poems'))  # True

# rmdir() による作成
if not os.listdir('poems'):
    os.rmdir('poems')  # poems ディレクトリを削除
    print(os.path.exists('poems'))  # False

# listdir() による内容リストの作成
if not os.path.exists('poems'):
    os.mkdir('poems')  # poems ディレクトリの作成
    print(os.listdir('poems'))  # ディレクトリに含まれるもののリストを取得(今のところ何もない)

    os.mkdir('poems/mcintyre')  # poems ディレクトリ下に mcintype サブディレクトリを作る
    print(os.listdir('poems'))  # ['mcintyre']

fout = open('poems/mcintyre/the_good_man.txt', 'wt')  # サブディレクトリにファイルを作る
fout.write('''Cheerful and happy was his mood,
He to te poor was king and good,
He to the poor was kind and good,
And he oft' times did find them food,
Also supplies of coal and wood,
He never spake a word aws fude,
And cheer'd those did o'er sorrows brood,
He passed away ot understood,
Because no poet in his lays
Had penned a sonnet in his praise,
'Tis sad, but such is world's ways.
''')
fout.close()

print(os.listdir('poems/mcintyre'))  # ['the_good_man']

# chdir() によるカレントディレクトリの変更
os.chdir('poems')       # カレントディレクトリを poems に変更
print(os.listdir('.'))  # ['mcintyre']

# glob() によるパターンにマッチするファイルのリストの作成
print(glob.glob('m*'))          # mで始まるファイル、ディレクトリのリストを作成(['mcintyre'])
print(glob.glob('??'))          # 何であれ２文字の名前を持つファイル、ディレクトリ([])
print(glob.glob('m??????e'))    # mで始まりeで終わる８文字のファイル名があったはず('[mcintyre]')
print(glob.glob('[klm]*e'))     # k,l,mのどれかで始まりeで終わるファイルはどうか('[mcintyre]')

# カレントディレクトリを復元
os.chdir(cdir)

#
# プログラムとプロセス
#

print(os.getpid())  # プロセスIDを取得
print(os.getcwd())  # 現在のカレントディレクトリを取得

print(os.getuid())  # ユーザーIDを取得
print(os.getgid())  # グループIDを取得

# subprocess によるプロセスの作成
ret = subprocess.getoutput('date')  # シェルの中でプログラム(date)を起動し、生成された出力を取得
print(ret)  # `date`の出力を表示(標準出力と標準エラー出力の両方)
ret = subprocess.getoutput('date -u')  # 引数は完全なシェルコマンドを表す文字列(`date -u`)
print(ret)  # `date -u`の出力を表示
ret = subprocess.getoutput('date -u | wc')  # もちろんパイプも使える
print(ret)  # `date -u | wc`の出力を表示

ret = subprocess.check_output(
        ['date', '-u'])  # コマンドと引数のリストを受け取りbyte形式で標準出力を返す(シェルは使わない)
print(ret)  # bytes形式で`date -u`の出力を表示

ret = subprocess.getstatusoutput('date')  # 終了ステータスコードと出力のタプルを返す
print(ret)  # (0, `date`), Unix系システムでは終了ステータス0は成功
ret = subprocess.call('date')  # 終了ステータスだけ返される(結果が出力に表示されるがプログラムには渡されない)
print(ret)  # 期待値は 0

ret = subprocess.call(
    'date -u', shell=True)  # 引数を取るプログラムを実行,shell=Trueで文字列をシェルのコマンドとして展開
ret = subprocess.call(['date', '-u'])  # 引数のリストを作って実行,シェルを呼び出さずに住む


# multiprocessing によるプロセスの生成
class multi_processing():
    def do_this(self, what):
        self.whoami(what)

    def whoami(self, what):
        print("Process %s says: %s" % (os.getpid(), what))

    def run(self, count):
        self.whoami("I'm the current process")
        for n in range(count):  # プロセスはcount個実行される
            # 新しいプロセスを起動し、そのなかでdo_this()関数を実行
            p = multiprocessing.Process(
                target=self.do_this, args=("I'm function %s" % n,))
            p.start()


multi_processing().run(4)  # 4個プロセスを作って実行


# terminate() によるプロセスの強制終了
class terminate_process():
    def whoami(self, name):
        print("I'm %s, in process %s" % (name, os.getpid()))

    # 100万まで数えようとして１ステップ毎に１秒眠り、イライラするメッセージを表示する
    def loopy(self, name):
        self.whoami(name)
        start = 1
        stop = 1000000
        for num in range(start, stop):
            print("\tNumber %s of %s. Honk!" % (num, stop))
            time.sleep(1)

    def run(self):
        self.whoami("current process")
        p = multiprocessing.Process(
            target=self.loopy, args=("loopy",))
        p.start()
        time.sleep(5)  # 5秒間待機する
        p.terminate()  # terminate()によるloopyプロセスの強制終了


terminate_process().run()

#
# カレンダーとクロック
#

# 様々な年がうるう年かどうか
print(calendar.isleap(1900))  # False
print(calendar.isleap(1996))  # True
print(calendar.isleap(1999))  # False
print(calendar.isleap(2000))  # True
print(calendar.isleap(2002))  # False
print(calendar.isleap(2004))  # True

# datetime モジュール
halloween = date(2014, 10, 31)  # 年月日を指定してdateオブジェクトを作成
print(halloween.day)            # 日(31)
print(halloween.month)          # 月(10)
print(halloween.year)           # 年(2014)
print(halloween.isoformat())    # ISO 8601 による日時表現('2014-10-31')

now = date.today()              # 今日の日付を生成
print(now)

one_day = timedelta(days=1)     # 一日を表現するtimedeltaオブジェクト
tomorrow = now + one_day        # 今日の一日後で明日
print(tomorrow)
print(now + (17 * one_day))     # 今日から17日後
yesterday = now - one_day       # 今日の一日前で昨日
print(yesterday)

noon = datetime.time(12, 0, 0)  # 時刻を表現するdatetimeモジュールtimeオブジェクト(12時)
print(noon.hour)                # 時(12)
print(noon.minute)              # 分(0)
print(noon.second)              # 秒(0)
print(noon.microsecond)         # マイクロ秒(0)

some_day = \
    datetime.datetime(2014, 1, 2, 3, 4, 5, 6)  # 日付と時間を含む(2014年1月2日3時4分5秒6μ秒)
print(some_day)
print(some_day.isoformat())     # '2014-01-02T03:04:05.000006'
now = datetime.datetime.now()   # 現在の日付と時刻を生成
print(now.year)                 # 現在の年
print(now.month)                # 現在の月
print(now.day)                  # 現在の日
print(now.hour)                 # 現在の時
print(now.minute)               # 現在の分
print(now.second)               # 現在の秒
print(now.microsecond)          # 現在のマイクロ秒

noon = datetime.time(12)
this_day = date.today()
noon_today = \
 datetime.datetime.combine(this_day, noon)  # dateオブジェクトとtimeオブジェクトを結合
print(noon_today)  # datetime.datetime(2014, 2, 2, 12, 0)
noon_today.date()  # dateオブジェクトを抽出(datetime.date(2014, 2, 2))
noon_today.time()  # timeオブジェクトを抽出(datetime.time(12, 0))

# time モジュールの使い方
now = time.time()           # 現在時をUnix時間で返す
print(now)
print(time.ctime(now))      # Unix時間を文字列に変換
print(time.localtime(now))  # システムの標準時での日時をstruct_timeオブジェクトとして返す
print(time.gmtime(now))     # UTCでの日時をstruct_timeオブジェクトとして返す
tm = time.localtime(now)
print(time.mktime(tm))      # struct_timeオブジェクトをUnix時間に変換する

# 日時の読み書き

# strtime()の書式指定子
strtime_format = {  # 書式指定子 : 意味 : 範囲
    '%Y': ('年', '1900-...'),
    '%m': ('月', '01-12'),
    '%B': ('月名', 'January,...'),
    '%b': ('月略称', 'Jan,...'),
    '%d': ('日', '01-31'),
    '%A': ('曜日', 'Sunday,...'),
    '%a': ('曜日略称', 'Sun,...'),
    '%H': ('時間(24時)', '00-23'),
    '%I': ('時間(12時)', '01-12'),
    '%M': ('分', '00-59'),
    '%S': ('秒', '00-59'),
    }

fmt = "It's %A, %B %d, %r, local time %I:%M:%S%P"  # 日時を表示する書式指定フォーマット
t = time.localtime()
print(t)                            # 現在時のstruct_timeオブジェクト
print(time.strftime(fmt, t))        # 書式指定フォーマットでstruct_timeオブジェクトを文字列に変換
some_day = date(2014, 7, 4)         # dataオブジェクト
print(some_day.strftime(fmt))       # 日付の部分だけが整形される(時刻はデフォルトで深夜0時)
some_time = datetime.time(10, 35)   # timeオブジェクト
some_time = time.strftime(fmt)      # 時刻の部分だけが変更される

fmt = "%Y-%m-%d"
print(time.strptime("2019-01-29", fmt))  # 書式指定フォーマットで文字列をstruct_timeに変換

lnames = locale.locale_alias.keys()  # ロケール名を表す文字列をすべて取得
good_names = [lname for lname in lnames if len(lname) == 5 and lname[2] == '_']
print(good_names[:5])  # '言語_国'のロケール名だけを取り出して最初の５つを表示

de = [lname for lname in good_names if lname.startswith('de')]
print(de)  # ドイツ語のロケールをすべて取得して表示


def set_locale():
    halloween = date(2014, 10, 31)
    for lang_country in good_names[:5]:
        locale.setlocale(locale.LC_TIME, locale=lang_country)  # 日時のロケールを変更する
        print(halloween.strftime('%A, %B, %d'))  # フォーマットに従って設定したロケールの言語で表示する


# set_locale()


# 代替モジュール
other_datetime_mod = {
    'arrow', 'dateutil', 'iso8601', 'fleming'
    }
