import requests
import re
import time

# Yeni tkn tokenini əldə etmək üçün funksiyanı yazırıq
def get_new_token():
    # Bu yeri dəyişdirin, tokeni əldə etməyin yolunu burda əlavə edin
    # Burada tokenin sadə dəyişdirilməsi ilə nümunə göstəririk
    new_token = "w-2tS11TT7LOKrVVrqjN1A"  # Yeni token dəyəri
    return new_token

# Kanalın URL-i
channel_url = "https://ecanlitv3.etvserver.com/xazartv.m3u8?tkn=w-2tS11TT7LOKrVVrqjN1A&tms=1740634801"

# Yeni tkn tokenini əldə et
new_token = get_new_token()

# Yeni URL yaradılır
new_url = re.sub(r'tkn=[^&]+', f'tkn={new_token}', channel_url)

# Yeni M3U faylına əlavə edirik
M3U_FILE = "playlist.m3u"

# M3U playlist faylını yeniləyirik
with open(M3U_FILE, "w", encoding="utf-8") as m3u:
    m3u.write("#EXTM3U\n")
    
    # Yeni kanal məlumatını əlavə edirik
    m3u.write("#EXTINF:-1, Xazartv\n")
    m3u.write(f"{new_url}\n")

print(f"✅ M3U playlist yeniləndi: {M3U_FILE}")
