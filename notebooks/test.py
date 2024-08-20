from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=INjiWW3c4QQ')
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()