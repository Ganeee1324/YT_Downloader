from yt_dlp import YoutubeDL
from tkinter import Tk
from tkinter.filedialog import askdirectory


def fetch_video_title(youtube_url):
    """Fetch the video title using yt_dlp."""
    try:
        # Fetch metadata
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


def get_output_path():
    """Prompt the user for YouTube URL and output folder, return the file path."""
    # Step 1: Get YouTube URL
    youtube_url = input("Enter the YouTube URL: ")

    # Step 2: Fetch the video title
    video_title = fetch_video_title(youtube_url)

    # Step 3: Prompt the user to select a folder
    print("Please select the folder where you want to save the video.")
    root = Tk()
    root.withdraw()  # Hide the root window
    output_folder = askdirectory(title="Select Output Folder")

    if not output_folder:
        raise ValueError("No folder selected. Exiting.")

    # Step 4: Construct the output file path
    output_file = f"{output_folder}/{video_title}.mp4"

    return youtube_url, output_file


if __name__ == "__main__":
    youtube_url, output_file = get_output_path()
    print(f"Config: URL={youtube_url}, File={output_file}")
