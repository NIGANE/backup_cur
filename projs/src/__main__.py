import sys
from src.parse import error_usage_func
from src.parse import parse
from src.Agent import Agent
from llm_sdk import Small_LLM_Model
from typing import Dict, Any


def prompting_visualizer(valid_data, res):
    for prompt in valid_data.prompts:
        print(f"- {prompt} ")
        print(f"|\n|--> {"answer"}\n")


def main():
    if (len(sys.argv) < 7):
        error_usage_func()
    valid_data = parse()
    if not valid_data:
        print("invalid input")
        return
    # prompting_visualizer(valid_data, None)
    # res: list[Dict] = []
    # buffer: dict[str, Any] = {}
    agent = Agent(
        Small_LLM_Model(),
        valid_data.prompts[0].prompt,
        valid_data.funcs
        )
    agent.generate_function_name()
    print("prompt: ", valid_data.prompts[0].prompt)
    print("fn_name: ", agent.fn_name_res)
    # print([ele["name"] for ele in agent.fns])
    # buffer = agent.generate_json_valid()
    # res.append(buffer)
    # buffer = {}
    # print(res)


if __name__ == "__main__":
    main()
