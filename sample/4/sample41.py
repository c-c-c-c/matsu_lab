# -*- coding: utf-8 -*-
import cv2
import numpy as np
import time

def color_tracking(img):

    # HSV 色空間に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #  赤色の HSV の値域 1
    hsv_min = np.array([0,100,0])
    hsv_max = np.array([60,255,255])
    mask1 = cv2.inRange(hsv, hsv_min, hsv_max)
    
    #  赤色の HSV の値域 2
    hsv_min = np.array([160,100,0])
    hsv_max = np.array([255,255,255])
    mask2 = cv2.inRange(hsv, hsv_min, hsv_max)
    
    # 2 つのマスク画像を加算
    mask = mask1 + mask2
    
    #  膨張・収縮処理でノイズ低減
    kernel = np.ones((6, 6), np.uint8)
    mask = cv2.dilate(mask, kernel)
    mask = cv2.erode(mask, kernel)
    return mask
    
    
def calc_max_point(mask):
    if np.count_nonzero(mask) <= 0:
        return(-20, -20)
        
    #  ラベリング処理
    label = cv2.connectedComponentsWithStats(mask)
    
    #  ブロブ情報を項目別に抽出
    n = label[0] - 1
    data = np.delete(label[2], 0, 0)
    center = np.delete(label[3], 0, 0)  
    
    #  ブロブ面積が最大のインデックス
    max_index = np.argmax(data[:,4])
   
    #  最大面積をもつブロブの中心座標を返す
    return center[max_index]
    
    
def main():

    #  データ格納用のリスト
    data = []
    
    #  カメラのキャプチャ
    cap = cv2.VideoCapture(0)

    #  動画ファイルの読み込み
    #cap = cv2.VideoCapture("input.mp4")

    #  開始時間
    start = time.time()
    
    while(cap.isOpened()):
    
        #  フレームを取得
        ret, frame = cap.read()
        
        #  カラートラッキング（赤色）
        mask = color_tracking(frame)
        
        #  面積最大ブロブの中心座標 (x, y) を取得
        x, y = calc_max_point(mask)
        
        #  経過時間 , x, y をリストに追加
        data.append([time.time() - start, x, y])
        
        #  中心座標に赤丸を描く
        cv2.circle(frame, (int(x), int(y)), 20, (0, 0, 255), 10)
        
        #  ウィンドウ表示
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)
        
        # q キーが押されたら途中終了
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
            
    # CSV ファイルに保存
    np.savetxt("data.csv", np.array(data), delimiter=",")
    
    #  キャプチャ解放・ウィンドウ廃棄
    cap.release()
    cv2.destroyAllWindows()
    
    
if __name__ == '__main__':
    main()