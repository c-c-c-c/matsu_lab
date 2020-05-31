#-*- coding:utf-8 -*-
import cv2
import numpy as np

def main():
    #  画像の読み込み (RGB)
    img = cv2.imread("input.png")
    height, width, ch = img.shape
    
    #  画素数  =  幅  *  高さ
    size = width * height
    
    #  情報表示
    print(" 幅： ", width)
    print(" 高さ： ", height)
    print(" チャンネル数 :", ch)
    print(" 画素数 :", size)   
    print(" データ型： ", img.dtype)
    print("B の画素値： ¥n", img[0])
    print("G の画素値： ¥n", img[1])
    print("R の画素値： ¥n", img[2])


if __name__ == "__main__":
    main()