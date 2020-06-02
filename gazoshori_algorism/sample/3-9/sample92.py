# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt

def lowpass_ﬁlter(src, a = 0.5):
    #  高速フーリエ変換 (2 次元 )
    src = np.fft.fft2(src)
    
    #  画像サイズ
    h, w = src.shape
   
    #  画像の中心座標
    cy, cx =  int(h/2), int(w/2)
    
    #  フィルタのサイズ ( 矩形の高さと幅 )
    rh, rw = int(a*cy), int(a*cx)

    #  第 1 象限と第 3 象限、第 1 象限と第 4 象限を入れ替え
    fsrc =  np.fft.fftshift(src)  

    #  入力画像と同じサイズで値 0 の配列を生成
    fdst = np.zeros(src.shape, dtype=complex)

    #  中心部分の値だけ代入（中心部分以外は 0 のまま）
    fdst[cy-rh:cy+rh, cx-rw:cx+rw] = fsrc[cy-rh:cy+rh, cx-rw:cx+rw]
    
    #  第 1 象限と第 3 象限、第 1 象限と第 4 象限を入れ替え ( 元に戻す )
    fdst =  np.fft.fftshift(fdst)

    #  高速逆フーリエ変換  
    dst = np.fft.ifft2(fdst)
   
    #  実部の値のみを取り出し、符号なし整数型に変換して返す
    return  np.uint8(dst.real)
    
    
def main():
    #  入力画像を読み込み
    img = cv2.imread("input2.png")
    
    #  グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    #  ローパスフィルタ処理
    himg = lowpass_ﬁlter(gray, 0.3)
    
    #  処理結果を出力
    cv2.imwrite("output.png", himg)
    
if __name__ == "__main__":
    main()