#-*- coding:utf-8 -*-
import cv2
    
def main():
    #  入力画像の読み込み
    img = cv2.imread("input.jpg")
    
    #  グレースケール変換    
    gray2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    #  結果を出力
    cv2.imwrite("gray2.jpg", gray2)
    

if __name__ == "__main__":
    main()