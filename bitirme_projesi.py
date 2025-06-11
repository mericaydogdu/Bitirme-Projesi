import cv2

# Haar Cascade modeli yükleniyor
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Kamera başlatılıyor
cap = cv2.VideoCapture(0)

# Tam ekran pencere oluşturuluyor
cv2.namedWindow("Yüz Bulanıklaştırma", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Yüz Bulanıklaştırma", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    # Kameradan kare alınıyor
    ret, frame = cap.read()
    if not ret:
        print("Kamera açılamadı!")
        break


# Ayna görüntüsü veriliyor
    frame = cv2.flip(frame, 1)

# Griye çevriliyor  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüz tespiti yapılıyor
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # tespit edilen yüzler bulanıklaştırılıyor
    for (x, y, w, h) in faces:
        
        face_roi = frame[y:y+h, x:x+w]
        
        blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 30)
        
        frame[y:y+h, x:x+w] = blurred_face

    # Sonuç
    cv2.imshow("Yüz Bulanıklaştırma", frame)

    # döngüden çık
    if cv2.waitKey(1) != -1:
        break


cap.release()
cv2.destroyAllWindows()









