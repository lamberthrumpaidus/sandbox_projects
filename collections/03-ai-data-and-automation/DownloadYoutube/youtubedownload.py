import yt_dlp


def download_video(url, format_choice):
    ydl_opts = {
        'format': format_choice,
        'noplaylist': True,
        'outtmpl': '%(title)s.%(ext)s',  # Menentukan nama file output
        'verbose': True,
    }

    if format_choice == 'bestaudio/best':  # Audio MP3
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print("Video atau audio berhasil diunduh!")
        except Exception as e:
            print("Terjadi kesalahan:", e)


if __name__ == "__main__":
    url = input("Masukkan URL video YouTube: ")
    print("Pilih format:")
    print("1. Video 4K (2160p)")
    print("2. Video 2K (1440p)")
    print("3. Video 1080p")
    print("4. Video 720p")
    print("5. Video 480p")
    print("6. Video 360p")
    print("7. Audio (mp3)")

    choice = input("Masukkan pilihan (1/2/3/4/5/6/7/8): ")

    if choice == '1':
        format_choice = 'best[ext=mp4][height<=2160]'  # Video 4K
    elif choice == '2':
        format_choice = 'best[ext=mp4][height<=1440]'  # Video 2K
    elif choice == '3':
        format_choice = 'best[ext=mp4][height<=1080]'  # Video 1080p
    elif choice == '4':
        format_choice = 'best[ext=mp4][height<=720]'  # Video 720p
    elif choice == '5':
        format_choice = 'best[ext=mp4][height<=480]'  # Video 480p
    elif choice == '6':
        format_choice = 'best[ext=mp4][height<=360]'  # Video 360p
    elif choice == '7':
        format_choice = 'bestaudio/best'  # Mengunduh audio terbaik
    else:
        print("Pilihan tidak valid.")
        exit()

    download_video(url, format_choice)
