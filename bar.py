# -*- coding: utf-8 -*-
# Project pxchar

import sys
import os.path
from PIL import Image

# バージョンは一文字で表す
VERSION = '0';

# color辞書（とりあえず決め打ち）
# 外出ししたい
COLORS = {
    # pxchar制御文字
    "??": (255, 255, 255),   # 不明な文字
    "<" : (0, 0, 0),         # 終端文字
    ">" : (69,90,100),       # ファイル改行
    "%" : (255,235,59),
    # encodeURIComponentで変換されない記号
    # - _ . ! ~ * ' ( )
    "-": (209,196,233),
    "_": (179,157,219),
    ".": (126,87,194),
    "!": (197,202,233),
    "~": (159,168,218),
    "*": (121,134,203),
    "'": (187,222,251),
    "(": (144,202,249),
    ")": (100,181,246),
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

def determineFilename(filePath):
    # ファイルパスからファイル名を得る
    # 拡張子は含まない
    paths = filePath.split('/');
    filename = paths[len(paths) - 1];
    return filename.split('.')[0];

# 画像の基本情報を取得して返す
def get_img_info(path):
    img = Image.open(path)
    imgInfo = {
      "size_h": img.size[1],
      "size_w": img.size[0],
      "mode": img.mode,
      "format": img.format
    }
    return imgInfo

# 画像の色情報を二次元配列に保持する
def collect_px_rgb(path):
    img = Image.open(path)
    rgb = list(img.getdata())
    return rgb

# RGB情報を受け取って文字を決定する
def findChar(color):
    for key, value in COLORS.items():
        if color[0] == value[0] and color[1] == value[1] and color[2] == value[2]:
            return key;
    return '?'

# Pixelを1つずつ読み込む
def readPx(filepath):
    # 文字データを保持する配列
    chars = [''];

    # 有効なパスかどうか判定
    if os.path.isfile(filepath) is not True:
        return;

    filename = determineFilename(filePath);
    txtfilename = filename + '.txt';

    # 画像の横幅が一行あたりの文字数と一致する
    chars_per_line = get_img_info(filepath)['size_w'];
    rgb_data = collect_px_rgb(filepath);

    txt = '';
    # 画像の高さを一段ずつ見ていく
    step = 0;
    i = 0;
    char ='';
    while char != '\n':      # 終端文字ならば終了
        color = rgb_data[i];
        char = findChar(color);

        if char != '>':      # 改行ならばstepを進める
            # 先頭はバージョン情報なので不要
            if i == 0: char = '';
            # 終端文字に変換
            if char == '<':
                char = '\n';
            else:
                chars[step] = chars[step] + char;
        else:
            chars[step] = chars[step] + '\n';
            chars.append('');
            step += 1;
        i += 1;

    generateTxt(chars, txtfilename);

# 結果をテキストファイルに出力する
def generateTxt(strs, txtfilename):
    f = open('char/tmp/' + txtfilename, 'w');
    f.writelines(strs);
    f.close();

if __name__ == '__main__':
    print 'Hello!';
    # 引数からテキストファイルのパスを得る
    argv = sys.argv;
    if len(argv) == 2:
        filePath = argv[1];
        readPx(filePath);

    print 'Done!';
