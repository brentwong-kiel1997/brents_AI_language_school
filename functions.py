import yt_dlp
from moviepy.editor import VideoFileClip
import os
import whisper_timestamped as whisper
import torch
import datetime
from openai import OpenAI

def download_au_vi(url):
  video_url = url
  ydl = yt_dlp.YoutubeDL()
  video_info = ydl.extract_info(video_url, download=False)
  video_name = video_info['title']
  print("Video Name:", video_name)
  output_dir = f"./content/{video_name}/"

  ydl = yt_dlp.YoutubeDL({
      'format': 'bestvideo+bestaudio',
      'outtmpl': output_dir + '%(title)s.%(ext)s',
  })

  video_info = ydl.extract_info(video_url, download=True)

  video_path = output_dir + video_name+'.webm'

  return {'video_path': video_path,
          'video_name': video_name,
          'output_dir': output_dir,
          'url':url,
          'video_info': video_info}



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


def audio2text(audio_path):
    ## file size needs to be kept within 25MB
    if os.stat(audio_path).st_size/(1024**2) <= 25:
        client = OpenAI()
        audio_file = open(audio_path, "rb")
        text = str(client.audio.transcriptions.create(model="whisper-1",
                                               file=audio_file).text)
        return text
    else: raise ValueError('File needs to be with in 25MB!')


def generate_prompt(native_language,
                    target_language,
                    target_language_level,):
    prompt = f'I am a naitve {native_language} speaker.\
       I\'m learning {target_language} and my {target_language} is at {target_language_level} level.\
       you are my {target_language} tearch. I\'ll provide an article at the end,\
       you need to generate 3 sections of learning materials for me according to this article,\
       please make sure those materials are appropriate to my {target_language} level.\n\
       section 1: important words from the article and the translation and one example sentence for each word.\n\
       section 2: important grammars used in the article and the interpretation and one example sentence for each grammar.\n\
       section 3: translation of the article into {native_language}\n\
       the atricle:\n'
    return prompt


from openai import OpenAI

def chatbox(text,
            prompt,
            model,
            message_history= [ ]):
    client = OpenAI()
    message_history.append({'role':'user', 'content':prompt + text})
    response = client.chat.completions.create(
            model = model,
            messages = message_history
        )
    reply = response.choices[0].message.content
    message_history.append({'role':'assistant', 'content':reply})
    return reply, message_history

def audio2text2(file_path, language, model):
  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  audio = whisper.load_audio(file_path)
  model = whisper.load_model(model, device=device)

  result = whisper.transcribe(model, audio, language=language)
  text_with_timestamp = ''
  for i in range(len(result['segments'])):
    time = round(result['segments'][i]['start'])
    timestamp = str(datetime.timedelta(seconds = time))
    text_with_timestamp = text_with_timestamp+timestamp+result['segments'][i]['text']+'\n'
  return result['text'], text_with_timestamp
