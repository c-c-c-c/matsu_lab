#-*- coding:utf-8 -*-
import cv2
import numpy as np

def main():
    #  閾値
    t = 127
    
    #  入力画像の読み込み
    img = cv2.imread("input.jpg")
    
    #  グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    #  出力画像用の配列生成
    th1 = gray.copy()
    
    # 単純二値化処理
    th1[gray < t] = 0
    th1[gray >= t] = 255
    
    #  結果を出力
    cv2.imwrite("th1.jpg", th1)
    
    
if __name__ == "__main__":
    main()