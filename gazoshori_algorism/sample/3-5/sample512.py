#-*- coding:utf-8 -*-
import cv2
import numpy as np


def ﬁlter2d(src, kernel, fill_value=-1):
    #  カーネルサイズ
    m, n = kernel.shape
    
    #  畳み込み演算をしない領域の幅
    d = int((m-1)/2)
    h, w = src.shape[0], src.shape[1]
    
    #  出力画像用の配列
    if fill_value == -1: dst = src.copy()
    elif fill_value == 0: dst = np.zeros((h, w))
    else:
        dst = np.zeros((h, w))
        dst.ﬁll(fill_value)
        
    #  畳み込み演算
    for y in range(d, h - d):
        for x in range(d, w - d):
            dst[y][x] = np.sum(src[y-d:y+d+1, x-d:x+d+1]*kernel)
            
    return dst
  
    
def main():
    #  入力画像をグレースケールで読み込み
    gray = cv2.imread("input.jpg", 0)
    
    #  「ガウシアン」フィルタのカーネル
    kernel_g = np.array([[1/16, 1/8, 1/16],
                         [1/8,  1/4, 1/8],
                         [1/16, 1/8, 1/16]])
                         
    #  「ラプラシアン」フィルタのカーネル
    kernel_lp = np.array([[1, 1,  1],
                          [1, -8, 1],
                          [1, 1,  1]])
 
    #  「ガウシアン」フィルタでぼかし
    gaussian = filter2d(gray, kernel_g, -1)
    
    #  「ラプラシアン」フィルタで輪郭検出
    laplacian = filter2d(gray, kernel_lp, 0)  
    
    #  結果を出力
    cv2.imwrite("gaussian.jpg", gaussian)
    cv2.imwrite("laplacian.jpg", laplacian)
    
    
if __name__ == "__main__":
    main()