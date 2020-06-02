#-*- coding:utf-8 -*-
import cv2
import numpy as np


def main():
    #  入力画像を読み込み
    img = cv2.imread("input.jpg")

    #  グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    #  Cannyアルゴリズム処理
    edge2 = cv2.Canny(gray, 100, 200)

    #  結果を出力
    cv2.imwrite("output2.jpg", edge2)
    
    
if __name__ == "__main__":
    main()