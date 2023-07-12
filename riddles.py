
"""DILARANG UNTUK MEMPERJUAL BELIKAN SCRIPT INI TANPA IZIN
    Copyright (C) Sreetx Allright Reserved"""

try:
    import zipfile, sys, os, time, glob, time
except ImportError:
    print(' [!] Kamu tidak memiliki module zipfile. Module akan diinstall secara otomatis')
    os.system('pip install zipfile')
try:
    from tqdm import tqdm
except ImportError:
    print(' [!] Kamu tidak memiliki module tqdm. Module akan diinstall secara otomatis')
    os.system('pip install tqdm')
    
if sys.platform in ["linux", "linux2"]:
    oyen = "\033[33m"
    norml = "\033[39m"
    putih = "\033[97m"
    hju = "\033[92m"
    kuning = "\033[93m"
    merah = "\033[91m"
else:
    oyen = ""
    norml = ""
    putih = ""
    hju = ""
    kuning = ""
    merah = ""

os.system('cls||clear')

banner = oyen+'''
 #===============================================================#
 <|=========================|'''+putih+''' Riddles'''+oyen+''' |=========================|>
  | '''+putih+'''Author:            RX77E, Security Syber Team Indonesian'''+oyen+'''    |
  | '''+putih+'''Spesial Thank's:   RX77E '''+oyen+'''                                   |
  | '''+putih+'''Github:            https://github.com/Sreetx  '''+oyen+'''              |
  | '''+putih+'''Instagram:         https://www.instagram.com/memelucubikin  '''+oyen+'''|
  |'''+putih+''' Blog:              https://postingan4ku.blogspot.com '''+oyen+'''       |
  | '''+putih+'''Version:           3.16.4.#Stable         '''+oyen+'''                  |
  +=============================================================+
  |'''+putih+'''Gunakan ini untuk membobol file zip anda jika anda lupa sandi'''+oyen+'''|
 <|=============================================================|>
 #===============================================================#
 '''+norml

try:
    print(banner)
    f = input(hju+' [?] Masukkan lokasi file zip anda: ')
    tebak = input(' [?] Masukkan lokasi file wordlist anda: ')
    print(kuning+' [INFO] Jika proses penebakan berhenti, itu artinya script menemukan kata yang tepat dan script mencoba untuk mengekstrak file tersebut'+norml)
    try:
        z = zipfile.ZipFile(f)
    except:
        print(merah+'\n [!] Terdeteksi bukan file zip atau anda salah memasukkan path. Koreksi penulisan path'+norml);sys.exit()
    try:
        j = len(list(open(tebak, 'rb')))
    except:
        print(merah+'\n [!] Alamat wordlist yang anda masukan salah, wordlist tidak tersedia. Harap perhatikan penulisan alamat wordlist'+putih);sys.exit()

    os.system('mkdir hasil')
    print(hijau+' [*] Jumlah kata yang akan dicek:'+merah, j)
    with open(tebak, 'rb') as to:
        for p in tqdm(to, total=j, unit='p'):
            try:
                s = z.extractall('hasil', pwd=p.strip())
            except KeyboardInterrupt: print(merah+'\n [!] Membatalkan....'+norml);sys.exit()
            except RuntimeError: continue
            else:
                print('\n')
                print(kuning+'\a [+] Password ditemukan:'+merah, p.decode().strip())
                print(kuning+'\n\a [+] File berhasil diekstrak')
                print(' [*] Terima kasih karena telah menggunakan script kami')
                print(merah+' [*] Keluar dari program....'+norml); sys.exit()
        
    print(merah+' [!] Password tidak ditemukan, silakan tambahkan kata baru pada wordlist anda'+norml)
except (KeyboardInterrupt, EOFError): print(merah+'\n [!] CTRL+C Terdeteksi, keluar dari program....'+norml);sys.exit()