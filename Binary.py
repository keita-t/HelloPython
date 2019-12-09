#!/usr/bin/python

#
# バイナリデータ
#

# バイトとバイト列
blist = [1, 2, 3, 255]
the_bytes = bytes(blist)            # バイト（イミュータブル）
print(the_bytes)                    # b'\x01\x02\x03\xff'
the_byte_array = bytearray(blist)   # バイト列(ミュータブル)
print(the_byte_array)               # bytearray(b'\x01\x02\x03\xff')

print(b'\x61')  # bytes 値を表現するには、 bを先頭にしてクォートで囲む(有効なら ASCII 文字で表示)
print(b'\x01abc\xff')  # b'\x01abc\xff'(abc は ASCII 文字に対応するバイト値)

try:
    the_bytes[1] = 127  # bytes はイミュータブルで書き込み不可
except TypeError as err:
    print("'bytes' object does not support item assignment")

the_byte_array[1] = 127     # bytearray はミュータブルで書き込み可能
print(the_byte_array)       # bytearray(b'\x01\x7f\x03\xff')

the_bytes = bytes(range(0, 256))  # 0 から 255 までの 256 個の要素をもつ bytes
the_byte_array = bytearray(range(0, 256))  # 上と同じ要素をもつ bytearray
print(the_bytes)  # 印字可能バイトについては対応する ASCII 文字の表示となる


# struct によるバイナリデータの変換
def read_PNG_size():  # PNG形式の画像のサイズを抽出する
    import struct
    vlid_png_header = b'\x89PNG\r\n\x1a\n'  # 有効なPNGファイルの先頭を示す8バイトのシーケンス
    data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
        b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'  # 先頭30バイト
    if data[:8] == vlid_png_header:  # 先頭8バイトは有効なPNGファイルを示しているか
        # '>LL' ビッグエンディアン(>)で4バイト符号なし長整数を２つ(LL) data[16:24] から抽出
        width, height = \
            struct.unpack('>LL', data[16:24])
        print('Valid PNG, width', width, 'height', height)  # 抽出したサイズを表示
    else:
        print('Not a valid PNG')


def pack_bytes():
    import struct
    struct.pack('>L', 154)  # Python データをバイトに変換, b'\x00\x00\x00\x9a'
    struct.pack('>L', 141)  # b'\x00\x00\x00\x8d'


read_PNG_size()
pack_bytes()


# エンディアン指定子(struct)
endian = {
    '<': 'リトルエンディアン',
    '>': 'ビッグエンディアン',
    }

# 書式指定子(struct)
struct_format = {  # 指定子: (説明, バイト数)
    'x': ('1バイト読み飛ばし', 1),
    'b': ('符号付きバイト', 1),
    'B': ('符号なしバイト', 1),
    'h': ('符号付き短整数', 2),
    'H': ('符号なし短整数', 2),
    'i': ('符号付き整数', 4),
    'I': ('符号なし整数', 4),
    'l': ('符号付き長整数', 4),
    'L': ('符号なし長整数', 4),
    'Q': ('符号なし長長整数', 8),
    'f': ('単精度浮動小数点数', 4),
    'd': ('倍精度浮動小数点数', 8),
    'p': ('countと文字シーケンス', '1+count'),
    's': ('文字シーケンス', 'count'),
    }

# struct.unpack('>2L', data[16:24]) ... LL の代わりにcountプレフィックスを使える
# struct.unpack('>16x2L6x', data) ... x指定子で関心のないバイトを読み飛ばす


# binascii によるバイト/文字列の変換
def bin_ascii():
    import binascii
    valid_png_heder = b'\x89PG\r\n\x1a\n'
    print(binascii.hexlify(valid_png_heder))  # 16進数のシーケンスとして表示する
    print(binascii.unhexlify(b'89504e470d0a1a0a'))  # hexlify の逆


bin_ascii()


# ビット演算子
bit = {  # 演算子: (説明, 例)
    '&': ('AND', 'a & b'),
    '|': ('OR', 'a | b'),
    '^': ('排他的OR', 'a ^ b'),
    '~': ('ビット反転', '~a'),
    '<<': ('左シフト', 'a << 1'),
    '>>': ('右シフト', 'a >> 1'),
    }
