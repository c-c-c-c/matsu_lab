#-*- coding:utf-8 -*-
import cv2
import numpy as np

def main():
    #  入力画像の読み込み
    img = cv2.imread("input.jpg")
    #  方法 2(OpenCV で実装 )       
    hsv2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #  結果を出力
    cv2.imwrite("hsv2.jpg", hsv2)
    
    
if __name__ == "__main__":
    main()