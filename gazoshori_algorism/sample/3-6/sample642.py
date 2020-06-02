#-*- coding:utf-8 -*-
import cv2
import numpy as np

#  膨張処理
def dilate(src, ksize=3):
    h, w = src.shape
    dst = src.copy()
    d = int((ksize-1)/2)
    
    for y in range(0, h):
        for x in range(0, w):
            # 近傍に白色画素(255)が1つでもあれば白色に塗りつぶす
            if np.count_nonzero(src[y-d:y+d+1, x-d:x+d+1]) > 0:
                dst[y][x] = 255
    return dst
    
#  収縮処理
def erode(src, ksize=3):
    h, w = src.shape
    dst = src.copy()
    d = int((ksize-1)/2)
    
    for y in range(0, h):
        for x in range(0, w):
            # 近傍に黒色画素(0)が1つでもあれば黒色に塗りつぶす
            if np.count_nonzero(src[y-d:y+d+1, x-d:x+d+1]) < ksize**2:
                dst[y][x] = 0
    return dst
    
    
def main():
    #  入力画像を読み込み
    img = cv2.imread("input.png")
    
    #  グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    #  二値化処理
    gray[gray<127] = 0
    gray[gray>=127] = 255
    
    #  膨張・収縮処理
    dilate_img = dilate(gray, ksize=3)
    erode_img = erode(dilate_img, ksize=3)
    
    #  結果を出力
    cv2.imwrite("dilate.jpg", dilate_img)
    cv2.imwrite("erode.jpg", erode_img)
    
if __name__ == "__main__":
    main()