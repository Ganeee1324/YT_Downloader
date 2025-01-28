import os
import subprocess
from yt_dlp import YoutubeDL
from tkinter import Tk
from tkinter.filedialog import askdirectory

def fetch_video_title(youtube_url):
    """Fetch the video title using yt_dlp."""
    try:
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
        }
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=False)
            return info_dict.get('title', 'output')
    except Exception as e:
        print(f"Error fetching video title: {e}")
        return "output"


def select_output_folder():
    """Prompt the user to select an output folder."""
    print("Please select the folder where you want to save the video.")
    root = Tk()
    root.withdraw()  # Hide the root window
    folder = askdirectory(title="Select Output Folder")
    if not folder:
        raise ValueError("No folder selected. Exiting.")
    return folder


def download_video(youtube_url, output_file):
    """Download video and audio and merge them into a single file."""
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': output_file,  # Specify the output file
            'merge_output_format': 'mp4',  # Merge directly into MP4
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print(f"Download complete. File saved as: {output_file}")
    except Exception as e:
        print(f"Download error: {e}")


def convert_to_h264(input_file, output_file):
    """Use ffmpeg to convert the video to H.264 format."""
    try:
        command = [
            "ffmpeg",
            "-i", input_file,           # Input file
            "-c:v", "libx264",          # Video codec
            "-c:a", "aac",              # Audio codec
            "-strict", "experimental",  # Compatibility flag
            output_file                 # Output file
        ]
        subprocess.run(command, check=True)
        print(f"Conversion complete. File saved as: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")


if __name__ == "__main__":
    try:
        # Step 1: Prompt for YouTube URL
        youtube_url = input("Enter the YouTube URL: ")

        # Step 2: Fetch video title
        video_title = fetch_video_title(youtube_url)

        # Step 3: Ask user to select output folder
        output_folder = select_output_folder()

        # Step 4: Construct file paths
        output_file = os.path.join(output_folder, f"{video_title}.mp4")
        converted_file = os.path.join(output_folder, f"{video_title}_h264.mp4")

        # Step 5: Download the video
        download_video(youtube_url, output_file)

        # Step 6: Convert the video using ffmpeg
        convert_to_h264(output_file, converted_file)

    except Exception as e:
        print(f"An error occurred: {e}")
