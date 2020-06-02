# -*- coding: utf-8 -*-
import cv2
import numpy as np

def anime_filter(img):
    #  グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    
    #  ぼかしでノイズ低減
    edge = cv2.blur(gray, (3, 3))
    
    # Canny アルゴリズムで輪郭抽出
    edge = cv2.Canny(edge, 50, 150, apertureSize=3) 
    
    #  輪郭画像を RGB 色空間に変換
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    
    #  画像の領域分割
    img = cv2.pyrMeanShiftFiltering(img, 5, 20)
    
    #  差分を返す
    return cv2.subtract(img, edge)
    
    
def main():
    #  入力画像の読み込み
    img = cv2.imread("input.jpg")
    
    #  画像のアニメ絵化
    anime = anime_filter(img)
    
    #  結果出力
    cv2.imwrite('anime.jpg', anime)
    
    
if __name__ == '__main__':
    main()