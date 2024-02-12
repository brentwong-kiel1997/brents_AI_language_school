# Brent's AI language School Project
## Introduction
This is a project developed by me, Brent Wong([Linkedin Profile](https://www.linkedin.com/in/mingqianwangbrent987614198/))

The main purpose of this project is to use AI to make learning materials based on short news reports from YouTube.

### Collaboration
If you like to discuss collaboration, please contact me via email [brentwang1997@gmail.com](brentwang1997@gmail.com).

### Donation
If you find this useful and would like to support my work,
you can make some donation via this [PayPal link](https://paypal.me/brentwmq?country.x=DE&locale.x=en_US
)

### Disclaimer
**Please do not share the YouTube videos downloaded using this project.**

Once the video is transcribed, the program will delete the original video and audio.
If you need to share the videos along with the materials, please share them via 
**YouTube link** or add the original video via **YouTube Embedding function**.
Make sure each time the videos are played, the original creators can benefit from those views.

The materials generated from the programming are considered as **commentaries**.

## Project Breakdown

### part 1 Get The Source

1. Download YouTube video using yt_dlp. https://github.com/yt-dlp/yt-dlp
2. Extract audio from video using moviepy. https://zulko.github.io/moviepy/

### part 2 Turn Audio into Text

#### option 1 Whisper from OpenAI
Please check out the follow link to see detail introduction of the AI.

https://openai.com/research/whisper

Advantages : 
1. It requires less processing power from the device you use.
2. It has a stable result.

#### option 2 Whisper-timestamped
Please see fine-tuned versions of Whisper and their via the link below

https://github.com/linto-ai/whisper-timestamped

Advantages :
1. This method can offer transcription of the audio with timestamps.
2. More model choices.

#### Part 3 Use ChatGPT to Generate Learning Materials
Please check out OpenAI API product page for more information

https://openai.com/product

## Usage Examples

### 0. Pre-requisite
1. Get a API key from OpenAI
https://openai.com/blog/openai-api
2. Check for package requirements from [requirements.txt](requirements.txt)
3. _(Optional)_ If you like to use Whisper-timestamped model, please
load the requirements from this link
https://github.com/linto-ai/whisper-timestamped

### 1. imports and environment setup
1. imports

`import os`

`from generator_class import Learn_From_Yt_With_ChatGPT`

2. Set up OpenAI key

`os.environ['OPENAI_API_KEY'] = 'insert your key here'
`

### 2. Set up parameters
Your native language
`native_language = 'English'`

The video language
`target_language = 'German'`

Your target language level
`target_language_level = 'B1'`

The short code for target language
`target_language_short = 'de'`

The video link
`url = 'https://www.youtube.com/watch?v=Kwv3NR0hXVY'`


### 3. Create a object from the class
Put the parameters together and create the object you'll work on.

`example=Learn_From_Yt_With_ChatGPT(native_language=native_language,
target_language=target_language,target_language_level=target_language_level,target_language_short= target_language_short,url=url)`


### 4. Create the materials using option 1 Whisper from OpenAI

#### 1. The default models used here are **Whisper from OpenAI** and **gpt-3.5-turbo**
`example.generate_material_all_in_one_()`

#### 2. _(Optional)_ Change the ChatGPT model.
If you like to use another version of ChatGPT you can change the 
model via 2 methods.
1. Specify the model when creating the object by add one more augment 
in the parameters, such as `language_model='gpt-4-32k'`

`example=Learn_From_Yt_With_ChatGPT(native_language=native_language,
target_language=target_language,target_language_level=target_language_level,target_language_short= target_language_short,url=url, language_model='gpt-4-32k)`


2. Change the parameter after creating the object

`example.language_model = gpt-4-32k`

#### 3. _(Optional)_ Change the prompt

The message that will be passed through ChatGPT is a string, **prompt+transcription**.
You can change the prompt like changing the model.
The default prompt is as following:

`prompt = f'I am a naitve {native_language} speaker. I\'m learning {target_language} and my {target_language} is at {target_language_level} level.you are my {target_language} tearch. I\'ll provide an article at the end, you need to generate 3 sections of learning materials for me according to this article, please make sure those materials are appropriate to my {target_language} level.
        \n\section 1: important words from the article and the translation and one example sentence for each word.\n\
        section 2: important grammars used in the article and the interpretation and one example sentence for each grammar.\n\
        section 3: translation of the article into {native_language}\n\
        the atricle:\n'`


1. Either specify the prompt as you set up the object parameters

`prompt='your prompt'`

2. Or change the parameter after creating the object

`example.prompt='your prompt'`


### 5. _(Optional)_ Create the materials using option 2 Whisper-timestamped
#### 1. The default models used here are 'tiny' and gpt-3.5-turbo 
`example.generate_material_all_in_one_2()
`
#### 2.  _(Optional)_ Change the Whisper-timestamped Model
1. Either specify the prompt as you set up the object parameters
`speech_model='your choice of model'`

2. Or change the parameter after creating the object
`exmaple.speech_model='your choice of model'`

please check out this following website for detailed model options
 https://github.com/linto-ai/whisper-timestamped

### 6. Find the generated materials
Please find the materials in the `/content` folder








