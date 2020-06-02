# -*- coding: utf-8 -*-
import cv2
import numpy as np


def main():
    #  入力画像の読み込み
    img = cv2.imread("input.jpg")
    
    #  グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #  バイリニア補間で 2 倍に拡大
    dst2  =  cv2.resize(gray,  (gray.shape[1]*2,  gray.shape[0]*2), interpolation=cv2.INTER_LINEAR)
        
    #  結果を出力
    cv2.imwrite("output2.jpg", dst2)
    
    
if __name__ == "__main__":
    main()