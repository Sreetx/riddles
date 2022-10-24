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
    
os.system('cls||clear')

banner = '''
 #----------------------------------------------------------------#
 <|-------------------------| Riddles |--------------------------|>
  | Author:             RX77E, Security Syber Team Indonesian    |
  | Spesial Thank's:    RX77E                                    |
  | Github:             https://github.com/Sreetx                |
  | Instagram:          https://www.instagram.com/memelucubikin  |
  | Blog:               https://postingan4ku.blogspot.com        |
  |--------------------------------------------------------------|
  | Gunakan ini untuk membobol file zip anda jika anda lupa sandi|
 <|--------------------------------------------------------------|>
 #----------------------------------------------------------------#
 '''

try:
    print(banner)
    f = input(' [?] Masukkan lokasi file zip anda: ')
    tebak = input(' [?] Masukkan lokasi file wordlist anda: ')
    print(' [INFO] Jika proses penebakan berhenti, itu artinya script menemukan kata yang tepat dan script mencoba untuk mengekstrak file tersebut')
    try:
        z = zipfile.ZipFile(f)
    except:
        print('\n [!] Terdeteksi bukan file zip atau anda salah memasukan path, harap dikoreksi. operasi dibatalkan');sys.exit()
    try:
        j = len(list(open(tebak, 'rb')))
    except:
        print('\n [!] Alamat wordlist yang anda masukan salah, wordlist tidak tersedia. Harap perhatikan penulisan alamat wordlist');sys.exit()

    os.system('mkdir hasil')
    print(' [*] Jumlah kata yang akan dicek:', j)

    with open(tebak, 'rb') as to:
        for p in tqdm(to, total=j, unit='p'):
            try:
                s = z.extractall('hasil', pwd=p.strip())
            except:
                continue
            else:
                print('\n')
                print('\a [+] Password ditemukan:', p.decode().strip())
                print('\n\a [+] File berhasil diekstrak')
                print(' [*] Terima kasih karena telah menggunakan script kami')
                print(' [*] Keluar dari program....'); sys.exit()
        
    print(' [!] Password tidak ditemukan, silakan tambahkan kata baru pada wordlist anda')
except KeyboardInterrupt: print('\n [!] CTRL+C Terdeteksi, keluar dari program....')
except EOFError: print('\n [!] CTRL+C Terdeteksi, keluar dari program....')