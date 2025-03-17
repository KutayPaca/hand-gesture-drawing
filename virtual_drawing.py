import cv2
import numpy as np
import mediapipe as mp

print("MediaPipe hands initialized successfully.")

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
draw_color = (255, 255, 255)  #çizme rengi
erase_color = (0, 0, 0)        #silme rengi

# webcam çağırma
cap = cv2.VideoCapture(0)

# numpy ile siyah canva
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

# ilk x, y koordinat
prev_x, prev_y = 0, 0
drawing = False  

# çizme fonksiyonu
def draw_line(canvas, start, end, color, thickness=4):
    cv2.line(canvas, start, end, color, thickness)

# silme fonksiyonu
def erase_area(canvas, center, radius, color):
    cv2.circle(canvas, center, radius, color, -1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # kamerayı yatay döndürme
    frame = cv2.flip(frame, 2)

    # cv BGA sından mediapipe RGB sine döndürme
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    # el konum işaretleri ekle
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            for id, lm in enumerate(hand_landmarks.landmark):
                # her el konum işareti için x,y koordinatı alma
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                    
                if id == 8:  
                    # çizzmek için parmak seçme (işaret parmağı)
                    if drawing and prev_x != 0 and prev_y != 0:
                        draw_line(canvas, (prev_x, prev_y), (cx, cy), draw_color)
                    prev_x, prev_y = cx, cy

                elif id == 4:  
                    # silmek için parmak seçme (baş parmağı)
                    if not drawing:
                        erase_area(canvas, (cx, cy), 20, erase_color)

    # kamera ve canvayı gösterme
    cv2.imshow('Frame', frame)
    cv2.imshow('Canvas', canvas)

    # çizme,silme ve çıkma için buton kontrolü
    key = cv2.waitKey(1) & 0xFF
    if key == ord('d'):
        drawing = True
    elif key == ord('e'):
        drawing = False
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
