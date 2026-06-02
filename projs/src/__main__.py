import sys
from src.parse import error_usage_func
from src.parse import parse
from src.Agent import Agent
from llm_sdk import Small_LLM_Model
from typing import Dict, Any


def prompting_visualizer(agents):
    for agent in agents:
        print(f"- {agent.prompt} ")
        print(f"|\n|--> {agent.res} \n")


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
    # for pt in valid_data.prompts:

    agent = Agent(
        Small_LLM_Model(),
        valid_data.prompts[2].prompt,
        valid_data.funcs
        )
    agent.generate_json_valid()
    
    prompting_visualizer([agent])
    # res.append(buffer)
    # buffer = {}
    # print(res)


if __name__ == "__main__":
    main()
