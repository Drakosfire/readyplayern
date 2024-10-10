import json
from pytubefix import YouTube
import os

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        print(f"Attempting to download: {yt.title}")
        
        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()
        
        if not stream:
            print(f"No suitable stream found for {url}")
            return
        
        # Create a valid filename
        filename = "".join([c for c in yt.title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
        filename = f"{filename}.mp4"
        file_path = os.path.join(output_path, filename)
        
        # Download the video
        stream.download(output_path=output_path, filename=filename)
        print(f"Downloaded: {yt.title} to {file_path}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
        print(f"Full error: {type(e).__name__}: {str(e)}")

def main():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the full path to videos.json
    json_path = os.path.join(script_dir, 'videos.json')
    
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: videos.json not found at {json_path}")
        return
    
    output_dir = os.path.join(script_dir, data.get('output_directory', 'downloads'))
    os.makedirs(output_dir, exist_ok=True)
    
    for video in data['videos']:
        download_video(video['url'], output_dir)

if __name__ == "__main__":
    main()
