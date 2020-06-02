# -*- coding: utf-8 -*-
import cv2
import numpy as np


def red_detect(img):
    # HSV 色空間に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #  赤色の HSV の値域 1
    hsv_min = np.array([0,128,0])
    hsv_max = np.array([30,255,255])
    mask1 = cv2.inRange(hsv, hsv_min, hsv_max)
    
    #  赤色の HSV の値域 2
    hsv_min = np.array([150,128,0])
    hsv_max = np.array([179,255,255])
    mask2 = cv2.inRange(hsv, hsv_min, hsv_max)
    
    return mask1 + mask2
    
def main():
    #  動画のキャプチャ
    cap = cv2.VideoCapture("input.mp4")
    
    while(cap.isOpened()):
        #  フレームを取得
        ret, frame = cap.read()
        #  赤色検出
        mask = red_detect(frame)
        #  結果表示
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)
        # q キーが押されたら終了
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()
    
    
if __name__ == '__main__':
    main()