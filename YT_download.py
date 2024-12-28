# This Python script uses the yt-dlp library to download videos from YouTube. Key features include:

# User Input: Prompts the user to enter a YouTube video link.
# High-Quality Download: Downloads the video in the best available quality (combining video and audio streams).
# Customizable Path: Saves the downloaded video to a specified directory (C:\tmp by default).
# Error Handling: Provides feedback in case of errors during the download process.
# The script is simple to use and ensures that videos are saved efficiently while offering clear feedback to the user. Perfect for quick, high-quality YouTube video downloads!

import os
from yt_dlp import YoutubeDL

def download_youtube_video(url, download_path):
    try:
        # download options
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # choosing max resolution
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # filename template
        }
        
        # create download folder
        os.makedirs(download_path, exist_ok=True)
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"Downloaded to: {download_path}")
    except Exception as e:
        print(f"Ooops! Error has occured: {e}")

if __name__ == "__main__":
    # download location
    download_directory = "C:\\tmp"
    
    # asking for video URL
    video_url = input("Hey! Put your video url here: ")
    
    # downloading video
    download_youtube_video(video_url, download_directory)
