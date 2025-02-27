import requests
import re

# Kanalların URL-ləri və adları
channels = [
    {
        "name": "İctimai TV", 
        "url": "https://str.yodacdn.net/ictimai/tracks-v1a1/mono.ts.m3u8?token=104ca719e0399569043c15302ab129afb1d7e370-264b3bed0324abbee29655f6101cf29b-1740642099-1740631299", 
        "slug": "ictimai"
    },
    # Digər kanallar əlavə edilə bilər
]

M3U_FILE = "playlist.m3u"

# Tokeni yeniləyən funksiya
def get_new_token(link):
    # Burada tokeni URL-dən çıxarıb yeniləyəcəyik
    new_token = "yeniTokenDəyəri"  # Burada yeni token-i təyin edin
    new_link = re.sub(r'token=[^&]+', f'token={new_token}', link)  # Eski tokeni yenisi ilə dəyişirik
    return new_link

def get_new_m3u8_link(channel_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    response = requests.get(channel_url, headers=headers)
    
    if response.status_code == 200:
        # Burada yeni M3U8 linki əldə edirik
        return channel_url  # Yenilənmiş link
    else:
        print(f"❌ Xəta kodu: {response.status_code} | Kanal: {channel_url}")
        return None

# Yeni M3U playlistini yaradacağıq
with open(M3U_FILE, "w", encoding="utf-8") as m3u:
    m3u.write("#EXTM3U\n")
    
    for channel in channels:
        # Tokeni yeniləyirik
        updated_url = get_new_token(channel["url"])
        new_m3u8_link = get_new_m3u8_link(updated_url)
        
        if new_m3u8_link:
            m3u.write(f"#EXTINF:-1, {channel['name']}\n")
            m3u.write(f"{new_m3u8_link}\n")
        else:
            print(f"❌ Kanal linki yenilənmədi: {channel['name']}")

print(f"✅ M3U playlist yeniləndi: {M3U_FILE}")
