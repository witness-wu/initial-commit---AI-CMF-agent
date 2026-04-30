import openai
from utils.prompts import evaluate_prompt

def run_evaluator(cmf_text):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": evaluate_prompt(cmf_text)}]
    )
    return response['choices'][0]['message']['content']
