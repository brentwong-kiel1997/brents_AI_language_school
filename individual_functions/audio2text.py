import os
from openai import OpenAI
def speech2text(audio_path):
    ## file size needs to be kept within 25MB
    if os.stat(audio_path).st_size/(1024**2) <= 25:
        client = OpenAI()
        audio_file = open(audio_path, "rb")
        text = str(client.audio.transcriptions.create(model="whisper-1",
                                               file=audio_file).text)
        return text
    else: raise ValueError('File needs to be within 25MB!')