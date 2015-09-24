# -*- coding: utf-8 -*-
# Project pxchar

import sys
import os.path
from PIL import Image

DEFAULT_WIDTH = 400;

def generateImage():
    #
    pass;

# テキストファイルを一文字ずつ読み込む
def readChar(filePath):
    # カラーデータを保持する配列
    colors = [];

    # 有効なパスかどうか判定
    if os.path.isfile(filePath) is not True:
        return;

    # 一文字ずつ読み取り、カラーを決定して保持する


    # 総文字数から画像サイズを決定する
    charNums = len(colors);
    if charNums > 0:
        generateImage(colors);

    print charNums;
    pass;

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
