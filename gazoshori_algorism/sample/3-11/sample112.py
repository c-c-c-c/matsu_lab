# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main():
    #  動画のキャプチャ
    cap = cv2.VideoCapture("input2.mp4")
    
    # Shi-Tomasi 法のパラメータ（コーナー検出用）
    ft_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)
    
    # Lucas-Kanade 法のパラメータ（追跡用）
    lk_params = dict(winSize=(15,15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
    
    #  最初のフレームを取得
    ret, frame = cap.read()
    gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #  グレースケール変換
    ft1 = cv2.goodFeaturesToTrack(gray1, mask = None, **ft_params) # Shi-Tomasi 法で特徴点の検出
    mask = np.zeros_like(frame) # mask 用の配列を生成
    
    while(cap.isOpened()):
        #  グレースケールに変換
        gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Lucas-Kanade 法で「オプティカル・フロー」の検出
        ft2, status, err = cv2.calcOpticalFlowPyrLK(gray1, gray2, ft1, None, **lk_params)
        
        #  「オプティカル・フロー」を検出した特徴点を取得（ 1 なら検出）
        good1 = ft1[status == 1]
        good2 = ft2[status == 1]
        
        #  特徴点と「オプティカル・フロー」をフレーム・マスクに描画
        for i, (pt2, pt1) in enumerate(zip(good2, good1)):
            x1, y1 = pt1.ravel()
            x2, y2 = pt2.ravel()
            mask = cv2.line(mask, (x2, y2), (x1, y1), [0, 0, 200], 2)
            frame = cv2.circle(frame, (x2, y2), 5,  [0, 0, 200], -1)
            
        #  フレームとマスクの論理積（合成）
        img = cv2.add(frame, mask)
        cv2.imshow('mask', img)        #  ウィンドウに表示
        
        #  次のフレーム、ポイントの準備
        gray1 = gray2.copy()
        ft1 = good2.reshape(-1, 1, 2)
        ret, frame = cap.read()
        
        # q キーが押されたら終了
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
            
    #  終了処理
    cv2.destroyAllWindows()
    cap.release()
    
    
if __name__ == "__main__":
    main()