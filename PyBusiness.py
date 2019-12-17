#!/usr/bin/python


#
# Microsoft Office スイート
#


ms_office_lib = {
    'docx':
    'MS Office Word 2007 の.docxファイルの読み書き',
    'python-excel':
    'xlrd, xlwt, xlutils モジュール',
    'oletools':
    'Office形式のデータを抽出するライブラリ',
    'pywin32':
    '多くのWindowsアプリケーションをオートメーションで実行',
    'pywinauto':
    'Windowsアプリケーションをオートメーションで実行',
    'swapy':
    'ネイティブコントロールからpywinauto用のPythonコードを生成',
    }


other_biz_tools = {
    'PyUNO':
    'OpenOffice, LibreOfficeのプログラミング用Pythonブリッジ',
    'python-magic':
    '特定のバイトシーケンスを解析してファイル形式を推測',
    'python open document':
    '動的ドキュメント作成ののためのテンプレートへのPythonコードの供給',
    'ReportLab':
    'PythonベースPDFジェネレータ',
    }


#
# ビジネスデータの処理
#


# 抽出, 変換, ロード
def zoo_counts():  # スプレットシートのデータをデータベースに移す作業サンプル
    import csv
    from collections import Counter

    counts = Counter()
    with open('files/zoo.csv', 'rt') as fin:
        cin = csv.DictReader(fin)
        for row in cin:  # 動物(animal)が噛んだことによる慰謝料(hush)を集計する
            counts[row['animal']] += int(row['hush'])
    for animal, hush in counts.items():
        print("%10s %10s" % (animal, hush))


def zoo_counts_bubbles():  # Bubblesデータ処理ツールキットを使って簡略化出来る
    import bubbles

    p = bubbles.Pipeline()
    p.source(
        bubbles.data_object('csv_source', 'files/zoo.csv', infer_fields=True))
    p.aggregate('animal', 'hush')  # animalごとのhushを集計する
    p.pretty_print()  # 整形して表示


#
# 金融界での Python
#


py_economics = {
    'Quantitative economics':
    '計量経済学的なモデリングのためのツール',
    'Python for finance':
    'Derivatives Analytics with Python',
    'Quantopian':
    '独自のPythonコードを株価の履歴データに対して実行、結果が見れる対話的サイト',
    'PyAlgoTrade':
    '株式関連の戦略、モデルなどのテスト',
    'Quandl':
    '数百万の金融データセットの検索',
    'Ultra-finance':
    '株式関連の情報収集ライブラリ',
    "Python for Finance(O'Reilly)":
    '金融モデリングのためのPythonサンプル',
    }


#
# ビジネスデータのセキュリティ
#


py_biz_sec = {
    'Scapy': 'ネットワークに対する攻撃の説明に使用される',
    'Python Security': 'http://www.pythonsecurity.org/',
    'Violent Python': 'Pythonとコンピュータのセキュリティを包括的に扱った著書',
    }


#
# マップ
#


# ファイル形式
shp = {
    '.shp': 'シェープ(ベクトル)情報',
    '.shx': 'シェープインデックス',
    '.dbf': '属性データベース',
    }


# Python で役に立つシェープファイルモジュール
py_shp_lib = {
    'pyshp':
    'ピュアPythonのシェープファイルライブラリ',
    'shapely':
    'この町の建物の中で５０年前の洪水の範囲内になるものはどれか、などの地理上の問いに答える',
    'fiona':
    'シェープファイルなどのベクトル形式ファイルを処理するOGRライブラリをラップする',
    'kartograph':
    'サーバーまたはクライアント上でシェープファイルをSVGマップにレンダリングする',
    'basemap':
    'matplotlibを使って2Dデータを地図上にプロットする',
    'cartopy':
    'matplotlibとshapelyを使って地図を描画する',
    }


# 地図の描画
def display_shapefile():
    import shapefile
    from PIL import Image, ImageDraw
    shpname = 'files/shape/ne_110m_admin_1_states_provinces'
    iwidth, iheight = 500, 500

    r = shapefile.Reader(shpname)
    mleft, mbottom, mright, mtop = r.bbox
    # 地図の単位
    mwidth = mright - mleft
    mheight = mtop - mbottom
    # 地図の単位をイメージの単位にマッピング
    hscale = iwidth/mwidth
    vscale = iheight/mheight
    # 地図を描画
    img = Image.new("RGB", (iwidth, iheight), "white")
    draw = ImageDraw.Draw(img)
    for shape in r.shapes():
        pixels = [
            (int(iwidth - ((mright - x) * hscale)), int((mtop - y) * vscale))
            for x, y in shape.points]  # シェープの座標をイメージに合わせてスケーリングする
        if shape.shapeType == shapefile.POLYGON:
            draw.polygon(pixels, outline='black')   # ポリゴンの描画
        elif shape.shapeType == shapefile.POLYLINE:
            draw.line(pixels, fill='black')         # ポリラインの描画
    img.show()


# その他の Python マッピングソフトウェア
other_py_mapping = {
    'basemap':
    'matplotlibを基礎として、地図とデータのオーバーレイを書く',
    'mapnik':
    'Pythonバインディングを持つC++ライブラリ',
    'tilemill':
    'mapnikを基礎とするマップデザインスタジオ',
    'Vincent':
    'JavaScriptビジュアライゼーションツールのVegaへの変換',
    'Python for ArcGIS':
    'ESRIの商用製品、ArcGisのためのPythonリソース',
    'Spatial analysis with python':
    'チュートリアル、パッケージ、ビデオへのリンク',
    'Using geospatial data with python(YouTube)':
    'ビデオによるプレゼンテーション',
    "So you'd like to make a map using Python":
    'pandas, matplotlib, shapelyなどのPythonモジュールを使って歴史的な地域の地図を作る',
    'Python Geospatial Development(Packt)':
    'mapnikなどのツールを使ったサンプルが含まれる著書',
    'Learning Geospatial Analysis with Python(Packt)':
    'ファイル形式やライブラリを解説し、ジオスペーシャルアルゴリズムも取り上げている著書',
    }


# アプリケーションとデータ
geocoding_api = {  # ジオコーディング : 住所と緯度経度を相互に変換する
    'geopy', 'pygeocoder', 'googlemaps',
    }


mapping_data = {  # マッピングデータが入手できる場所
    'http://www.census.gov/geo/maps-data/':
    '米国国政調査局のマップファイルの概要',
    'http://www.census.gov/geo/maps-data/data/tiger.html':
    '地理、人口統計データなどの宝庫',
    'http://wiki.openstreetmap.org/wiki/Potential_datasources':
    '世界のデータソース',
    'http://www.naturalearthdata.com/':
    '３種類のサイズのベクトル、ラスターマップデータ',
    }


Data_Science_Toolkit = {  # フリーの双方向ジオコーディング、政治的境界線や統計のための座標データ
    'Data Science Toolkit': 'http://www.datasciencetoolkit.org'
    }


if __name__ == '__main__':
    zoo_counts()
    zoo_counts_bubbles()
    display_shapefile()
