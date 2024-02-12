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