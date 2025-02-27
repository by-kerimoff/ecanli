import requests
import re

# Kanal URL-i və yeni token
channel_url = "https://ecanlitv3.etvserver.com/xazartv.m3u8?tkn=w-2tS11TT7LOKrVVrqjN1A&tms=1740634801"
new_token = "w-2tS11TT7LOKrVVrqjN1A"  # Yeni token

# URL-i yeniləyirik
new_url = re.sub(r'tkn=[^&]+', f'tkn={new_token}', channel_url)

# M3U playlist faylına əlavə edirik
M3U_FILE = "playlist.m3u"

# M3U faylını yazırıq
with open(M3U_FILE, "w", encoding="utf-8") as m3u:
    m3u.write("#EXTM3U\n")
    m3u.write("#EXTINF:-1, Xazartv\n")  # Kanal adı əlavə edilir
    m3u.write(f"{new_url}\n")  # Yenilənmiş URL

print(f"✅ M3U playlist yeniləndi: {M3U_FILE}")
