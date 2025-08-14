# Hand Gesture Drawing and Erasing Application Using MediaPipe

This project implements a hand gesture-based drawing and erasing application using MediaPipe, OpenCV, and NumPy.  
The application allows users to draw and erase on a virtual canvas in real-time using hand movements captured through a webcam.

## Features:
- **Real-Time Hand Gesture Detection:** Hand landmarks and movements are detected using MediaPipe's hand tracking feature.  
- **Drawing Mode:** Users can draw on the canvas by moving their index finger (landmark 8) while holding the `d` key.  
- **Erasing Mode:** Users can erase areas on the canvas by moving their thumb (landmark 4) while holding the `e` key.  
- **Interactive Canvas:** The canvas updates dynamically according to user movements, providing an interactive drawing experience.  
- **Webcam Integration:** The application captures real-time video from a webcam and processes it to detect hand movements.

## How It Works:
1. **Webcam Capture:** Video stream is captured using OpenCV.  
2. **Hand Detection:** MediaPipe detects the position and landmarks of each hand.  
3. **Drawing Mode:** When the index finger (landmark 8) moves, the `draw_line` function draws lines on the canvas.  
4. **Erasing Mode:** When the thumb (landmark 4) moves, the `erase_area` function erases areas on the canvas.  
5. **User Interaction:** Users can switch between drawing and erasing modes using the `d` and `e` keys, and press `q` to quit the application.

## Requirements:
- Python 3.x  
- OpenCV  
- MediaPipe  
- NumPy


# MediaPipe Kullanarak El Hareketiyle Çizim ve Silme Uygulaması
Bu proje, MediaPipe, OpenCV ve NumPy kullanarak bir el hareketiyle çizim ve silme uygulaması gerçekleştirir.
Uygulama, kullanıcıların web kamerası aracılığıyla gerçek zamanlı olarak el hareketleri ile sanal bir tuvalde çizim yapmalarını ve silmelerini sağlar.

## Özellikler:
Gerçek Zamanlı El Hareketi Tespiti: MediaPipe'ın el izleme özelliği kullanılarak el işaretçileri ve hareketler tespit edilir.
Çizim Modu: Kullanıcılar, işaret parmaklarını (8 numaralı işaretçi) hareket ettirerek 'd' tuşuna basılı tutarken tuval üzerinde çizim yapabilir.
Silme Modu: Kullanıcılar, baş parmaklarını (4 numaralı işaretçi) hareket ettirerek 'e' tuşuna basılı tutarken tuvaldeki alanları silebilir.
Etkileşimli Tuval: Tuval, kullanıcı hareketlerine göre dinamik olarak güncellenir ve etkileşimli bir çizim deneyimi sunar.
Web Kamera Entegrasyonu: Uygulama, web kamerasından gerçek zamanlı video alır ve video akışını işleyerek el hareketlerini tespit eder.

## Nasıl Çalışır:
Web Kamera Kaydı: OpenCV kullanılarak web kamerasından video akışı alınır.
El Tespiti: MediaPipe, her bir elin konumunu ve işaretçilerini tespit eder.
Çizim Modu: İşaret parmağı (8 numaralı işaretçi) hareket ettiğinde, draw_line fonksiyonu kullanılarak tuval üzerine çizgi çizilir.
Silme Modu: Baş parmak (4 numaralı işaretçi) hareket ettiğinde, erase_area fonksiyonu ile tuvaldeki alanlar silinir.
Kullanıcı Etkileşimi: Kullanıcılar 'd' ve 'e' tuşlarına basarak çizim ve silme modları arasında geçiş yapabilir. 'q' tuşuna basarak uygulamadan çıkabilirler.

## Gereksinimler:
Python 3.x
OpenCV
MediaPipe
NumPy
