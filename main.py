import pandas as pd
import threading
from multiprocessing import Process
import cv2
from s3upload import *

excel_data = pd.read_excel('cameraDetails.xlsx')

#rtspUrl = rtsp://nrisiva:Pharmacy@174.71.184.108:7001/fe2d4963-502d-e7df-6973-73d53dfc961a?stream=1
cameraId = list(excel_data['cameraId'])
cameraUrl = list(excel_data['cameraUrl'])
rtspUrlList = []
fps = list(excel_data['fps'])
width = list(excel_data['width'])
height = list(excel_data['height'])
for i in cameraUrl:
    rtspUrlList.append(cameraUrl)
# print(rtspUrlList)
def run(camUrl,camId,fps,width,height):

    cap = cv2.VideoCapture(camUrl)
    # fps = cap.get(cv2.CAP_PROP_FPS)
    print(camId,fps)
    framecount = 0
    while True:
        ret, frame = cap.read()

        if ret is False or frame is None:
            break
        framecount = framecount + 1

        if framecount == fps:
            framecount = 0
            # cv2.imshow("Frame", frame)
            frame = cv2.resize(frame, (width,height))
            cv2.imwrite(str(camId)+".png", frame)
            uploadImage(camId)

            key = cv2.waitKey(1)
            if key == 27:
                break

    cap.release()
    cv2.destroyAllWindows()


def run1():
    if __name__ == '__main__':
        for i in range(len(rtspUrlList)):
            p = Process(target=run,args=(rtspUrlList[0][i],cameraId[i],fps[i],width[i],height[i]))
            p.start()
run1()
