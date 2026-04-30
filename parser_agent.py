import openai
import json
from utils.prompts import parse_prompt

def run_parser(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": parse_prompt(user_input)}]
    )
    text = response['choices'][0]['message']['content']

    try:
        return json.loads(text)
    except:
        return {"product": "未知产品", "style": ["现代"]}
