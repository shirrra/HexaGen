import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_gpt(prompt, **kwargs):
  response = openai.Completion.create(
      model =  kwargs['model'] if 'model' in kwargs.keys() else 'code-davinci-002',
      prompt = prompt,
      temperature = kwargs['temp'] if 'temp' in kwargs.keys() else 0,
      max_tokens = kwargs['max_tokens'] if 'max_tokens' in kwargs.keys() else 256,
      top_p = 1,
      frequency_penalty = 0,
      presence_penalty = 0
  )
  # print(response['choices'][0]['text'])
  return response['choices'][0]['text']

