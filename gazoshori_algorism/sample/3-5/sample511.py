#-*- coding:utf-8 -*-
import cv2
import numpy as np
    

def main():

    #  入力画像をグレースケールで読み込み
    gray = cv2.imread("input.jpg", 0)
    
    #  「ガウシアン」フィルタ処理   
    gaussian = cv2.GaussianBlur(gray, ksize=(3,3), sigmaX=1.3)

    #  「ラプラシアン」フィルタ処理
    laplacian = cv2.Laplacian(gray, cv2.CV_32F, ksize=3)

    #  「メディアン」フィルタ処理
    median = cv2.medianBlur(gray, ksize=3)
    sobel = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)

    #  結果を出力
    cv2.imwrite("gaussian.jpg", gaussian)
    cv2.imwrite("laplacian.jpg", laplacian)
    cv2.imwrite("median.jpg", median)
    cv2.imwrite("sobel.jpg", sobel)
    

if __name__ == "__main__":
    main()