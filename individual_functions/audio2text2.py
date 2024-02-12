import whisper_timestamped as whisper
import torch
import datetime

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