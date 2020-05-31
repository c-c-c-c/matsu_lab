# -*- coding: utf-8 -*-
import cv2
import numpy as np

#  アフィン変換で画像配列の回転
def rotate_affine(src, theta, tx=0, ty=0):

    #  元画像のサイズを取得
    h, w = src.shape[0], src.shape[1]
    
    #  出力画像用の配列生成（要素は全て 0 ）
    dst = np.zeros((h,w))
    
    # degree かｒ radian に変換
    rd = np.radians(theta)
    
    #  アフィン変換
    for y in range(0, h):
        for x in range(0, w):
            xi = (x - tx)*np.cos(rd) - (y - ty)*np.sin(rd) + tx
            yi = (x - tx)*np.sin(rd) + (y - ty)*np.cos(rd) + ty
            xi = int(xi)
            yi = int(yi)
            #  変換後の座標が範囲外でなければ出力画像配列に画素値を代入
            if yi < h - 1 and xi < w -1 and yi > 0 and xi > 0:
                dst[y][x] = src[yi][xi]
    return dst
    
    
def main():
    #  入力画像の読み込み
    img = cv2.imread("input.png")
    
    #  グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    theta = 45 #  回転角
    
    #  画像の中心座標
    oy, ox = int(gray.shape[0]/2), int(gray.shape[1]/2)
    
    #  アフィン変換で回転
    dst = rotate_affine(gray, theta, ox, oy)
    
    #  結果を出力
    cv2.imwrite("output.png", dst)
    
    
if __name__ == "__main__":
    main()