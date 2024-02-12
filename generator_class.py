from functions import download_au_vi, convert_webm_to_mp3, audio2text, chatbox, generate_prompt, audio2text2
import json
import os

class Learn_From_Yt_With_ChatGPT():
    def __init__(self,
                 native_language,
                 target_language,
                 target_language_level,
                 target_language_short,
                 url,
                 speech_model='tiny',
                 language_model='gpt-3.5-turbo',
                 prompt='default prompt'):
        self.native_language = native_language
        self.target_language = target_language
        self.target_language_level = target_language_level
        self.target_language_short = target_language_short
        self.url = url
        self.speech_model = speech_model
        self.language_model = language_model
        self.message_history = []
        if prompt == 'default prompt':
            self.prompt = generate_prompt(native_language=self.native_language,
                                      target_language=self.target_language,
                                      target_language_level=self.target_language_level)
        else:
            self.prompt = prompt

    def _video2audio(self):
        self.video_dict = download_au_vi(self.url)
        self.audio_path = convert_webm_to_mp3(self.video_dict)

    def audio2text(self):
        self._video2audio()
        self.text = audio2text(self.audio_path)
        with open(f"./content/{self.video_dict['video_name']}/transcription.txt", 'w') as f:
            f.write('source: '+self.url+'\n'+self.text)
        self._remove_file()

    def audio2text2(self):
        self._video2audio()
        self.text, self.text_timestamps = audio2text2(file_path=self.audio_path,
                                                      language=self.target_language_short,
                                                      model=self.speech_model)
        with open(f"./content/{self.video_dict['video_name']}/transcription.txt", 'w') as f:
            f.write('source: '+self.url+'\n' +self.text)
        with open(f"./content/{self.video_dict['video_name']}/transcription_timestamps.txt", 'w') as f:
            f.write(self.text_timestamps)
        self._remove_file()

    def change_prompt(self, prompt):
        self.prompt = prompt

    def clear_message_history(self):
        self.message_history=[]

    def generate_material(self):
        self.reply, self.message_history = chatbox(text=self.text,
                                                   model=self.language_model,
                                                   prompt=self.prompt)

        with open(f"./content/{self.video_dict['video_name']}/reply.txt", 'w') as f:
            f.write(self.reply)

        with open(f"./content/{self.video_dict['video_name']}/message_history.json", "w") as f:
            json.dump(self.message_history, f)

    def _remove_file(self):
        os.remove(self.audio_path)
        os.remove(self.video_dict['video_path'])

    def generate_material_all_in_one(self):
        self.audio2text()
        self.generate_material()

    def generate_material_all_in_one_2(self):
        self.audio2text2()
        self.generate_material()






