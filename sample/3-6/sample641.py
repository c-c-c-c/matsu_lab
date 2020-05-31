#-*- coding:utf-8 -*-
import cv2
import numpy as np

def main():
    #  入力画像を読み込み
    img = cv2.imread("input.png")
    
    #  グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    #  二値化処理
    gray[gray<127] = 0
    gray[gray>=127] = 255
    
    # 8 近傍で処理
    kernel = np.array([[1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1]], np.uint8)
                       
    # 膨張処理
    dilate = cv2.dilate(gray, kernel)
    
    # 収縮処理
    erode = cv2.erode(dilate, kernel)
    
    #  結果を出力
    cv2.imwrite("dilate.jpg", dilate)
    cv2.imwrite("erode.jpg", erode)
    
if __name__ == "__main__":
    main()