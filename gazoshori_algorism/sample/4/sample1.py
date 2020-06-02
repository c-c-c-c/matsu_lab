# -*- coding: utf-8 -*-
import cv2
import numpy as np

#  漫画化フィルタ
def manga_filter(src, screen, th1=60, th2=150):

    #  グレースケール変換
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    
    #  スクリーントーン画像を入力画像と同じ大きさにリサイズ
    screen = cv2.resize(screen,(gray.shape[1],gray.shape[0]))
    
    # Canny アルゴリズムで輪郭検出し、色反転
    edge = 255 - cv2.Canny(gray, 80, 120)
    
    #  三値化
    gray[gray <= th1] = 0
    gray[gray >= th2] = 255
    gray[ np.where((gray > th1) & (gray < th2)) ] = screen[ np.where((gray > th1)&(gray < th2)) ]
    
    #  三値画像と輪郭画像を合成
    return cv2.bitwise_and(gray, edge)
    
    
def main():
    #  カメラのキャプチャ
    cap = cv2.VideoCapture(0)
    
    #  スクリーントーン画像の読み込み
    screen = cv2.imread("screen.jpg")
    
    #  動画終了まで繰り返し
    while(cap.isOpened()):
    
        #  フレームを取得
        ret, frame = cap.read()
        
        #  漫画化フィルタ処理
        manga = manga_filter(frame, screen, 60, 150)
        
        #  フレームを表示
        cv2.imshow("input", frame)
        cv2.imshow("Flame", manga)
        
        # q キーが押されたら途中終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()
    
    
if __name__ == '__main__':
    main()