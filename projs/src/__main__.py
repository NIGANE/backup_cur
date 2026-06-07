import sys
from src.parse import error_usage_func
from src.parse import parse
from src.Agent import Agent, Prompt
from llm_sdk import Small_LLM_Model
from typing import Dict, List, Any


def prompting_visualizer(prompts: List[Prompt]):
    for pt in prompts:
        print(f"- {pt.prompt} ")
        res: Dict[str, Any] = {"name": pt.name, "parameters": pt.parameters}
        print(f"|\n|-->\" {res} \n")


def main() -> None:
    try:
        if (len(sys.argv) < 7):
            error_usage_func()
        valid_data = parse()
        if not valid_data:
            print("invalid input")
            return
        #  instantiate the Model with Prompts and Functions
        agent = Agent(
            Small_LLM_Model(),
            [pt.prompt for pt in valid_data.prompts],
            valid_data.funcs
            )
        # results: List[Prompt] = agent.resolve_prompts()
        # prompting_visualizer(results)
    except BaseException as e:
        print(f"ERROR catched: {e}")


if __name__ == "__main__":
    main()
