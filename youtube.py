import youtube_dl
import os
from pytube import YouTube


channel_name = '@RyanCelsiusMusic' # input("Введите название YouTube канала: ")
video_count = input("Сколько видео скачать ?: ")
channel_url = "https://www.youtube.com/" + channel_name + "/videos"
local_path = '/Users/nikolajtukmaceva/Desktop/'+ channel_name

def get_channel_videos(channel_url):
    video_dict = {}

    ydl_opts = {
        'ignoreerrors': True,
        'extract_flat': 'in_playlist',
        'dump_single_json': True,
        'playlistend': int(video_count),
        'quiet': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(channel_url, download=False)
            if 'entries' in info:
                playlist = info['entries']
                for video in playlist:
                    title = video['title']
                    url = video['url']
                    video_dict[title] = url
        except youtube_dl.utils.DownloadError:
            pass
    return video_dict

def download_video(vide_date):
    counter = 0
    for title, url in video_dict.items():
        video_url = 'https://www.youtube.com/watch?v=' + url
        title = title + '.mp4'
        file_path = local_path + '/' + title

        if not os.path.exists(local_path):
            os.makedirs(local_path)
            
        current_video_name = os.listdir(local_path)

        if title in current_video_name:
            print(" Видео уже загружено: ", title)
        else:
            try:
                yt = YouTube(video_url, use_oauth=True, allow_oauth_cache=True)
                video = yt.streams.filter(file_extension='mp4').get_highest_resolution()
                title = yt.title + '.mp4'
                print("Загрузка видео: " + title)
                video.download(local_path, filename=title)
            except Exception as e:
                print("Error:", e)
                continue
    print("Загрузка завершена: ")


video_dict = get_channel_videos(channel_url)
download_video(video_dict)
