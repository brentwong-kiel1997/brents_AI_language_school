from moviepy.editor import VideoFileClip

def convert_webm_to_mp3(video_dict):
    # Load the WebM video file
    webm_path = video_dict['video_path']
    mp3_path = f"./content/{video_dict['video_name']}/audio.mp3"

    video = VideoFileClip(webm_path)

    # Extract the audio from the video and save it as an MP3 file
    audio = video.audio
    audio.write_audiofile(mp3_path)

    # Close the video and audio files
    video.close()
    audio.close()

    return mp3_path
