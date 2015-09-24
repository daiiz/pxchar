# -*- coding: utf-8 -*-
# Project pxchar

import sys
import os.path
from PIL import Image

# 初期化
def initImage(filePath):

    pass;

# テキストファイルを一文字ずつ読み込む
def readChar(filePath):
    pass;

# 読み込んだ文字からピクセルデータを決定する
def determinePxColor(char):
    pass;

# PNGファイルを出力する
def applyPxColor(color):
    pass;

if __name__ == '__main__':
    print 'Hello!';
    # 引数からテキストファイルのパスを得る
    argv = sys.argv;
    if len(argv) == 2:
        filePath = argv[1];
        readChar(filePath);

    print 'Done!';
