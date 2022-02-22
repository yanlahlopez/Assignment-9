import cv2
from pyzbar.pyzbar import decode
from datetime import datetime
import webbrowser

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
now = datetime.now()
time = now.strftime("%H:%M:%S")
date = now.date()

while True:
    _, frame = cap.read()
    data, one, _ = detector.detectAndDecode(frame)
   
    if data: 
        a = data
        break

    for code in decode(frame): 
        qrdata = code.data.decode("utf-8")
        with open ('Contact Tracing Form.txt', 'w') as txtfile:
            txtfile.write(qrdata + (f'\nDate: {date}\nTime: {time}'))

    cv2.imshow('Contact Tracing Form', frame)
    if cv2.waitKey(1)==ord('q'):
        break

b = webbrowser.open(str(a))
cap.release(a)
cv2.destroyAllWindows()