#Call Playlist function from pytube to download playlist yuotube
from pytube import Playlist 

put_url = input(str("Enter Your Playlist Link: "))
playlists = Playlist(put_url)

for video in playlists.videos:

    video.streams.get_highest_resolution().download(output_path="C:/Users/sms/Desktop/downloaded") # Choose your path to saved your videos
    video.register_on_complete_callback(print("Download Finished !")) 
