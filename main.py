import re
import requests

def get_new_token(url):
    # URL-dən tokeni ayırırıq
    token_pattern = r'token=([a-zA-Z0-9\-]+)'
    match = re.search(token_pattern, url)
    if match:
        token = match.group(1)
        # Burada tokeni dəyişdirmək üçün yeni token əldə etmək funksiyası olmalıdır
        new_token = "yeni_token"  # Bu hissəni istədiyiniz yeni token ilə dəyişdirin
        # Tokeni dəyişdiririk
        new_url = url.replace(token, new_token)
        return new_url
    else:
        return None

def create_m3u(new_url):
    with open("new_channel.m3u", "w") as f:
        f.write("#EXTM3U\n")
        f.write("#EXTINF:-1, Yeni Kanal\n")
        f.write(new_url + "\n")
        
# Əvvəlki URL-i daxil edirik
old_url = "https://str.yodacdn.net/ictimai/tracks-v1a1/mono.ts.m3u8?token=104ca719e0399569043c15302ab129afb1d7e370-264b3bed0324abbee29655f6101cf29b-1740642099-1740631299"
new_url = get_new_token(old_url)
if new_url:
    create_m3u(new_url)
    print("Yeni kanal m3u faylı yaradıldı!")
else:
    print("Token tapılmadı!")
