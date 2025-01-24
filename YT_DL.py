import os
from yt_dlp import YoutubeDL
from tkinter import Tk
from tkinter.filedialog import askdirectory

def download_video_as_mp4(youtube_url):
    try:
        # Create a dialog box to select output folder
        print("Please select the folder where you want to save the video.")
        root = Tk()
        root.withdraw()  # Hide the root window
        output_folder = askdirectory(title="Select Output Folder")
        
        if not output_folder:
            raise ValueError("No folder selected. Download canceled.")
        
        # Download options to force mp4 format
        ydl_opts = {
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',  # Ensure output is in mp4 format
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # Convert to mp4 if needed
            }]
        }
        
        # Download the video
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print("Download complete.")
        print(f"Video saved to: {output_folder}")
    
    except Exception as e:
        print(f"Download error: {e}")

# Execution
if __name__ == "__main__":
    video_url = input("YouTube URL: ")
    download_video_as_mp4(video_url)
