#-*- coding:utf-8 -*-
import cv2
import numpy as np

def main():
    #  動画のキャプチャ
    cap = cv2.VideoCapture("input.mp4")
    
    #  動画終了まで繰り返し
    while(cap.isOpened()):
    
        #  フレームを取得
        ret, frame = cap.read()
        
        #  フレームを表示
        cv2.imshow("Flame", frame)
        
        # q キーが押されたら終了
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()
    
    
if __name__ == "__main__":
    main()