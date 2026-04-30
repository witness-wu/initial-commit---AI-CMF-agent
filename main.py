from agents.parser_agent import run_parser
from agents.generator_agent import run_generator
from agents.evaluator_agent import run_evaluator

def main():
    user_input = input("请输入产品需求（例如：极简风蓝牙耳机）：")

    print("\n🔍 解析需求...")
    parsed = run_parser(user_input)
    print(parsed)

    print("\n🎨 生成CMF方案...")
    cmf = run_generator(parsed["product"], parsed["style"])
    print(cmf)

    print("\n📊 评估方案...")
    result = run_evaluator(cmf)
    print(result)

if __name__ == "__main__":
    main()
