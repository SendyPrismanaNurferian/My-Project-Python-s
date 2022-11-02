import cv2 
#Read image / camera/vido input
from pyzbar.pyzbar import decode
import time

#img = cv2.imread('QRCODE.png')
cap = cv2.VideoCapture(0)
cap.set(3, 640) #3 - width
cap.set(4, 480) #4 - height
used_codes = []

camera = True
while camera == True:
    success, frame = cap.read()

    for code in decode(frame):
        if code.data.decode('utf-8') not in used_codes:
            print('Terverifikasi silahkan tekan Enter!')
            print (code.data.decode('utf-8'))
            used_codes.append(code.data.decode('utf-8'))
            time.sleep(5)
        elif code.data.decode('utf-8') in used_codes:
            print('Maaf QR code ini tidak bisa digunakan kembali!')
            time.sleep(5)
        else:
            pass    

    cv2.imshow('Testing-code-scan', frame)

    #Untuk keluar dari program
    key = cv2.waitKey(1)
    if key == ord('q'):
        break