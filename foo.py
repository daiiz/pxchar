# -*- coding: utf-8 -*-
# Project pxchar

import sys
import os.path
from PIL import Image

DEFAULT_WIDTH = 100;

# バージョンは一文字で表す
VERSION = '0';

# color辞書（とりあえず決め打ち）
COLORS = {
    "??": (255, 255, 255),   # 不明な文字
    "<" : (0, 0, 0),         # 終端文字
    ">" : (69,90,100),       # ファイル改行
    "%" : (255,235,59),
    # 数字
    "0": (244,67,54),
    "1": (156,39,176),
    "2": (103,58,183),
    "3": (33,150,243),
    "4": (3,169,244),
    "5": (0,188,212),
    "6": (0,150,136),
    "7": (76,175,80),
    "8": (205,220,57),
    "9": (255,152,0),
    # a-z
    "a": (255,138,128),
    "b": (255,128,171),
    "c": (234,128,252),
    "d": (179,136,255),
    "e": (140,158,255),
    "f": (130,177,255),
    "g": (128,216,255),
    "h": (132,255,255),
    "i": (167,255,235),
    "j": (185,246,202),
    "k": (204,255,144),
    "l": (244,255,129),
    "m": (255,255,141),
    "n": (255,229,127),
    "o": (255,209,128),
    "p": (255,158,128),
    "q": (215,204,200),
    "r": (158,158,158),
    "s": (96,125,139),
    "t": (255,82,82),
    "u": (255,64,129),
    "v": (224,64,251),
    "w": (124,77,255),
    "x": (83,109,254),
    "y": (64,196,255),
    "z": (255,171,64),
    # A-Z
    "A": (183,28,28),
    "B": (136,14,79),
    "C": (74,20,140),
    "D": (49,27,146),
    "E": (13,71,161),
    "F": (1,87,155),
    "G": (0,96,100),
    "H": (0,77,64),
    "I": (27,94,32),
    "J": (51,105,30),
    "K": (130,119,23),
    "L": (245,127,23),
    "M": (255,111,0),
    "N": (230,81,0),
    "O": (191,54,12),
    "P": (62,39,35),
    "Q": (38,50,56),
    "R": (255,23,68),
    "S": (245,0,87),
    "T": (213,0,249),
    "U": (101,31,255),
    "V": (61,90,254),
    "W": (41,121,255),
    "X": (0,229,255),
    "Y": (0,230,118),
    "Z": (255,145,0)
};

def generateImage(colors):
    height = len(colors) / DEFAULT_WIDTH + 1;
    width  = DEFAULT_WIDTH;
    canvas = Image.new("RGB", (width, height), (0,0,0));

    for y in range(0, height):
        for x in range(0, width):
            if width * y + x < len(colors):
                canvas.putpixel((x,y), colors[width * y + x]);

    canvas.save("px/test-0.png");


# テキストファイルを一文字ずつ読み込む
def readChar(filePath):
    # カラーデータを保持する配列
    colors = [];

    # colorsの最初の要素は、バージョン
    colors.append(COLORS[VERSION]);

    # 有効なパスかどうか判定
    if os.path.isfile(filePath) is not True:
        return;

    # 一行ずつ読み取り、カラーを決定して保持する
    f = open(filePath);
    line = f.readline();
    while line:
        if len(line) > 0:
            # 一文字ずつ読む
            for c in line:
                if c != '\n':
                    # colorをゲット
                    if COLORS.has_key(c) is True:
                        cColor = COLORS[c];
                    else:
                        cColor = COLORS['??'];
                    colors.append(cColor);

        # 次の行を見る
        colors.append(COLORS['>']); #ファイル改行
        line = f.readline();
    f.close;
    colors.append(COLORS['<']); #終端

    # 総文字数から画像サイズを決定する
    charNums = len(colors);
    if charNums > 0:
        generateImage(colors);

if __name__ == '__main__':
    print 'Hello!';
    # 引数からテキストファイルのパスを得る
    argv = sys.argv;
    if len(argv) == 2:
        filePath = argv[1];
        readChar(filePath);

    print 'Done!';
