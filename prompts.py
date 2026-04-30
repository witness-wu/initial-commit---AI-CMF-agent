def parse_prompt(user_input):
    return f"提取产品类型和风格，返回JSON：{user_input}"

def generate_cmf_prompt(product, style):
    return f"为产品生成3套CMF方案：产品：{product} 风格：{', '.join(style)}"

def evaluate_prompt(cmf_text):
    return f"对以下方案评分并选最佳：{cmf_text}"
