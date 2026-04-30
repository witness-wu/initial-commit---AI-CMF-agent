import openai
from utils.prompts import generate_cmf_prompt

def run_generator(product, style):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": generate_cmf_prompt(product, style)}]
    )
    return response['choices'][0]['message']['content']
