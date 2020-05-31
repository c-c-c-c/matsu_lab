#-*- coding:utf-8 -*-
import cv2
import numpy as np
   
    
def main():
    #  入力画像を読み込み
    img = cv2.imread("input.jpg")
    
    #  グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # 適応的二値化処理        
    dst2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
    
    #  結果を出力
    cv2.imwrite("output2.jpg", dst2)
    
    
if __name__ == "__main__":
    main()