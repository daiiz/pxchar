# -*- coding: utf-8 -*-
# Project pxchar

import sys
import os.path
from PIL import Image

DEFAULT_WIDTH = 400;

# color辞書（とりあえず決め打ち）
COLORS = {
    "?": (255, 255, 255),   # 不明な文字
    "*": (0, 0, 0),         # 終端文字
    "%": (255,235,59),
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
    "z": (255,171,64)
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
                        cColor = COLORS['?'];
                    colors.append(cColor);

        # 次の行を見る
        line = f.readline();
    f.close;
    colors.append(COLORS['*']); #終端

    # 総文字数から画像サイズを決定する
    charNums = len(colors);
    if charNums > 0:
        generateImage(colors);


# 読み込んだ文字からピクセルデータを決定する
def determinePxColor(char):
    pass;


if __name__ == '__main__':
    print 'Hello!';
    # 引数からテキストファイルのパスを得る
    argv = sys.argv;
    if len(argv) == 2:
        filePath = argv[1];
        readChar(filePath);

    print 'Done!';
