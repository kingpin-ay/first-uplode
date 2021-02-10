import requests
import pytube
import moviepy.editor as mp
import os
from playsound import playsound
import urllib.parse
import urllib.request
import re



def playmusic(url):
    query_string = urllib.parse.urlencode({"search_query" : url})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'watch\?v=(\S{11})', html_content.read().decode())
    Url = "https://www.youtube.com/watch?v="+search_results[0]

    # link = "https://www.youtube.com/watch?v=di1VMRqROLg&list=RDMM&index=4&ab_channel=Chino"
    path = r"D:\Project\Python\Music\song"

    listItem = os.listdir(path=path)
    for item in listItem:
        os.chdir(path=path)
        os.unlink(item)


    try:
        # creating youtube object
        video_data = pytube.YouTube(Url)
        # Informing the use that the video link is founded
        print("SONG FOUNDED..")

    except:
        # Exception Handleing 
        print("Error 1 - Not able to create the youtube object")


    # Streams data extraction
    # Testing Element  ---->>  print(video_data.streams)

    all_streams = video_data.streams.filter(type="video",progressive="False")
    # Downloading the video from the list of streams
    # Testing Element --->  print(all_streams)
    File = all_streams.get_lowest_resolution().download(output_path=r'D:\Project\Python\Music\song',filename='Song')
    # converting the video into audio 
    # video_path = r'D:\Project\Python\Music\song\Song.mp4'
    # music_path = r'D:\Project\Python\Music\song\Song.mp3'

    # basePath = os.path.splitext(File)
    video = mp.VideoFileClip(os.path.join("Song.mp4"))
    video.audio.write_audiofile(os.path.join("Song.mp3"))
    video.close()

    # Playing the music with playsound module 
    # playsound(music_path)
    os.chdir(r'D:\Project\Python\Music\song')
    os.system("mpg123 " + "Song.mp3")


while True:
    link = str(input("Please enter your song name :  "))
    playmusic(link)
