YouTubeClonner
==========

## Environment Setup
Install the required libraries by running the following commands:

Run the command:

```
   pip install youtube_dl
   pip install pytube
   pip install subprocess.run
```

Usage
-----

1. Open a terminal and navigate to the directory where the file is located.
2. Run the script by entering the following command:

```
   python youtube.py
```

3. When the script is executed, it will prompt you to enter the YouTube channel name and the number of videos to download.

## Notes
- Enter the YouTube channel name without spaces.
- The downloaded videos will be saved in a folder with the channel name on your desktop.
- Upon rerunning the script, it will check for already downloaded videos to prevent duplicates.

## Code Overview
The `get_channel_videos(channel_url)` function retrieves information about the videos from the YouTube channel and returns a dictionary with video titles and URLs.

The `download_video(video_dict)` function downloads videos from the channel using the provided dictionary with video information.

The `check_video_integrity(video_path)` function verifies the integrity of the video using ffmpeg.
