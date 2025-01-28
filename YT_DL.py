import sys
from yt_dlp import YoutubeDL

def download_video_as_mp4(youtube_url, output_file):
    """Download video and save it as the specified output file."""
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': output_file,  # Specify the output file name
            'merge_output_format': 'mp4',
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print(f"Download complete. File saved as: {output_file}")
    except Exception as e:
        print(f"Download error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python YT_DL.py <YouTube URL> <Output File>")
        sys.exit(1)

    youtube_url = sys.argv[1]
    output_file = sys.argv[2]
    download_video_as_mp4(youtube_url, output_file)
