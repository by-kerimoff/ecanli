import requests
import re

channels = [
    {"name": "Xəzər TV", "url": "https://ecanlitv3.etvserver.com/xazartv.m3u8?tkn=KIDk0i9vVdOOSNzbYp1t_A&tms=1740638106", "slug": "xazartv"},
    # Digər kanallar burada əlavə edilə bilər
]

M3U_FILE = "playlist.m3u"

# Token-i yeniləyən funksiya
def get_new_token(link):
    # Bu yerdə token dəyişməsinin nə şəkildə olduğunu müəyyən etmək lazımdır.
    # Məsələn, müəyyən bir API-dən yeni token ala bilərik
    # Amma burada nümunə olaraq sadəcə tokeni dəyişirəm.
    new_token = "yeniTokenDəyəri"  # Burada yeni token-i təmin edin
    new_link = re.sub(r'tkn=[^&]+', f'tkn={new_token}', link)  # Eski tokeni yenisi ilə əvəz edir
    return new_link

def get_new_m3u8_link(channel_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    response = requests.get(channel_url, headers=headers)
    
    if response.status_code == 200:
        # Burada yeni M3U8 linki əldə edə bilərik
        return channel_url  # Yenilənmiş link
    else:
        print(f"❌ Xəta kodu: {response.status_code} | Kanal: {channel_url}")
        return None

with open(M3U_FILE, "w", encoding="utf-8") as m3u:
    m3u.write("#EXTM3U\n")
    
    for channel in channels:
        # Token-i dəyişirik
        updated_url = get_new_token(channel["url"])
        new_m3u8_link = get_new_m3u8_link(updated_url)
        
        if new_m3u8_link:
            m3u.write(f"#EXTINF:-1, {channel['name']}\n")
            m3u.write(f"{new_m3u8_link}\n")
        else:
            print(f"❌ Kanal linki yenilənmədi: {channel['name']}")

print(f"✅ M3U playlist yeniləndi: {M3U_FILE}")
