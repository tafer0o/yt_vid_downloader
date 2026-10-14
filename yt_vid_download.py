
import yt_dlp


def download_yt_video(url):
    ydl_opts = {
        'format': 'bestvideo*+bestaudio/best',
        'noplaylist': True,
        'outtmpl': '%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed!")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ").strip()
    download_yt_video(url)
