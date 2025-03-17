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
