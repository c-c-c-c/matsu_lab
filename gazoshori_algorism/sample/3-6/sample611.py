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
    
    #  単純二値化処理     
    ret, th2 = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)  
      
    #  結果を出力
    cv2.imwrite("th2.jpg", th2)
    
    
if __name__ == "__main__":
    main()