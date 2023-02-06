# import openai
#
# # Set up the OpenAI API client
# openai.api_key = "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"
#
# # Set the model to use (e.g., "davinci")
# model_engine = "davinci"
#
# # Set the prompt for the model to generate text from
# prompt = "Write a story about a robot that becomes self-aware."
#
# # Send the request to the GPT-3 API
# completion = openai.Completion.create(
#     engine=model_engine,
#     prompt=prompt,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )
#
# # Print the generated text
# print(completion.choices[0].text)

import os
import sys

workingdirectory=os.getcwd()
print(sys.argv[1])
import openai
openai.api_key = "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"
model_engine = "text-davinci-002"
prompt = (sys.argv[1])
completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None,temperature=0.7)
message = completions.choices[0].text
print(message.strip())
