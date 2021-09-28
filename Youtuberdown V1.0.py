#Call Playlist and YouTube functions from pytube to download video or playlist from yuotube
from pytube import Playlist , YouTube

while True:

     download_type = input("""choose one of them: 

     (1) Download One Video ?
     (2) Download Playlist videos ?

     :""")   

     if download_type == "1" :
      put_url = input("Enter Your Video Link: ")
  
      video1 = YouTube(put_url).streams.get_highest_resolution().download(output_path="C:/Users/sms/Desktop/Video_downloaded") # Choose your path to saved your video
      video2 = YouTube(put_url).register_on_complete_callback(print("Download Finished !"))
      break

     elif download_type == "2" :
      put_url = input("Enter Your Playlist Link: ")
      playlists = Playlist(put_url)

      for video in playlists.videos:

       video.streams.get_highest_resolution().download(output_path="C:/Users/sms/Desktop/Playlist_downloaded") # Choose your path to saved your playlist
       video.register_on_complete_callback(print("Download Finished !"))
       break 
     else:
      print("please Choose 1 or 2 ?")
      continue
