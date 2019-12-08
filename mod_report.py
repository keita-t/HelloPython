
#
# Module.py でインポートされる
#


def get_description():
    """プロと同じようにランダムな天気を返す"""
    from random import choice  # random モジュールから choice を直接インポート
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)
