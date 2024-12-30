import cv2
import face_recognition

def capture_face():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    print("Silakan posisikan wajah Anda di depan kamera. Tekan 'q' untuk menangkap.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow("Verifikasi Wajah", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("database/captured_face.jpg", frame)
            break
    
    cap.release()
    cv2.destroyAllWindows()

known_face_path = r"D:\UAS_NLP\database\known_face.jpg"
captured_face_path = r"D:\UAS_NLP\database\captured_face.jpg"

def verify_face(known_face_path, captured_face_path):
    known_image = face_recognition.load_image_file(known_face_path)
    captured_image = face_recognition.load_image_file(captured_face_path)
    known_encoding = face_recognition.face_encodings(known_image)[0]
    captured_encoding = face_recognition.face_encodings(captured_image)[0]
    return face_recognition.compare_faces([known_encoding], captured_encoding)[0]
