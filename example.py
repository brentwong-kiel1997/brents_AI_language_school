import os
import getpass
from generator_class import Learn_From_Yt_With_ChatGPT


key = getpass.getpass('Password :: ')
os.environ['OPENAI_API_KEY'] = key

#native_language = input('please input your native language: ')
#target_language = input('please input your target language: ')
#target_language_level = input('please input your target language level: ')
#target_language_short = input('please input your target language short code, such as en for English: ')
#url = input('please input YouTube url: ')

native_language = 'English'
target_language = 'German'
target_language_level = 'B1'
target_language_short = 'de'
url = 'https://www.youtube.com/watch?v=Kwv3NR0hXVY'



example = Learn_From_Yt_With_ChatGPT(native_language=native_language,
                                     target_language=target_language,
                                     target_language_level=target_language_level,
                                     target_language_short= target_language_short,
                                     url=url)



example.generate_material_all_in_one()



