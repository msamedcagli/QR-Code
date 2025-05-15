import qrcode
import os
import uuid  # Benzersiz ID oluşturmak için

# 1. Kullanıcıdan QR koduna dönüştürülecek linki al
data = input("QR koduna dönüştürmek istediğiniz bağlantıyı girin: ")

# 2. QR kodunu oluştur
img = qrcode.make(data)

# 3. Kaydedilecek klasörü belirt
save_folder = input("QR kodunun kaydedileceği klasör yolunu girin (örneğin: C:/Users/username/Desktop): ")

# 4. Klasör var mı kontrol et, yoksa oluştur
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 5. Benzersiz ID oluştur
unique_id = uuid.uuid4().hex  # Örn: '3f9f1a6a8c984aa49f44760dcaaf50c2'

# 6. Kaydedilecek dosya adı ve yolu
file_name = f"qr_code_{unique_id}.png"
file_path = os.path.join(save_folder, file_name)

# 7. QR kodunu kaydet
img.save(file_path)

print(f"QR kod başarıyla kaydedildi: {file_path}")
