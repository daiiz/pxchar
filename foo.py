# -*- coding: utf-8 -*-
# Project pxchar

import sys
import os.path
from PIL import Image

DEFAULT_WIDTH = 400;

# color辞書（とりあえず決め打ち）
COLORS = {
    "?": (255, 255, 255),   # 不明な文字
    "*": (0, 0, 0)          # 終端文字
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
