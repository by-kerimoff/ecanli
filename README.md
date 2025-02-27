# Stream Token Generator

Bu Python skripti URL-dəki tokeni dəyişdirir və yenilənmiş `.m3u` faylı yaradır. URL-dəki tokeni dəyişdirmək və yeni kanal URL-ləri yaratmaq üçün istifadə edilə bilər.

## Təsvir
Bu skript, URL-dəki tokeni avtomatik olaraq tapır, onu dəyişdirir və nəticəni `.m3u` faylı olaraq saxlayır. Yeni token əlavə etmək üçün xüsusi bir məntiq yazılmalıdır (məsələn, bir API vasitəsilə).

## Necə İşləyir
1. **`get_new_token(url)`** funksiyası, verilmiş URL-dəki tokeni ayırır.
2. **`create_m3u(new_url)`** funksiyası isə dəyişdirilmiş URL ilə yeni `.m3u` faylı yaradır.
3. Skript işlədikdən sonra `new_channel.m3u` adlı yeni fayl yaradılır.

## İstifadə
Bu skripti istifadə etmək üçün aşağıdakı addımları izləyin:

1. Python 3.x quraşdırıldığından əmin olun. Əgər Python yoxdursa, [buradan Python-u yükləyin](https://www.python.org/downloads/).
   
2. **Kitabxanaları quraşdırın:**
   Bu skript `requests` kitabxanasını istifadə edir. Onu aşağıdakı əmrlə quraşdıra bilərsiniz:
   
   ```bash
   pip install requests
