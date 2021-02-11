import pytube 
import requests
import urllib.parse
import urllib.request
import re


response = requests.get("https://www.youtube.com/")
print(response)
def downlode_vid(Url):
    try:
        # creating youtube object
        video_data = pytube.YouTube(Url)
        # Informing the use that the video link is founded
        print('Video founded...')

    except:
        # Exception Handleing 
        print("Error 1 - Not able to create the youtube object")

    all_streams = video_data.streams.filter(type="video",progressive="True")

    video = all_streams.get_highest_resolution()
    # print(video.title)
    video.download(output_path=r'E:\Video\Youtube downlodes',filename=video.title)
    print("video downloded..")
    return None


url = str(input('Please enter your video title or the link of the video : '))
try:
    if "https://" in url:
        downlode_vid(url)
        print('Process complete..!')
    else:
        query_string = urllib.parse.urlencode({"search_query" : url})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'watch\?v=(\S{11})', html_content.read().decode())
        Url = "https://www.youtube.com/watch?v="+search_results[0]
        downlode_vid(Url)
        print('Process complete..!')

except Exception as e:
    print(e)

