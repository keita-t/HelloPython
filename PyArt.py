#!/usr/bin/python
import os


#
# 2D グラフィックス
#


# 標準ライブラリ
def image_type():
    import imghdr
    print(imghdr.what('oreilly.png'))  # イメージファイルのファイルタイプを抽出


# PIL と Pillow
def image_show_pillow():  # Pillow(PIL)を使って画面にイメージを表示
    from PIL import Image
    img = Image.open('oreilly_pil.png')
    print(img.format)   # イメージのフォーマット
    print(img.size)     # イメージのサイズ
    print(img.mode)     # イメージのカラーモード

    img.show()          # 画面に表示


def image_cs_pillow():  # メモリ内のイメージの切り取りと保存
    from PIL import Image
    img = Image.open('oreilly.png')

    crop = (5, 5, 280, 70)
    img = img.crop(crop)  # 左上のx,y 右下のx,y の座標でイメージを切り取り
    img.show()

    img.save('cropped.gif', 'GIF')  # 切り取ったイメージをGIF形式で保存
    cimg = Image.open('cropped.gif')
    print(cimg.format)  # 'GIF'
    print(cimg.size)    # (275, 65)


def image_paste_pillow():  # イメージの貼り付け
    from PIL import Image
    mustache = Image.open('mustaches.png')          # mustaches.pngを読み込み
    handlebar = mustache.crop((0, 30, 100, 70))     # 範囲を切り取り
    print(handlebar.size)

    img = Image.open('oreilly.png')
    img.paste(handlebar, (178, 40))      # oreilly.pngに切り取ったmustache.pngを貼り付け
    img.show()


# ImageMagick
def image_show_im():  # ImageMagickを使ってイメージを表示
    from wand.image import Image
    from wand.display import display

    img = Image(filename='oreilly_im.png')  # oreilly.pngを読み込み
    print(img.size)     # サイズを表示
    print(img.format)   # フォーマットを表示

    display(img)


#
# GUI (グラフィカル・ユーザー・インタフェース)
#


# Tkinter
def show_window_tkinter():
    import tkinter
    from PIL import Image, ImageTk

    main = tkinter.Tk()  # メインウィンドウを取得
    img = Image.open('oreilly.png')
    tkimg = ImageTk.PhotoImage(img)  # Tkinter用のイメージを取得

    tkinter.Label(main, image=tkimg).pack()  # メインウィンドウにイメージラベルを追加
    main.mainloop()  # メインウィンドウを表示


# その他の GUI 環境
gui_toolkit = {
    'PySide': 'Pythonで使えるLGPLライセンスのQtライブラリ',
    'PyQt': 'Pythonで使えるGPLライセンスのQtライブラリ',
    'PyGTK': 'GTK+ Pythonバインディング',
    'WxPython': 'WxWidgets Pythonバインディング',
    'Kivy': '様々なプラットフォームに対応したマルチメディアユーザーインタフェース',
    }


#
# 3D グラフィックスとアニメーション
#


# Panda3D
def panda_sample3d():  # Panda3Dによる3Dグラフィックス描画サンプル
    from direct.showbase.ShowBase import ShowBase

    class MyApp(ShowBase):
        def __init__(self):
            ShowBase.__init__(self)

            # 環境モデルをロードする
            self.environ = self.loader.loadModel("models/environment")
            # レンダリングのために親を変更する
            self.environ.reparentTo(self.render)
            # モデルに対してスケーリングと位置変更を行う
            self.environ.setScale(0.25, 0.25, 0.25)
            self.environ.setPos(-8, 42, 0)

    app = MyApp()
    app.run()


# その他の 3D パッケージ
rendering_3d = {
    'Blender': 'フリーの3Dアニメーション、ゲーム作成システム',
    'Maya': '商用の3Dアニメーション、グラフィックスシステム',
    'Houdini': 'Apprenticeというフリーバージョンがある',
    }


#
# プロット, グラフ, ビジュアライゼーション
#


# matplotlib
def show_matplotlib():  # matplotlibを使ったプレゼンテーション
    import matplotlib.pyplot as plot
    import matplotlib.image as image

    img = image.imread('oreilly.png')   # イメージの読み込み
    plot.imshow(img)                    # プロットにイメージを追加
    plot.show()                         # プロットを表示


# bokeh
bokeh = {'bokeh': 'http://bit.ly/bokeh-dl'}


#
# ゲーム
#
pygame = {'pygame': 'http://pygame.org/download.shtml'}


#
# サウンドと音楽
#
music_api = {
    'pyknon': 'Music for Geeks and Nerds',
    'mingus': 'MIDIファイルを読み書きできるミュージックシーケンサー',
    'remix': '音楽のリミックスのためのAPI',
    'sebastian': '音楽理論と分析のためのライブラリ',
    'Piano': 'キーボードでピアノを弾けるようにする',
    }


music_lib_api = {
    'Beets': '音楽コレクションを管理',
    'Echonest API': '音楽のメタデータにアクセス',
    'Monstermash': '楽曲の断片をマッシュアップ',
    'Shiva': 'コレクションについてのクエリーを発行するためのRESTful APIとサーバー',
    'MPD Album Art Grabber': '音楽に会うアルバムアートを取得',
    }


if __name__ == '__main__':
    cdir = os.getcwd()  # 現在のカレントディレクトリを保存
    os.chdir('files/graphics')  # 作業ディレクトリを files/graphics に変更する

    image_type()
    image_show_pillow()
    image_cs_pillow()
    image_paste_pillow()
    image_show_im()
    show_window_tkinter()
    show_matplotlib()
    panda_sample3d()

    os.chdir(cdir)
