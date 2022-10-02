import cv2
import numpy as np
import time 
cascade = cv2.CascadeClassifier("C:\\XXXX.xml")#用いるデータのパス
cap = cv2.VideoCapture(0)
while True:

    ret,frame = cap.read()
    facerect = cascade.detectMultiScale(frame)
    print('検出人数: {}'.format(len(facerect)))
    for rect in facerect:
        cv2.rectangle(frame, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), (255,255,255), thickness=2) # 引数　rectangle(画像データ、検出した物を囲う四角の左頂点の座標、検出した物を囲う四角の右下頂点の座標、四角の色、四角の厚さ)
    
        if len(facerect) > 0: #facerectに入った要素数が0以上の時(物体を認識できたとき)
            print("x座標" + str((rect[0]+rect[2])/2)) #検出した物体の中心のx座標
            print("y座標" + str((rect[1]+rect[3])/2)) #検出した物体の中心のy座標

    cv2.imshow("Camera",frame)
    if cv2.waitKey(25) & 0xFF == ord('q') or len(facerect) == 0:
        break

cap.release()
cv2.destroyAllWindows()