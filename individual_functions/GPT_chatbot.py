from openai import OpenAI

def chatbox(text,
            prompt,
            model,
            message_history= [ ]):
    client = OpenAI()
    message_history.append({'role':'user', 'content':prompt + text})
    response = client.chat.completions.create(
            model=model,
            messages=message_history
        )
    reply = response.choices[0].message.content
    message_history.append({'role':'assistant', 'content':reply})
    return reply, message_history


